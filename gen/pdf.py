"""TMUA-format PDFs with reportlab: question papers (cover page + one question per page, like the
real test), solution booklets, and compact topic sets. Maths is rendered by gen/mathtex.py."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
                                KeepTogether, CondPageBreak)
from reportlab.lib.enums import TA_CENTER
from . import mathtex
from bank.topics import TEST, topic_index

FONT = "Times-Roman"
BOLD = "Times-Bold"
BODY = ParagraphStyle("body", fontName=FONT, fontSize=11, leading=16, spaceAfter=4)
BODY_C = ParagraphStyle("bodyc", parent=BODY, alignment=TA_CENTER)
DISP = ParagraphStyle("disp", parent=BODY, alignment=TA_CENTER, spaceBefore=4, spaceAfter=6)
ROMAN = ParagraphStyle("roman", parent=BODY, leftIndent=36, spaceAfter=2)
BUL = ParagraphStyle("bul", parent=BODY, leftIndent=24, bulletIndent=10, spaceAfter=2)
OPT = ParagraphStyle("opt", parent=BODY, leftIndent=28, spaceAfter=3)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=9, leading=12, textColor=colors.HexColor("#555555"))
H1 = ParagraphStyle("h1", fontName=BOLD, fontSize=16, leading=20, spaceAfter=8)
H2 = ParagraphStyle("h2", fontName=BOLD, fontSize=13, leading=17, spaceBefore=8, spaceAfter=4)
SOL = ParagraphStyle("sol", parent=BODY, fontSize=10, leading=14, leftIndent=12, textColor=colors.HexColor("#222222"))

IDX = topic_index()


def _blocks(text, style=BODY, size=11.0):
    out = []
    for kind, b in mathtex.to_pdf_blocks(text, size=size):
        if kind == "p":
            out.append(Paragraph(b, style))
        elif kind == "disp":
            out.append(Paragraph(b, DISP))
        elif kind == "roman":
            for rn, x in b:
                out.append(Paragraph(f"<b>{rn}</b>&nbsp;&nbsp;&nbsp;{x}", ROMAN))
        elif kind == "bullet":
            for x in b:
                out.append(Paragraph(x, BUL, bulletText="•"))
    return out


def _question(q, number, compact=False):
    """Flowables for one question: number, stem, lettered options."""
    fl = []
    stem = _blocks(q.text)
    # number sits in a two-column table with the stem so the text wraps neatly
    t = Table([[Paragraph(f"<b>{number}</b>", BODY), stem]], colWidths=[10 * mm, 155 * mm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    fl.append(t)
    fl.append(Spacer(1, 6))
    rows = []
    for letter, opt in zip(q.letters, q.options):
        body = mathtex.to_pdf_blocks(opt)
        markup = " ".join(b if kind == "p" else "" for kind, b in body) or ""
        rows.append([Paragraph(f"<b>{letter}</b>", BODY), Paragraph(markup, BODY)])
    ot = Table(rows, colWidths=[10 * mm, 145 * mm])
    ot.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 2 if compact else 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 2 if compact else 4)]))
    ot.hAlign = "LEFT"
    ot.spaceBefore = 0
    fl.append(_indent(ot))
    return fl


def _indent(flowable, left=10 * mm):
    t = Table([["", flowable]], colWidths=[left, 155 * mm])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t


def _footer_factory(label):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT, 9)
        canvas.drawCentredString(A4[0] / 2, 12 * mm, str(doc.page))
        canvas.drawString(20 * mm, 12 * mm, label)
        canvas.restoreState()
    return draw


def _doc(path, label):
    return SimpleDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
                             title=label, author="TMUA practice site"), _footer_factory(label)


def build_question_paper(path, pno, set_label, questions):
    """Cover page + one question per page + END OF TEST, like the real papers."""
    doc, footer = _doc(path, f"TMUA practice - Paper {pno} - {set_label}")
    info = TEST["papers"][pno]
    fl = [Spacer(1, 10 * mm),
          Paragraph("TEST OF MATHEMATICS FOR UNIVERSITY ADMISSION", ParagraphStyle("t", fontName=BOLD, fontSize=15, leading=19, alignment=TA_CENTER)),
          Spacer(1, 4 * mm),
          Paragraph(f"PAPER {pno}: {info['title'].split(': ')[1].upper()}", ParagraphStyle("t2", fontName=BOLD, fontSize=13, leading=17, alignment=TA_CENTER)),
          Paragraph(f"Practice paper &middot; {set_label}", BODY_C), Spacer(1, 2 * mm),
          Paragraph(f"<b>{info['minutes']} minutes</b>", BODY_C), Spacer(1, 10 * mm),
          Paragraph("<b>INSTRUCTIONS TO CANDIDATES</b>", BODY),
          Paragraph("Please read these instructions carefully, but do not open the question paper until you are told that you may do so.", BODY),
          Paragraph("A separate answer sheet is provided for this paper. You require a soft pencil and an eraser. "
                    "Please complete the answer sheet with your candidate number, centre number, date of birth and full name.", BODY),
          Paragraph(f"This paper contains <b>{info['questions']} questions</b>. For each question, choose the <b>one</b> answer you consider correct and record your "
                    "choice on the separate answer sheet. If you make a mistake, erase thoroughly and try again.", BODY),
          Paragraph("There are no penalties for incorrect responses, only marks for correct answers, so you should attempt all "
                    f"{info['questions']} questions. Each question is worth one mark.", BODY),
          Paragraph("You can use the question paper for rough working or notes, but no extra paper is allowed.", BODY),
          Paragraph("You must complete the answer sheet within the time limit.", BODY),
          Paragraph("<b>Calculators and dictionaries are NOT permitted.</b>", BODY),
          Paragraph("<b>There is no formulae booklet for this test.</b>", BODY),
          Paragraph("Please wait to be told you may begin before turning this page.", BODY),
          Spacer(1, 14 * mm),
          Paragraph("This is a practice paper generated from a question bank written to the TMUA content specification. "
                    "It is not an official UAT-UK paper. Answers and worked solutions are in the accompanying solutions booklet.", SMALL),
          PageBreak(), Spacer(1, 100 * mm), Paragraph("BLANK PAGE", BODY_C), PageBreak()]
    for i, q in enumerate(questions, 1):
        fl += _question(q, i)
        if i < len(questions):
            fl.append(PageBreak())
    fl += [Spacer(1, 12 * mm), Paragraph("<b>END OF TEST</b>", BODY_C)]
    doc.build(fl, onFirstPage=footer, onLaterPages=footer)


def _answer_table(questions):
    rows = [["Question", "Answer", "Topic"]]
    for i, q in enumerate(questions, 1):
        rows.append([str(i), q.answer, IDX[q.topic]["name"]])
    t = Table(rows, colWidths=[22 * mm, 22 * mm, 90 * mm], repeatRows=1)
    t.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), FONT, 10), ("FONT", (0, 0), (-1, 0), BOLD, 10),
                           ("GRID", (0, 0), (-1, -1), 0.4, colors.grey), ("ALIGN", (0, 0), (1, -1), "CENTER"),
                           ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee"))]))
    t.hAlign = "LEFT"
    return t


def build_solutions(path, title, subtitle, questions, numbered=True):
    """Answer key table followed by every question with its answer and worked solution."""
    doc, footer = _doc(path, title)
    fl = [Paragraph(title, H1), Paragraph(subtitle, SMALL), Spacer(1, 4 * mm),
          Paragraph("Answer key", H2), _answer_table(questions), PageBreak(), Paragraph("Worked solutions", H1)]
    for i, q in enumerate(questions, 1):
        label = str(i) if numbered else q.id
        block = [Paragraph(f"<b>Question {label}</b> &nbsp; <font size=9 color='#555555'>{q.id} &middot; {IDX[q.topic]['name']} &middot; spec {q.spec}</font>", H2)]
        block += _blocks(q.text, size=10.5)
        block.append(Paragraph(f"<b>Answer: {q.answer}</b>", BODY))
        block += _blocks(q.solution, style=SOL, size=10)
        block.append(Spacer(1, 4))
        fl.append(KeepTogether(block))
    doc.build(fl, onFirstPage=footer, onLaterPages=footer)


def build_topic_set(path, title, subtitle, questions):
    """Compact 'questions by topic' paper: several questions per page, numbered 1..n."""
    doc, footer = _doc(path, title)
    fl = [Paragraph(title, H1), Paragraph(subtitle, SMALL),
          Paragraph("Each question has one correct answer. No calculator. Answers and worked solutions are in the separate solutions PDF.", SMALL),
          Spacer(1, 6 * mm)]
    for i, q in enumerate(questions, 1):
        fl.append(CondPageBreak(70 * mm))
        fl.append(KeepTogether(_question(q, i, compact=True) + [Spacer(1, 8 * mm)]))
    doc.build(fl, onFirstPage=footer, onLaterPages=footer)
