"""Question markup -> HTML (maths left as \\( \\) / \\[ \\] for KaTeX) and -> reportlab
paragraph markup (maths rendered to PNG with matplotlib mathtext and placed inline).
"""
import os, re, html, hashlib
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["mathtext.fontset"] = "stix"
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "build-cache", "math")
os.makedirs(CACHE, exist_ok=True)

# split on $$...$$ first, then $...$
_TOK = re.compile(r"(\$\$.+?\$\$|\$.+?\$)", re.S)
_ROMAN = re.compile(r"^(I|II|III|IV|V|VI)\.\s+(.*)$")
_BOLD = re.compile(r"\*\*(.+?)\*\*")

# aliases KaTeX accepts but mathtext does not
_PDF_SUBS = [(r"\le ", r"\leq "), (r"\ge ", r"\geq "), (r"\implies", r"\Rightarrow"), (r"\displaystyle", ""),
             (r"\tfrac", r"\frac"), (r"\textbf", r"\mathbf"), (r"\iff", r"\Leftrightarrow"), (r"\big", ""), (r"\Big", ""),
             (r"\pounds", "£"), (r"\dot{", r"\dot{")]
_TWO_ARG = ("\\frac", "\\dfrac", "\\tfrac", "\\binom")
_ONE_ARG = ("\\sqrt", "\\mathbf", "\\mathrm", "\\vec", "\\hat", "\\bar", "\\overline", "\\underline", "\\dot", "\\overrightarrow", "\\text")


def _read_arg(s, i):
    """Read one TeX argument starting at s[i] (after optional spaces): {...}, a control word, or one char.
    Returns (braced_text, next_index) or (None, i) if nothing usable is there."""
    n = len(s)
    while i < n and s[i] == " ":
        i += 1
    if i >= n:
        return None, i
    if s[i] == "{":
        depth, j = 0, i
        while j < n:
            if s[j] == "{":
                depth += 1
            elif s[j] == "}":
                depth -= 1
                if depth == 0:
                    return "{" + _brace_args(s[i + 1:j]) + "}", j + 1
            j += 1
        return None, i
    if s[i] == "\\":
        j = i + 1
        while j < n and s[j].isalpha():
            j += 1
        if j == i + 1:
            j += 1
        return "{" + s[i:j] + "}", j
    if s[i] == "[":   # optional argument (\sqrt[3]{x}) - leave untouched
        return None, i
    return "{" + s[i] + "}", i + 1


def _brace_args(tex):
    """Rewrite \\frac12, \\frac\\pi3, \\binom nr, \\sqrt2 etc. into fully braced forms mathtext accepts."""
    out, i, n = [], 0, len(tex)
    while i < n:
        hit = None
        for cmd in _TWO_ARG + _ONE_ARG:
            if tex.startswith(cmd, i) and not (i + len(cmd) < n and tex[i + len(cmd)].isalpha()):
                hit = cmd
                break
        if not hit:
            if tex[i] == "{":
                a, j = _read_arg(tex, i)
                if a is not None:
                    out.append(a)
                    i = j
                    continue
            out.append(tex[i])
            i += 1
            continue
        j = i + len(hit)
        if hit == "\\sqrt" and j < n and tex[j:].lstrip().startswith("["):
            k = tex.index("]", j) + 1
            out.append(hit + tex[j:k])
            a, j2 = _read_arg(tex, k)
            out.append(a if a else "")
            i = j2 if a else k
            continue
        nargs = 1 if hit in _ONE_ARG else 2
        args = []
        for _ in range(nargs):
            a, j = _read_arg(tex, j)
            if a is None:
                break
            args.append(a)
        if len(args) < nargs:
            out.append(hit)
            i += len(hit)
            continue
        out.append(hit + "".join(args))
        i = j
    return "".join(out)


def _normalise(tex):
    for a, b in _PDF_SUBS:
        tex = tex.replace(a, b)
    return _brace_args(tex)


def math_spans(text):
    """Yield (is_math, display, content) tokens."""
    for tok in _TOK.split(text):
        if not tok:
            continue
        if tok.startswith("$$"):
            yield True, True, tok[2:-2].strip()
        elif tok.startswith("$"):
            yield True, False, tok[1:-1].strip()
        else:
            yield False, False, tok


# ---------------------------------------------------------------- HTML ----
def _inline_html(s):
    out = []
    for is_math, disp, c in math_spans(s):
        if is_math:
            out.append(("\\[" + c + "\\]") if disp else ("\\(" + c + "\\)"))
        else:
            out.append(html.escape(c, quote=False))
    # Bold is applied after joining so that **...** may span a maths snippet.
    return _BOLD.sub(r"<b>\1</b>", "".join(out))


def to_html(text):
    """Paragraphs, roman-numeral statement lists and bullets -> HTML."""
    blocks = re.split(r"\n\s*\n", text.strip())
    out = []
    for b in blocks:
        lines = b.strip().split("\n")
        if all(_ROMAN.match(l.strip()) for l in lines):
            out.append("<ol class='roman'>" + "".join(
                f"<li><span class='rn'>{_ROMAN.match(l.strip()).group(1)}</span>{_inline_html(_ROMAN.match(l.strip()).group(2))}</li>" for l in lines) + "</ol>")
        elif all(l.strip().startswith("- ") for l in lines):
            out.append("<ul>" + "".join(f"<li>{_inline_html(l.strip()[2:])}</li>" for l in lines) + "</ul>")
        elif b.strip().startswith("$$") and b.strip().endswith("$$") and b.count("$$") == 2:
            out.append(f"<div class='disp'>{_inline_html(b.strip())}</div>")
        else:
            out.append("<p>" + _inline_html("\n".join(lines)).replace("\n", "<br>") + "</p>")
    return "\n".join(out)


def to_text(text):
    """Plain text (for search indexes): strips markup, keeps the LaTeX source."""
    t = re.sub(r"\$\$?", " ", text)
    t = _BOLD.sub(r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+", lambda m: " " + m.group(0)[1:] + " ", t)
    t = re.sub(r"[{}^_]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# ----------------------------------------------------------------- PDF ----
_parser = mathtext.MathTextParser("agg")


def render_math(tex, size=11.0, dpi=400):
    """Render one maths snippet to a cached PNG. Returns (path, width_pt, height_pt, depth_pt)."""
    tex = _normalise(tex)
    key = hashlib.md5(f"{tex}|{size}|{dpi}".encode()).hexdigest()
    png = os.path.join(CACHE, key + ".png")
    meta = os.path.join(CACHE, key + ".txt")
    if os.path.exists(png) and os.path.exists(meta):
        w, h, d = map(float, open(meta).read().split())
        return png, w, h, d
    r = _parser.parse("$" + tex + "$", dpi=dpi, prop=FontProperties(size=size))
    img = np.asarray(r.image)
    if img.ndim == 2:   # grayscale alpha -> black RGBA
        rgba = np.zeros(img.shape + (4,), dtype=np.uint8)
        rgba[..., 3] = img
    else:
        rgba = img
    Image.fromarray(rgba, "RGBA").save(png)
    scale = 72.0 / dpi
    w, h, d = r.width * scale, r.height * scale, r.depth * scale
    open(meta, "w").write(f"{w} {h} {d}")
    return png, w, h, d


def check_math(text):
    """Raise if any maths snippet cannot be parsed by mathtext (used by build validation)."""
    for is_math, disp, c in math_spans(text):
        if is_math:
            t = _normalise(c)
            _parser.parse("$" + t + "$", dpi=72, prop=FontProperties(size=11))


def _inline_pdf(s, size):
    out = []
    for is_math, disp, c in math_spans(s):
        if is_math and re.fullmatch(r"\^\{?(\d)\}?", c):   # cm$^2$ etc.: use a text superscript
            out.append(f"<super>{c.strip('^{}')}</super>")
        elif is_math:
            png, w, h, d = render_math(c, size=size + (1 if disp else 0))
            out.append(f'<img src="{png}" width="{w:.2f}" height="{h:.2f}" valign="{-d:.2f}"/>')
        else:
            out.append(html.escape(c, quote=False))
    return _BOLD.sub(r"<b>\1</b>", "".join(out))


def to_pdf_blocks(text, size=11.0):
    """Returns a list of ('p'|'roman'|'bullet'|'disp', markup) blocks for gen/pdf.py."""
    blocks = re.split(r"\n\s*\n", text.strip())
    out = []
    for b in blocks:
        lines = b.strip().split("\n")
        if all(_ROMAN.match(l.strip()) for l in lines):
            out.append(("roman", [(_ROMAN.match(l.strip()).group(1), _inline_pdf(_ROMAN.match(l.strip()).group(2), size)) for l in lines]))
        elif all(l.strip().startswith("- ") for l in lines):
            out.append(("bullet", [_inline_pdf(l.strip()[2:], size) for l in lines]))
        elif b.strip().startswith("$$") and b.strip().endswith("$$") and b.count("$$") == 2:
            out.append(("disp", _inline_pdf(b.strip(), size)))
        else:
            out.append(("p", _inline_pdf("\n".join(lines), size).replace("\n", "<br/>")))
    return out
