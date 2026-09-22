"""Static site generator: layout, shared CSS/JS, question rendering and the main pages.
All state (progress, attempts, timers, scores) lives in the browser's localStorage under `tmua.*`,
so the site works as plain files or on GitHub Pages with no server. Maths is rendered by KaTeX
(loaded from jsDelivr) via auto-render on \\( \\) and \\[ \\] delimiters."""
import html, json, re
from bank.topics import TEST, GROUPS, topic_index, PAPER_TOPICS
from bank.official_index import OFFICIAL_INDEX
from bank.official_keys import KEYS, GRADES, SERIES, DEFAULT_GRADE_SERIES
from . import mathtex

IDX = topic_index()
EXAM_SECONDS = 75 * 60
NOTES_ALL = {}
FACTS = []
OFFICIAL_FILES = []

KATEX = ('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
         '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
         '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>')

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Source+Sans+3:wght@400;600;700&display=swap');
:root{--navy:#14213d;--ink:#1b2432;--teal:#0b7a75;--teal-dark:#075e5a;--teal-light:#dff3f1;--gold:#e0a91a;--gold-light:#fff3d1;--paper:#f6f5f0;--paper-dark:#ebe9e1;--stone:#5f6b7a;--line:#d9d6cc;
--p1:#2a5d8f;--p1-light:#e1ecf7;--p2:#7a3e9d;--p2-light:#eee3f5;--card:#fff;--head:#14213d;--sol-bg:#eef7f6;--sol-line:#c6e3df;--note-bg:#fff8e6;--note-line:#ecd9a3;--input:#fff;
--ok:#2e8b57;--warn:#d9a441;--bad:#c0554a;--ok-light:#e3f3e8;--bad-light:#f9e3e0}
[data-theme=dark]{--navy:#0b1220;--ink:#e6e8ee;--teal:#5cc8c1;--teal-dark:#8fdcd6;--teal-light:#12302e;--gold:#e8bd4f;--gold-light:#3a2f10;--paper:#121820;--paper-dark:#1a222c;--stone:#a4adba;--line:#2a3441;
--p1-light:#16283a;--p2-light:#2a1c36;--card:#182029;--head:#e6e8ee;--sol-bg:#152624;--sol-line:#28504b;--note-bg:#2b2716;--note-line:#5a4c22;--input:#0f151c;--ok-light:#183426;--bad-light:#3a1f1c}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:'Source Sans 3',Segoe UI,Arial,sans-serif;font-size:17px;color:var(--ink);background:var(--paper);line-height:1.55}
h1,h2,h3,.brand{font-family:Fraunces,Georgia,'Times New Roman',serif;font-weight:700;letter-spacing:-.01em}
a{color:var(--teal-dark)}code{background:var(--paper-dark);padding:1px 5px;border-radius:4px;font-size:.9em}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
header.top{background:var(--navy);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 2px 12px rgba(0,0,0,.18)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;min-height:62px}
header.top a{color:#fff;text-decoration:none}.brand{font-size:1.25rem;display:flex;align-items:center;gap:10px}.brand .sig{font-family:'Times New Roman',serif;font-style:italic;background:var(--gold);color:#14213d;border-radius:8px;padding:0 8px;font-size:1.1rem}
header.top nav{display:flex;align-items:center;flex-wrap:wrap}header.top nav a{margin-left:16px;font-size:.94rem;opacity:.9;padding:6px 0;border-bottom:2px solid transparent}header.top nav a:hover,header.top nav a.on{opacity:1;border-color:var(--gold)}
button.icon-btn{margin-left:16px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:8px;padding:5px 10px;cursor:pointer;font-size:.9rem;font-family:inherit}button.icon-btn:hover{background:rgba(255,255,255,.22)}
.hero{position:relative;overflow:hidden;background:linear-gradient(135deg,#14213d 0%,#1f3a63 55%,#0b7a75 100%);color:#fff;padding:54px 0 48px}
.hero:before{content:"";position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'><g fill='none' stroke='rgba(255,255,255,0.10)' stroke-width='1'><path d='M0 60h120M60 0v120'/><circle cx='60' cy='60' r='40'/><path d='M20 100L100 20'/></g></svg>");opacity:.6}
.hero .wrap{position:relative}.hero h1{margin:0 0 10px;font-size:2.4rem;line-height:1.15}.hero p{margin:0;max-width:780px;color:rgba(255,255,255,.88);font-size:1.08rem}
.hero .crumbs{font-size:.9rem;margin-bottom:14px;color:rgba(255,255,255,.75)}.hero .crumbs a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.4)}.hero .crumbs span{margin:0 8px;opacity:.6}
.hero.p1{background:linear-gradient(135deg,#1a3a5c 0%,#2a5d8f 60%,#3f7fb5 100%)}.hero.p2{background:linear-gradient(135deg,#3d1f52 0%,#7a3e9d 60%,#9a5fbf 100%)}
.hero.small{padding:34px 0 30px}.hero.small h1{font-size:1.9rem}
.pill{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:3px 12px;font-size:.82rem;margin-right:8px;margin-top:10px}
main{padding:30px 0 40px}
h2.sec{font-size:1.55rem;color:var(--head);margin:34px 0 14px;display:flex;align-items:center;gap:12px}h2.sec:after{content:"";flex:1;height:1px;background:var(--line)}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}@media(max-width:860px){.grid3{grid-template-columns:1fr}}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}@media(max-width:860px){.grid2{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 24px;box-shadow:0 1px 3px rgba(20,33,61,.06)}
.card h3{margin:0 0 8px;font-size:1.25rem;color:var(--head)}.card p{margin:0 0 10px;color:var(--stone)}
.stat{font-family:Fraunces,serif;font-size:2.2rem;color:var(--teal);line-height:1}
a.btn,button.btn{display:inline-block;background:var(--teal);color:#fff;text-decoration:none;padding:9px 16px;border-radius:8px;font-weight:600;font-size:.95rem;border:0;cursor:pointer;font-family:inherit}a.btn:hover,button.btn:hover{background:var(--teal-dark)}
[data-theme=dark] a.btn,[data-theme=dark] button.btn{color:#0b1220}
a.btn.ghost,button.btn.ghost{background:transparent;color:var(--teal-dark);border:1.5px solid var(--teal)}a.btn.ghost:hover,button.btn.ghost:hover{background:var(--teal-light)}
a.btn.gold,button.btn.gold{background:var(--gold);color:#14213d}
.paper-head{display:flex;align-items:center;gap:14px;margin:8px 0 14px}.paper-head .tag{white-space:nowrap;font-family:Fraunces,serif;font-size:1.05rem;font-weight:700;color:#fff;border-radius:8px;padding:4px 12px}
.tag.p1{background:var(--p1)}.tag.p2{background:var(--p2)}.tag.s2{background:var(--teal)}.paper-head span.assessed{color:var(--stone);font-size:.95rem}
.topic-card{display:flex;gap:16px;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;transition:transform .12s,box-shadow .12s}
.topic-card:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(20,33,61,.12)}
.topic-card .icon{flex:0 0 46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-family:Fraunces,serif;font-weight:700;font-size:.85rem}
.icon.part1{background:var(--p1-light);color:var(--p1)}.icon.part2{background:var(--teal-light);color:var(--teal-dark)}.icon.section2{background:var(--p2-light);color:var(--p2)}[data-theme=dark] .icon.part1{color:#8fc3ea}[data-theme=dark] .icon.section2{color:#cfa0e8}
.topic-card>div:last-child{flex:1;min-width:0}.topic-card h3{margin:0 0 3px;font-size:1.08rem;color:var(--head)}.topic-card .meta{color:var(--stone);font-size:.86rem}
.links{display:flex;flex-wrap:wrap;gap:6px}.links a{font-size:.82rem;padding:4px 11px;border-radius:999px;text-decoration:none;border:1px solid var(--line);background:var(--paper);color:var(--teal-dark);font-weight:600}
.links a:hover{background:var(--teal-light);border-color:var(--teal)}
table.list{border-collapse:collapse;width:100%;margin:10px 0 24px;background:var(--card);border-radius:12px;overflow:hidden;border:1px solid var(--line)}
table.list th,table.list td{padding:9px 14px;text-align:left;font-size:.95rem;vertical-align:top;border-bottom:1px solid var(--line)}table.list th{background:var(--paper-dark);color:var(--head)}table.list tr:last-child td{border-bottom:0}
/* questions */
.q{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:20px 0;box-shadow:0 1px 3px rgba(20,33,61,.05);border-left-width:5px}
.q[data-status="1"]{border-left-color:var(--warn)}.q[data-status="2"]{border-left-color:var(--ok)}
.q .qh{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:10px}
.q .qh .num{font-family:Fraunces,serif;font-weight:700;color:var(--head);font-size:1.15rem}.q .meta{font-size:.82rem;color:var(--stone)}.q .meta .d{color:var(--gold);letter-spacing:1px}
.q .qt p{margin:6px 0}.q .disp{margin:8px 0;text-align:center}ol.roman{list-style:none;padding-left:30px;margin:8px 0}ol.roman li{margin:4px 0;position:relative}ol.roman .rn{position:absolute;left:-30px;font-weight:700;width:26px;text-align:right}
ol.opts{list-style:none;padding:0;margin:12px 0 4px;display:grid;grid-template-columns:1fr 1fr;gap:6px 14px}@media(max-width:720px){ol.opts{grid-template-columns:1fr}}
ol.opts li{display:flex;gap:10px;align-items:flex-start;padding:8px 12px;border:1px solid var(--line);border-radius:10px;cursor:pointer;background:var(--paper);transition:background .12s,border-color .12s}
ol.opts li:hover{border-color:var(--teal)}ol.opts li .lt{font-weight:700;font-family:Fraunces,serif;min-width:18px;color:var(--teal-dark)}
ol.opts li.pick{border-color:var(--p1);background:var(--p1-light)}ol.opts li.right{border-color:var(--ok);background:var(--ok-light)}ol.opts li.wrong{border-color:var(--bad);background:var(--bad-light)}
.q.done ol.opts li{cursor:default}
.fb{margin:10px 0 4px;font-weight:700;min-height:1.2em}.fb.ok{color:var(--ok)}.fb.bad{color:var(--bad)}
details.sol{margin-top:10px;background:var(--sol-bg);border:1px solid var(--sol-line);border-radius:10px;padding:10px 14px}details.sol summary{cursor:pointer;font-weight:700;color:var(--teal-dark)}
details.sol .src{font-size:.85rem;color:var(--stone);margin-top:8px;border-top:1px dashed var(--sol-line);padding-top:6px}
.note{background:var(--note-bg);border:1px solid var(--note-line);border-radius:10px;padding:12px 16px;font-size:.95rem}
footer{background:var(--navy);color:rgba(255,255,255,.75);padding:26px 0;font-size:.88rem;margin-top:40px}footer a{color:#fff}
/* progress */
.st{display:inline-flex;gap:4px;margin-left:auto}.st button{font-family:inherit;font-size:.78rem;border:1px solid var(--line);background:var(--paper);color:var(--stone);border-radius:999px;padding:2px 10px;cursor:pointer}
.st button:hover{border-color:var(--teal)}.st button.on[data-s="1"]{background:var(--warn);color:#222;border-color:var(--warn)}.st button.on[data-s="2"]{background:var(--ok);color:#fff;border-color:var(--ok)}
.prog{display:flex;align-items:center;gap:10px;font-size:.82rem;color:var(--stone);margin-top:8px}.prog .bar{flex:1;height:8px;background:var(--paper-dark);border-radius:999px;overflow:hidden;display:flex;max-width:260px}
.prog .bar .ok{background:var(--ok);height:100%}.prog .bar .wk{background:var(--warn);height:100%}.prog .pl{white-space:nowrap;min-width:90px}
.hero .prog{color:rgba(255,255,255,.85)}.hero .prog .bar{background:rgba(255,255,255,.25)}
/* filter bar & tools */
.filterbar{position:sticky;top:var(--hdr,62px);z-index:10;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin:10px 0 6px;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.filterbar input[type=search]{flex:1 1 200px;font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.filterbar label{font-size:.85rem;color:var(--stone);display:inline-flex;align-items:center;gap:4px;cursor:pointer}.chip{border:1px solid var(--line);border-radius:999px;padding:2px 10px;background:var(--paper);color:var(--stone);font-size:.82rem;cursor:pointer;font-family:inherit}
.chip.on{background:var(--teal);color:#fff;border-color:var(--teal)}.filterbar .cnt{font-size:.85rem;color:var(--stone);margin-left:auto}
.filterbar select,.qf-controls select,.plan select{font:inherit;font-size:.88rem;padding:5px 8px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.tools{position:sticky;top:var(--hdr,62px);z-index:10;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 16px;margin:10px 0;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.tools .time{font-family:Fraunces,serif;font-size:1.6rem;font-weight:700;color:var(--head);min-width:110px}.tools .time.low{color:var(--bad)}
.tools .score{font-weight:700;color:var(--teal-dark)}.tools .score b{font-family:Fraunces,serif;font-size:1.3rem}.tools .pct{font-size:.85rem;color:var(--stone)}
.tools button{font-family:inherit;font-size:.88rem;padding:6px 12px;border-radius:8px;border:1px solid var(--teal);background:transparent;color:var(--teal-dark);cursor:pointer}.tools button.primary{background:var(--teal);color:#fff}
.q.hide{display:none}
/* answer grid for papers */
.agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;margin:14px 0}.agrid .cell{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:6px 8px}
.agrid .cell b{display:inline-block;width:26px;font-family:Fraunces,serif}.agrid .cell .ls{display:inline-flex;gap:2px;flex-wrap:wrap}.agrid .cell .ls button{width:22px;height:22px;border-radius:5px;border:1px solid var(--line);background:var(--paper);font-size:.72rem;cursor:pointer;padding:0;font-family:inherit;color:var(--ink)}
.agrid .cell .ls button.on{background:var(--p1);color:#fff;border-color:var(--p1)}.agrid .cell.right{border-color:var(--ok);background:var(--ok-light)}.agrid .cell.wrong{border-color:var(--bad);background:var(--bad-light)}.agrid .cell.blank{border-color:var(--warn)}
.agrid .cell .k{font-size:.75rem;color:var(--stone);margin-left:6px}
.result{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;margin:14px 0}.result .big{font-family:Fraunces,serif;font-size:2.4rem;color:var(--teal);line-height:1}.result .grade{font-family:Fraunces,serif;font-size:1.6rem;color:var(--gold)}
.pdfbox{width:100%;height:78vh;border:1px solid var(--line);border-radius:12px;background:#fff}
/* quick-fire & search */
.qf-controls{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:10px 0 16px}.qf-controls label{font-size:.9rem;color:var(--stone);display:inline-flex;gap:5px;align-items:center}
.qf-controls input[type=search]{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.kbd{font-size:.8rem;color:var(--stone)}.kbd kbd{border:1px solid var(--line);border-radius:4px;padding:0 5px;background:var(--paper-dark);font-family:inherit}
.res{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0;text-decoration:none;color:inherit}.res:hover{border-color:var(--teal)}
.res .t{font-weight:700;color:var(--head)}.res .m{font-size:.82rem;color:var(--stone)}.res .s{font-size:.92rem;margin-top:4px}.res mark{background:#ffe58a;color:#222;border-radius:3px;padding:0 2px}
.empty{color:var(--stone);font-style:italic}
#totop{position:fixed;right:18px;bottom:18px;z-index:15;background:var(--teal);color:#fff;border:0;border-radius:50%;width:42px;height:42px;font-size:1.2rem;cursor:pointer;box-shadow:0 3px 10px rgba(0,0,0,.25);opacity:0;pointer-events:none;transition:opacity .2s}#totop.show{opacity:1;pointer-events:auto}
.jump{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 4px}.jump a{font-size:.82rem;padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:var(--paper);color:var(--teal-dark);text-decoration:none;font-weight:600}.jump a:hover{background:var(--teal-light)}
.real .row{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;padding:8px 0;border-bottom:1px dashed var(--line);font-size:.95rem}.real .row .ser{font-weight:700;color:var(--head);min-width:150px}.real .row .qn{color:var(--stone);min-width:90px}.real .row .t{flex:1 1 300px}
.real .row a{font-size:.82rem;padding:2px 9px;border-radius:999px;border:1px solid var(--line);background:var(--paper);text-decoration:none;font-weight:600}
.plan input[type=date]{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}.plan .big{font-family:Fraunces,serif;font-size:2rem;color:var(--teal)}
table.list td .bar{height:8px;background:var(--paper-dark);border-radius:999px;overflow:hidden;display:flex;width:140px}table.list td .bar .ok{background:var(--ok)}table.list td .bar .wk{background:var(--warn)}
@media(max-width:720px){header.top{position:static}header.top nav a{margin-left:12px;font-size:.88rem}.filterbar,.tools{top:0}.hero h1{font-size:1.8rem}.hero{padding:34px 0 28px}}
/* drills, facts */
.drill{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin:14px 0;min-height:160px}
.drill .term{font-family:Fraunces,serif;font-size:1.35rem;color:var(--head);margin:0 0 6px}.drill .def{font-size:1.05rem;margin:8px 0}.drill .src{font-size:.82rem;color:var(--stone)}
.drill .btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}.drill input.ans{font:inherit;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink);width:100%;max-width:420px}
.drill .fbk{margin-top:8px;font-weight:700}.drill .fbk.ok{color:var(--ok)}.drill .fbk.bad{color:var(--bad)}
.drill .work{background:var(--paper-dark);border-radius:8px;padding:10px 14px;font-size:.95rem;margin-top:8px}
.modecard{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:14px}.modecard .mi{font-size:1.6rem;flex:0 0 40px;text-align:center}.modecard h3{margin:0 0 4px;color:var(--head)}.modecard p{margin:0 0 8px;color:var(--stone)}
.due{font-size:.85rem;color:var(--stone)}
/* notes */
.notes{max-width:900px}.notes h2{font-size:1.4rem;color:var(--head);margin:34px 0 8px;padding-top:8px;border-top:1px solid var(--line)}
.notes p{margin:8px 0}.notes ul,.notes ol{margin:6px 0 10px 22px;padding:0}.notes li{margin:5px 0}
.notes .summary{font-size:1.1rem;line-height:1.6;background:var(--teal-light);border-left:4px solid var(--teal);border-radius:0 12px 12px 0;padding:14px 18px;margin:18px 0}
.nums{background:var(--note-bg);border:1px solid var(--note-line);border-radius:12px;padding:12px 18px;margin:16px 0}.nums h3,.examh h3{margin:0 0 6px;font-size:1.05rem;color:var(--head)}.nums ul{columns:2;column-gap:24px}@media(max-width:720px){.nums ul{columns:1}}
.examh{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin:16px 0}
.traps{background:var(--bad-light);border:1px solid var(--bad);border-radius:12px;padding:12px 18px;margin:16px 0}.traps h3{margin:0 0 6px;font-size:1.05rem;color:var(--bad)}
.worked{background:var(--sol-bg);border:1px solid var(--sol-line);border-radius:12px;padding:12px 18px;margin:16px 0}
.toc{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 18px;margin:14px 0 6px;font-size:.92rem}.toc b{color:var(--head)}.toc a{margin-right:14px;white-space:nowrap;line-height:1.9}
.nlinks{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}
.notes-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:860px){.notes-grid{grid-template-columns:1fr}}
.ncard{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;text-decoration:none;color:inherit}.ncard:hover{border-color:var(--teal)}.ncard b{color:var(--head)}.ncard span{display:block;font-size:.85rem;color:var(--stone)}
table.grades{border-collapse:collapse;font-size:.88rem;background:var(--card);border:1px solid var(--line)}table.grades th,table.grades td{border:1px solid var(--line);padding:3px 8px;text-align:center}table.grades th{background:var(--paper-dark)}
.katex{font-size:1.06em}
/* print */
@media print{header.top,footer,.tools,.filterbar,.st,.pill,.hero .crumbs,.prog,.noprint,#totop{display:none!important}
body{background:#fff;color:#000;font-size:12pt}.hero{background:#fff!important;color:#000;padding:10px 0}.hero p,.hero h1{color:#000}.hero:before{display:none}
.q{break-inside:avoid;box-shadow:none;border:1px solid #999;page-break-inside:avoid}details.sol{display:none}body.print-sol details.sol{display:block;background:#f3f3f3}body.print-sol details.sol summary{display:none}
ol.opts li{background:#fff;border-color:#bbb}a{color:#000;text-decoration:none}}
"""

# Shared JavaScript: theme, KaTeX rendering, progress, attempts, MCQ interaction, filtering, timer helpers.
JS = r"""
(function(){
const LS=k=>{try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}};
const SV=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
window.TM={LS,SV};
/* ---- maths ---- */
window.TM.math=function(root){root=root||document.body;if(window.renderMathInElement){try{renderMathInElement(root,{delimiters:[{left:'\\(',right:'\\)',display:false},{left:'\\[',right:'\\]',display:true}],throwOnError:false});}catch(e){}}};
document.addEventListener('DOMContentLoaded',()=>{const go=()=>window.renderMathInElement?window.TM.math():setTimeout(go,60);go();});
/* ---- theme ---- */
const root=document.documentElement;
function applyTheme(t){if(t==='dark')root.dataset.theme='dark';else delete root.dataset.theme;const b=document.getElementById('themeBtn');if(b)b.textContent=t==='dark'?'☀ Light':'☾ Dark';}
applyTheme(LS('tmua.theme')||'light');
const tb=document.getElementById('themeBtn');if(tb)tb.onclick=()=>{const t=root.dataset.theme==='dark'?'light':'dark';SV('tmua.theme',t);applyTheme(t);};
/* ---- progress: 0 untried, 1 needs work, 2 secure; attempts: {n, c, last} ---- */
let prog=LS('tmua.progress')||{};let att=LS('tmua.attempts')||{};
window.TM.prog=()=>prog;window.TM.att=()=>att;
window.TM.setProg=(id,s)=>{if(s)prog[id]=s;else delete prog[id];SV('tmua.progress',prog);window.TM.schedule(id,s);};
window.TM.record=(id,correct)=>{const a=att[id]||{n:0,c:0};a.n++;if(correct)a.c++;a.last=Date.now();a.ok=correct?1:0;att[id]=a;SV('tmua.attempts',att);};
function paint(){
  document.querySelectorAll('.q[data-qid]').forEach(el=>{const s=prog[el.dataset.qid]||0;el.dataset.status=s;el.querySelectorAll('.st button[data-s]').forEach(b=>b.classList.toggle('on',+b.dataset.s===s&&s>0));});
  document.querySelectorAll('[data-qids]').forEach(el=>{const ids=el.dataset.qids.split(',').filter(Boolean);const n=ids.length;if(!n)return;
    const ok=ids.filter(i=>prog[i]===2).length,wk=ids.filter(i=>prog[i]===1).length;
    const o=el.querySelector('.bar .ok'),w=el.querySelector('.bar .wk'),p=el.querySelector('.pl');
    if(o)o.style.width=(100*ok/n)+'%';if(w)w.style.width=(100*wk/n)+'%';if(p)p.textContent=ok+'/'+n+' secure'+(wk?' · '+wk+' to revisit':'');});
  const ov=document.getElementById('overall');if(ov){const all=(ov.dataset.qids||'').split(',').filter(Boolean);const ok=all.filter(i=>prog[i]===2).length,wk=all.filter(i=>prog[i]===1).length;ov.querySelector('.stat').textContent=Math.round(100*ok/all.length)+'%';ov.querySelector('.detail').textContent=ok+' secure, '+wk+' to revisit, '+(all.length-ok-wk)+' not attempted of '+all.length+' questions.';}
}
window.TM.paint=paint;
document.addEventListener('click',e=>{const b=e.target.closest('.st button[data-s]');if(!b)return;const q=b.closest('.q');const s=+b.dataset.s;const cur=prog[q.dataset.qid]||0;window.TM.setProg(q.dataset.qid,(s===cur)?0:s);paint();if(window.TM.onFilter)window.TM.onFilter();});
const rs=document.getElementById('resetProg');if(rs)rs.onclick=()=>{if(confirm('Clear all saved progress, attempts and scores on this browser?')){prog={};att={};SV('tmua.progress',prog);SV('tmua.attempts',att);SV('tmua.srs',{});SV('tmua.scores',{});paint();location.reload();}};
/* ---- spaced repetition: secure questions return after 1, 3, 7, 14, 30 days ---- */
const IVL=[1,3,7,14,30];let srs=LS('tmua.srs')||{};
window.TM.srs=()=>srs;window.TM.isDue=id=>{const r=srs[id];return !r||!r.due||r.due<=Date.now();};
window.TM.schedule=(id,s)=>{if(s===2){const prev=srs[id]&&srs[id].ivl||0;const i=IVL[Math.min(IVL.indexOf(prev)+1,IVL.length-1)]||1;srs[id]={ivl:i,due:Date.now()+i*86400000};}else delete srs[id];SV('tmua.srs',srs);};
/* ---- multiple-choice interaction (instant feedback unless the container has data-nofb) ---- */
window.TM.answer=function(q,letter){
  if(q.classList.contains('done'))return;
  const ans=q.dataset.ans;const li=q.querySelector('ol.opts li[data-l="'+letter+'"]');
  const nofb=q.closest('[data-nofb]');
  if(nofb){q.querySelectorAll('ol.opts li').forEach(x=>x.classList.remove('pick'));li.classList.add('pick');q.dataset.pick=letter;if(window.TM.onPick)window.TM.onPick(q,letter);return;}
  q.classList.add('done');const right=letter===ans;
  q.querySelectorAll('ol.opts li').forEach(x=>{if(x.dataset.l===ans)x.classList.add('right');else if(x.dataset.l===letter)x.classList.add('wrong');});
  const fb=q.querySelector('.fb');if(fb){fb.textContent=right?'✓ Correct — '+ans:'✗ Not quite — the answer is '+ans;fb.className='fb '+(right?'ok':'bad');}
  const sol=q.querySelector('details.sol');if(sol&&!right)sol.open=true;
  window.TM.record(q.dataset.qid,right);
  if(!prog[q.dataset.qid]||!right)window.TM.setProg(q.dataset.qid,right?2:1);
  paint();if(window.TM.onFilter)window.TM.onFilter();if(window.TM.onAnswer)window.TM.onAnswer(q,right);
};
document.addEventListener('click',e=>{const li=e.target.closest('ol.opts li');if(!li)return;const q=li.closest('.q');if(!q)return;window.TM.answer(q,li.dataset.l);});
document.addEventListener('keydown',e=>{if(e.target&&e.target.matches&&e.target.matches('input,textarea,select'))return;const k=e.key.toUpperCase();if(!'ABCDEFGH'.includes(k)||k.length!==1)return;const q=window.TM.focusQ?window.TM.focusQ():null;if(q&&q.querySelector('ol.opts li[data-l="'+k+'"]'))window.TM.answer(q,k);});
/* ---- reveal all solutions / print ---- */
document.querySelectorAll('[data-showsol]').forEach(b=>b.onclick=()=>document.querySelectorAll('details.sol').forEach(d=>d.open=true));
document.querySelectorAll('[data-print]').forEach(b=>b.onclick=()=>{document.body.classList.toggle('print-sol',b.dataset.print==='sol');window.print();});
/* ---- copy link ---- */
document.addEventListener('click',e=>{const b=e.target.closest('button.lnk');if(!b)return;const id=b.closest('.q').id;const u=location.href.split('#')[0]+'#'+id;(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>{b.textContent='✓';setTimeout(()=>b.textContent='\u{1F517}',1200)},()=>prompt('Link:',u));});
/* ---- back to top ---- */
const tt=document.getElementById('totop');if(tt){window.addEventListener('scroll',()=>tt.classList.toggle('show',window.scrollY>600));tt.onclick=()=>window.scrollTo({top:0,behavior:'smooth'});}
paint();
/* ---- filter bar (topic pages) ---- */
const fb=document.getElementById('filterbar');
if(fb){const qs=[...document.querySelectorAll('.q[data-qid]')];const kw=fb.querySelector('input[type=search]');const chips=[...fb.querySelectorAll('.chip')];const cnt=fb.querySelector('.cnt');
  const st={paper:'',diff:'',type:'',status:''};
  chips.forEach(c=>c.onclick=()=>{const g=c.dataset.g;const on=c.classList.contains('on');chips.filter(x=>x.dataset.g===g).forEach(x=>x.classList.remove('on'));if(!on)c.classList.add('on');st[g]=on?'':c.dataset.v;apply();});
  if(kw)kw.oninput=apply;
  function apply(){const k=(kw?kw.value:'').trim().toLowerCase();let n=0;qs.forEach(q=>{let ok=true;if(k&&!q.textContent.toLowerCase().includes(k))ok=false;
    if(st.paper&&q.dataset.paper!==st.paper)ok=false;if(st.diff&&q.dataset.diff!==st.diff)ok=false;if(st.type&&!(q.dataset.tags||'').split(',').includes(st.type))ok=false;
    if(st.status){const s=prog[q.dataset.qid]||0;if(st.status==='0'&&s!==0)ok=false;if(st.status==='1'&&s!==1)ok=false;if(st.status==='2'&&s!==2)ok=false;}
    q.classList.toggle('hide',!ok);if(ok)n++;});if(cnt)cnt.textContent=n+' of '+qs.length+' shown';}
  window.TM.onFilter=apply;apply();}
/* ---- countdown timer helper: TM.timer(key, seconds, displayEl, onEnd) ---- */
window.TM.timer=function(key,total,el,onEnd){
  let s=LS(key)||{left:total,running:false,at:0};
  function left(){return s.running?Math.max(0,s.left-Math.floor((Date.now()-s.at)/1000)):s.left;}
  function fmt(t){const m=Math.floor(t/60),ss=t%60;return (m<10?'0':'')+m+':'+(ss<10?'0':'')+ss;}
  function draw(){const l=left();el.textContent=fmt(l);el.classList.toggle('low',l<300);if(l<=0&&s.running){s.running=false;s.left=0;SV(key,s);if(onEnd)onEnd();}}
  const t={start(){if(!s.running){s.running=true;s.at=Date.now();SV(key,s);}},pause(){if(s.running){s.left=left();s.running=false;SV(key,s);}},reset(){s={left:total,running:false,at:0};SV(key,s);draw();},
    used(){return total-left();},running(){return s.running;},draw};
  setInterval(draw,500);draw();return t;};
})();
"""

NAV = [("index.html", "Home"), ("topics.html", "Topics"), ("notes.html", "Notes"), ("papers.html", "Mock papers"), ("official.html", "Past papers"),
       ("practice.html", "Practice"), ("planner.html", "Planner")]


def esc(s):
    return html.escape(str(s), quote=True)


def rel(depth):
    return "../" * depth


def page(title, body, depth=0, active="", hero="", extra_head="", extra_js="", desc=""):
    r = rel(depth)
    nav = "".join(f'<a href="{r}{h}" class="{"on" if h == active else ""}">{t}</a>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} - TMUA Practice</title><meta name="description" content="{esc(desc or 'TMUA practice: questions by topic, mock papers, past papers and revision notes written to the TMUA specification.')}">
{KATEX}<style>{CSS}</style>{extra_head}</head>
<body><header class="top"><div class="wrap"><a class="brand" href="{r}index.html"><span class="sig">&Sigma;</span> TMUA Practice</a>
<nav>{nav}<a href="{r}search.html" title="Search">&#128269;</a><button class="icon-btn" id="themeBtn">&#9790; Dark</button></nav></div></header>
{hero}
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap">Questions, notes and mock papers written to the UAT-UK <a href="{r}official/TMUA-Specification.pdf">TMUA Content Specification</a> (October 2026 / January 2027). Official past papers &copy; Cambridge University Press &amp; Assessment / UAT-UK, reproduced for personal revision. This site is not affiliated with UAT-UK. All progress is stored only in this browser.</div></footer>
<button id="totop" title="Back to top">&uarr;</button>
<script>{JS}</script>{extra_js}</body></html>"""


def hero(title, blurb, crumbs=None, cls="", pills=(), depth=0, extra=""):
    r = rel(depth)
    c = ""
    if crumbs:
        c = '<div class="crumbs">' + "<span>&rsaquo;</span>".join(f'<a href="{r}{h}">{esc(t)}</a>' if h else esc(t) for h, t in crumbs) + "</div>"
    p = "".join(f'<span class="pill">{x}</span>' for x in pills)
    return f'<section class="hero {cls}"><div class="wrap">{c}<h1>{title}</h1><p>{blurb}</p>{p}{extra}</div></section>'


# ------------------------------------------------------------------ questions ----
def question_html(q, number=None, depth=0, show_status=True, link_topic=True):
    r = rel(depth)
    t = IDX[q.topic]
    stars = "★" * q.diff + "☆" * (3 - q.diff)
    tags = ",".join(("roman",) if "roman" in q.tags else ()) + ("," if q.tags else "") + ",".join(x for x in q.tags if x != "roman")
    tags = ",".join(sorted({x for x in tags.split(",") if x}))
    tname = f'<a href="{r}topic/{q.topic}.html">{esc(t["name"])}</a>' if link_topic else esc(t["name"])
    st = ('<div class="st"><button class="lnk" title="Copy link">&#128279;</button><button data-s="1">Needs work</button><button data-s="2">Secure</button></div>' if show_status else "")
    opts = "".join(f'<li data-l="{L}"><span class="lt">{L}</span><span>{mathtex.to_html(o).replace("<p>", "").replace("</p>", "")}</span></li>' for L, o in zip(q.letters, q.options))
    num = f"{number}" if number is not None else q.id
    meta = f'{tname} &middot; spec {esc(q.spec)} &middot; Paper {q.paper} style &middot; <span class="d" title="difficulty">{stars}</span>'
    return f"""<div class="q" id="{q.id}" data-qid="{q.id}" data-topic="{q.topic}" data-ans="{q.answer}" data-paper="{q.paper}" data-diff="{q.diff}" data-tags="{tags}">
<div class="qh"><span class="num">{num}</span><span class="meta">{meta}</span>{st}</div>
<div class="qt">{mathtex.to_html(q.text)}</div>
<ol class="opts">{opts}</ol><div class="fb"></div>
<details class="sol"><summary>Worked solution</summary><div class="sb">{mathtex.to_html(q.solution)}</div><div class="src">Answer <b>{q.answer}</b> &middot; {esc(t['name'])} ({esc(q.spec)}) &middot; question {q.id}</div></details>
</div>"""


def qdata_js(questions):
    data = []
    for q in questions:
        t = IDX[q.topic]
        data.append({"id": q.id, "topic": q.topic, "tname": t["name"], "group": t["group_slug"], "spec": q.spec, "paper": q.paper, "diff": q.diff,
                     "tags": list(q.tags), "text": mathtex.to_html(q.text), "opts": [mathtex.to_html(o).replace("<p>", "").replace("</p>", "") for o in q.options],
                     "ans": q.answer, "sol": mathtex.to_html(q.solution),
                     "search": (mathtex.to_text(q.text) + " " + " ".join(mathtex.to_text(o) for o in q.options) + " " + mathtex.to_text(q.solution) + " " + t["name"] + " " + q.spec).lower()})
    topics = {s: {"name": IDX[s]["name"], "group": IDX[s]["group_slug"], "spec": IDX[s]["spec"]} for s in IDX}
    return ("window.QDATA=" + json.dumps(data, ensure_ascii=False) + ";\nwindow.TOPICS=" + json.dumps(topics, ensure_ascii=False) +
            ";\nwindow.GRADES=" + json.dumps(GRADES) + ";\nwindow.DEFAULT_GRADE_SERIES=" + json.dumps(DEFAULT_GRADE_SERIES) + ";\n")


# ---------------------------------------------------------------- real papers ----
def real_by_topic():
    out = {}
    for series, papers in OFFICIAL_INDEX.items():
        for pno, qs in papers.items():
            for n, (slug, desc) in qs.items():
                out.setdefault(slug, []).append((series, pno, n, desc))
    for v in out.values():
        v.sort(key=lambda x: (-_series_year(x[0]), x[1], x[2]))
    return out


def _series_year(s):
    for sid, label, year, note in SERIES:
        if sid == s:
            return year
    return 0


def series_label(s):
    for sid, label, year, note in SERIES:
        if sid == s:
            return label
    return s


def official_counts():
    c = {}
    for slug, lst in real_by_topic().items():
        c[slug] = len(lst)
    return c


def real_row_html(series, pno, n, desc, depth=0, with_series=True):
    r = rel(depth)
    ser = f'<span class="ser">{esc(series_label(series))} &middot; Paper {pno}</span>' if with_series else ""
    return (f'<div class="row">{ser}<span class="qn">Question {n}</span><span class="t">{esc(desc)}</span>'
            f'<a href="{r}official/TMUA-{series}-P{pno}.pdf#page={n + 2}" target="_blank">question paper</a>'
            f'<a href="{r}real/{series}-P{pno}.html?q={n}">sit online</a></div>')


# --------------------------------------------------------------------- pages ----
def index_page(by_topic, counts, generated):
    ids_all = ",".join(q.id for qs in by_topic.values() for q in qs)
    groups = ""
    for g in GROUPS:
        cards = ""
        for t in g["topics"]:
            qs = by_topic.get(t["slug"], [])
            ids = ",".join(q.id for q in qs)
            cards += (f'<a class="topic-card" href="topic/{t["slug"]}.html"><div class="icon {g["slug"]}">{esc(t["spec"].split(",")[0].split("-")[0])}</div><div>'
                      f'<h3>{esc(t["name"])}</h3><div class="meta">{len(qs)} questions &middot; {counts["real"].get(t["slug"], 0)} real past questions</div>'
                      f'<div class="prog" data-qids="{ids}"><div class="bar"><div class="ok"></div><div class="wk"></div></div><span class="pl"></span></div></div></a>')
        groups += f'<h2 class="sec">{esc(g["name"])} <small style="font-family:Source Sans 3;font-size:.8rem;font-weight:400;color:var(--stone)">{esc(g["paper"])}</small></h2><div class="grid2">{cards}</div>'
    h = hero("Test of Mathematics for University Admission",
             f"{counts['questions']} original multiple-choice questions written to the TMUA specification, {counts['papers']} generated mock papers in the real format, "
             f"every official past paper (2017-2023, specimen and practice) with online marking and grade conversion, revision notes for all {counts['topics']} topics, and drills for the skills you must do without a calculator.",
             pills=["2 papers &times; 20 questions", "75 minutes each", "No calculator, no formula booklet", "No negative marking"])
    body = f"""
<div class="grid4">
 <div class="card" id="overall" data-qids="{ids_all}"><div class="stat">0%</div><h3>Your progress</h3><p class="detail"></p><button class="btn ghost" id="resetProg">Reset progress</button></div>
 <div class="card"><div class="stat">{counts['questions']}</div><h3>Questions by topic</h3><p>Instant marking, worked solutions, PDF sets.</p><a class="btn" href="topics.html">Browse topics</a></div>
 <div class="card"><div class="stat">{counts['papers']}</div><h3>Mock papers</h3><p>Timed 75-minute papers, auto-marked with a grade estimate.</p><a class="btn" href="papers.html">Sit a paper</a></div>
 <div class="card"><div class="stat">{counts['official']}</div><h3>Official papers</h3><p>Every published paper, sit it online against the real key.</p><a class="btn" href="official.html">Past papers</a></div>
</div>
<h2 class="sec">The two papers</h2>
<div class="grid2">
 <div class="card"><div class="paper-head"><span class="tag p1">Paper 1</span><span class="assessed">Applications of Mathematical Knowledge &middot; 75 min &middot; 20 questions</span></div>
 <p>{esc(TEST['papers'][1]['blurb'])} Draws on Section 1 of the specification: AS-level pure maths (Part 1) and Higher GCSE (Part 2).</p><div class="links"><a href="papers.html#p1">Paper 1 mocks</a><a href="quickfire.html?paper=1">Quick-fire Paper 1</a></div></div>
 <div class="card"><div class="paper-head"><span class="tag p2">Paper 2</span><span class="assessed">Mathematical Reasoning &middot; 75 min &middot; 20 questions</span></div>
 <p>{esc(TEST['papers'][2]['blurb'])} Section 2 adds the logic of arguments, proof and spotting errors in proofs, and the maths questions are posed as statements to test.</p><div class="links"><a href="papers.html#p2">Paper 2 mocks</a><a href="quickfire.html?paper=2">Quick-fire Paper 2</a><a href="technique.html">Paper 2 language guide</a></div></div>
</div>
{groups}
<h2 class="sec">Practice modes</h2>
<div class="grid3">
 <div class="card"><h3>Quick-fire</h3><p>One random question at a time, keyboard answers, spaced repetition and a per-question timer.</p><a class="btn ghost" href="quickfire.html">Start</a></div>
 <div class="card"><h3>Formula recall</h3><p>{counts['facts']} flashcards - everything you must know without a formula booklet.</p><a class="btn ghost" href="facts.html">Drill</a></div>
 <div class="card"><h3>Skill drills</h3><p>Fresh numbers every time: indices, logs, quadratics, series, calculus, logic.</p><a class="btn ghost" href="drills.html">Practise</a></div>
</div>
<h2 class="sec">Also on this site</h2>
<div class="links"><a href="notes.html">Revision notes</a><a href="pastq.html">Real questions by topic</a><a href="grades.html">Grade calculator &amp; conversion tables</a><a href="technique.html">Exam technique</a><a href="planner.html">Revision planner</a><a href="search.html">Search every question</a><a href="official/TMUA-Specification.pdf">The specification (PDF)</a></div>
"""
    return page("Home", body, hero=h, active="index.html")


def topics_page(by_topic, counts):
    body = ""
    for g in GROUPS:
        rows = ""
        for t in g["topics"]:
            qs = by_topic.get(t["slug"], [])
            ids = ",".join(q.id for q in qs)
            rows += (f'<tr><td><a href="topic/{t["slug"]}.html"><b>{esc(t["name"])}</b></a><br><span style="font-size:.85rem;color:var(--stone)">{esc(t["desc"])}</span></td>'
                     f'<td>{esc(t["spec"])}</td><td>{len(qs)}</td><td>{counts["real"].get(t["slug"], 0)}</td>'
                     f'<td><div class="prog" data-qids="{ids}" style="margin:0"><div class="bar"><div class="ok"></div><div class="wk"></div></div></div><span class="pl" style="font-size:.8rem;color:var(--stone)"></span></td>'
                     f'<td class="links"><a href="notes/{t["slug"]}.html">notes</a><a href="quickfire.html?topic={t["slug"]}">quick-fire</a></td></tr>')
        body += f'<h2 class="sec">{esc(g["name"])}</h2><table class="list"><tr><th>Topic</th><th>Spec</th><th>Bank</th><th>Real</th><th>Progress</th><th></th></tr>{rows}</table>'
    h = hero("Topics", "Every topic in the TMUA Content Specification, with the bank questions, revision notes and the real past-paper questions on it.", pills=[f"{counts['topics']} topics", f"{counts['questions']} questions"])
    return page("Topics", body, hero=h, active="topics.html")


def topic_page(slug, questions, sets, real):
    t = IDX[slug]
    g = t["group_slug"]
    ids = ",".join(q.id for q in questions)
    cls = {"part1": "p1", "part2": "", "section2": "p2"}[g]
    nreal = len(real)
    h = hero(esc(t["name"]), esc(t["desc"]), crumbs=[("index.html", "Home"), ("topics.html", "Topics"), (None, t["name"])], cls=cls, depth=1,
             pills=[f"Spec {esc(t['spec'])}", esc(t["group"]), f"{len(questions)} questions", f"{nreal} real past questions"],
             extra=f'<div class="prog" data-qids="{ids}"><div class="bar"><div class="ok"></div><div class="wk"></div></div><span class="pl"></span></div>')
    pdfs = "".join(f'<a href="../pdf/topic/{slug}-set{k}-QP.pdf">Set {k} questions (PDF)</a><a href="../pdf/topic/{slug}-set{k}-SOL.pdf">Set {k} solutions</a>' for k in range(1, len(sets) + 1))
    types = [("roman", "Statements I/II/III"), ("fixed", "Logic / proof format")]
    chips = ''.join(f'<button class="chip" data-g="paper" data-v="{p}">Paper {p} style</button>' for p in (1, 2))
    chips += ''.join(f'<button class="chip" data-g="diff" data-v="{d}">{"★" * d}</button>' for d in (1, 2, 3))
    chips += ''.join(f'<button class="chip" data-g="type" data-v="{v}">{n}</button>' for v, n in types)
    chips += ''.join(f'<button class="chip" data-g="status" data-v="{v}">{n}</button>' for v, n in (("0", "Not tried"), ("1", "Needs work"), ("2", "Secure")))
    qhtml = "".join(question_html(q, number=i, depth=1) for i, q in enumerate(questions, 1))
    real_html = "".join(real_row_html(*x, depth=1) for x in real) or '<p class="empty">No real past questions indexed for this topic.</p>'
    body = f"""
<div class="links" style="margin:6px 0 14px"><a href="../notes/{slug}.html">&#128214; Revision notes</a><a href="../quickfire.html?topic={slug}">&#9889; Quick-fire this topic</a><a href="../facts.html?topic={slug}">Formula cards</a>{pdfs}</div>
<div class="filterbar" id="filterbar"><input type="search" placeholder="Filter by keyword"> {chips}<button class="chip" data-showsol>Show all solutions</button><button class="chip" data-print="qp">Print</button><button class="chip" data-print="sol">Print + solutions</button><span class="cnt"></span></div>
<p class="note">Click an option to answer. A correct first attempt marks the question <b>secure</b>; a wrong one marks it <b>needs work</b> and opens the worked solution. Keys <kbd>A</kbd>-<kbd>H</kbd> answer the question nearest the top of the screen.</p>
{qhtml}
<h2 class="sec">How this topic has been examined</h2>
<p>Real TMUA questions on {esc(t['name'])}, newest first. Links open the official paper at the question and the online marking page.</p>
<div class="real">{real_html}</div>
"""
    js = "<script>window.TM.focusQ=function(){const qs=[...document.querySelectorAll('.q:not(.hide):not(.done)')];return qs.find(q=>q.getBoundingClientRect().bottom>80)||null;};</script>"
    return page(t["name"], body, depth=1, active="topics.html", hero=h, extra_js=js, desc=f"TMUA {t['name']} practice questions ({t['spec']}) with worked solutions.")


def notes_index_page(by_topic):
    body = ""
    for g in GROUPS:
        cards = "".join(f'<a class="ncard" href="notes/{t["slug"]}.html"><b>{esc(t["name"])}</b><span>{esc(t["spec"])} &middot; {len(by_topic.get(t["slug"], []))} questions</span></a>' for t in g["topics"] if t["slug"] in NOTES_ALL)
        body += f'<h2 class="sec">{esc(g["name"])}</h2><div class="notes-grid">{cards}</div>'
    h = hero("Revision notes", "Concise notes for every topic in the specification: what the spec asks for, the formulas you must recall (there is no formula booklet), the standard techniques, the classic traps, and the real past questions on each topic.", pills=[f"{len(NOTES_ALL)} topics"])
    return page("Revision notes", body, hero=h, active="notes.html")


def notes_page(slug, n, questions, real):
    t = IDX[slug]
    cls = {"part1": "p1", "part2": "", "section2": "p2"}[t["group_slug"]]
    secs = ""
    toc = ""
    for i, s in enumerate(n["sections"], 1):
        secs += f'<h2 id="s{i}">{esc(s["h"])}</h2>{mathtex.to_html(s["body"])}'
        toc += f'<a href="#s{i}">{esc(s["h"])}</a>'
    key = "".join(f"<li>{mathtex.to_html(k).replace('<p>', '').replace('</p>', '')}</li>" for k in n["key"])
    traps = "".join(f"<li>{mathtex.to_html(k).replace('<p>', '').replace('</p>', '')}</li>" for k in n["traps"])
    worked = "".join(f'<p><b>Q.</b> {mathtex.to_html(w["q"]).replace("<p>", "").replace("</p>", "")}</p><p><b>A.</b> {mathtex.to_html(w["a"]).replace("<p>", "").replace("</p>", "")}</p>' for w in n["worked"])
    real_html = "".join(real_row_html(*x, depth=1) for x in real[:12]) or '<p class="empty">No real past questions indexed for this topic.</p>'
    more = f'<p><a href="../pastq.html#{slug}">All {len(real)} real questions on this topic &rarr;</a></p>' if len(real) > 12 else ""
    h = hero(esc(t["name"]), f"Revision notes &middot; spec {esc(t['spec'])}", crumbs=[("index.html", "Home"), ("notes.html", "Notes"), (None, t["name"])], cls=cls, depth=1, pills=[esc(t["group"])])
    body = f"""<div class="notes">
<div class="links" style="margin:6px 0 14px"><a href="../topic/{slug}.html">&#9998; {len(questions)} practice questions</a><a href="../quickfire.html?topic={slug}">&#9889; Quick-fire</a><a href="../facts.html?topic={slug}">Formula cards</a></div>
<div class="summary">{mathtex.to_html(n["summary"])}</div>
<div class="toc"><b>Contents:</b> {toc}<a href="#key">Must-know</a><a href="#traps">Traps</a><a href="#exam">Real questions</a></div>
{secs}
<div class="nums" id="key"><h3>Must-know (no formula booklet)</h3><ul>{key}</ul></div>
<div class="traps" id="traps"><h3>Classic traps</h3><ul>{traps}</ul></div>
<div class="worked"><h3 style="margin:0 0 6px;font-size:1.05rem">Worked example</h3>{worked}</div>
<div class="examh" id="exam"><h3>How it has been examined</h3><div class="real">{real_html}</div>{more}</div>
</div>"""
    return page(f"{t['name']} notes", body, depth=1, active="notes.html", hero=h, desc=f"TMUA revision notes: {t['name']} ({t['spec']}).")


def papers_page(generated):
    def table(pno):
        rows = ""
        for g in generated:
            if g["paper"] != pno:
                continue
            f = g["file"]
            topics = sorted({IDX[q.topic]["name"] for q in g["questions"]})
            rows += (f'<tr><td><b>Set {g["set"]:02d}</b></td><td style="font-size:.85rem;color:var(--stone)">{esc(", ".join(topics[:8]))}{"..." if len(topics) > 8 else ""}</td>'
                     f'<td class="links"><a href="paper/{f}.html">Sit online</a><a href="pdf/papers/{f}-QP.pdf">Question paper (PDF)</a><a href="pdf/papers/{f}-SOL.pdf">Solutions (PDF)</a></td>'
                     f'<td class="score" data-file="{f}">-</td></tr>')
        return f'<table class="list"><tr><th>Paper</th><th>Topics covered</th><th></th><th>Your score</th></tr>{rows}</table>'
    h = hero("Mock papers", "Generated papers in the real format: 20 questions, 75 minutes, answer grid, no calculator. Sit them online with a countdown and automatic marking (score, grade estimate from the published conversion, and a breakdown by topic), or print the PDFs and mark yourself from the solutions booklet.",
             pills=[f"{len(generated)} papers", "Auto-marked", "Grade estimate"])
    body = f"""<p class="note">Questions rotate through the whole bank so every set is different; harder questions come later in each paper, as in the real test. The grade estimate uses the {DEFAULT_GRADE_SERIES} conversion table - real boundaries move a little every year (see <a href="grades.html">all conversion tables</a>).</p>
<h2 class="sec" id="p1"><span class="tag p1">Paper 1</span> Applications of Mathematical Knowledge</h2>{table(1)}
<h2 class="sec" id="p2"><span class="tag p2">Paper 2</span> Mathematical Reasoning</h2>{table(2)}"""
    js = """<script>(function(){const sc=window.TM.LS('tmua.scores')||{};document.querySelectorAll('td.score').forEach(td=>{const s=sc[td.dataset.file];if(s)td.innerHTML='<b>'+s.score+'/20</b>'+(s.grade?' &middot; grade '+s.grade:'')+'<br><span style="font-size:.8rem;color:var(--stone)">'+new Date(s.date).toLocaleDateString()+'</span>';});})();</script>"""
    return page("Mock papers", body, hero=h, active="papers.html", extra_js=js)


def paper_online_page(g):
    pno, n, f = g["paper"], g["set"], g["file"]
    qs = g["questions"]
    ids = ",".join(q.id for q in qs)
    qhtml = "".join(question_html(q, number=i, depth=1, show_status=False) for i, q in enumerate(qs, 1))
    grid = "".join(f'<div class="cell" data-n="{i}"><b>{i}</b><span class="ls">' + "".join(f'<button data-l="{L}">{L}</button>' for L in q.letters) + '</span><span class="k"></span></div>' for i, q in enumerate(qs, 1))
    h = hero(f"Paper {pno} &middot; Set {n:02d}", f"{TEST['papers'][pno]['title']}. 20 questions, 75 minutes. Answer on the grid or click the options; nothing is marked until you press <b>Submit</b>.",
             crumbs=[("index.html", "Home"), ("papers.html", "Mock papers"), (None, f"Paper {pno} Set {n:02d}")], cls=f"p{pno}", depth=1, pills=["75 minutes", "20 marks", "No calculator"])
    body = f"""
<div class="tools" id="tools"><span class="time" id="clock">75:00</span><button class="primary" id="startBtn">Start</button><button id="pauseBtn">Pause</button><button id="resetBtn">Reset paper</button>
<span class="score" id="scoreBox"></span><button class="primary" id="submitBtn" style="margin-left:auto">Submit answers</button><a class="btn ghost" href="../pdf/papers/{f}-QP.pdf" style="padding:6px 12px;font-size:.88rem">PDF</a></div>
<div class="result" id="result" style="display:none"></div>
<h3>Answer grid</h3><div class="agrid" id="agrid">{grid}</div>
<div id="paper" data-nofb data-qids="{ids}">{qhtml}</div>
<div class="note" style="margin-top:18px">After submitting, every question shows the correct answer and its worked solution; wrong answers are added to your <i>needs work</i> list and correct ones to <i>secure</i>.</div>
"""
    js = f"""<script>(function(){{
const FILE='{f}',PNO={pno};const qs=[...document.querySelectorAll('#paper .q')];const cells=[...document.querySelectorAll('#agrid .cell')];
const key='tmua.paper.'+FILE;let state=window.TM.LS(key)||{{picks:{{}},done:false}};
function save(){{window.TM.SV(key,state);}}
function pick(n,L){{if(state.done)return;state.picks[n]=L;save();const c=cells[n-1];c.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.l===L));const q=qs[n-1];q.querySelectorAll('ol.opts li').forEach(x=>x.classList.toggle('pick',x.dataset.l===L));}}
cells.forEach(c=>c.querySelectorAll('button').forEach(b=>b.onclick=()=>pick(+c.dataset.n,b.dataset.l)));
window.TM.onPick=(q,L)=>pick(qs.indexOf(q)+1,L);
Object.entries(state.picks).forEach(([n,L])=>pick(+n,L));
const clock=document.getElementById('clock');const timer=window.TM.timer(key+'.t',{EXAM_SECONDS},clock,()=>{{alert('Time is up - your answers will be submitted.');submit();}});
document.getElementById('startBtn').onclick=()=>timer.start();document.getElementById('pauseBtn').onclick=()=>timer.pause();
document.getElementById('resetBtn').onclick=()=>{{if(!confirm('Clear your answers and restart the timer for this paper?'))return;state={{picks:{{}},done:false}};save();timer.reset();location.reload();}};
function grade(raw){{const G=window.GRADES&&window.GRADES[window.DEFAULT_GRADE_SERIES];if(!G)return null;const t=G[PNO===1?'p1':'p2'];return t?t[Math.max(0,Math.min(20,raw))]:null;}}
function submit(){{if(state.done)return;const blanks=qs.filter((q,i)=>!state.picks[i+1]).length;if(blanks&&!confirm(blanks+' question(s) unanswered. Submit anyway? (There is no penalty for guessing!)'))return;
  state.done=true;save();timer.pause();let score=0;const byTopic={{}};
  qs.forEach((q,i)=>{{const L=state.picks[i+1];const ans=q.dataset.ans;const right=L===ans;if(right)score++;const c=cells[i];c.classList.add(L?(right?'right':'wrong'):'blank');c.querySelector('.k').textContent='key '+ans;
    q.classList.add('done');q.querySelectorAll('ol.opts li').forEach(x=>{{if(x.dataset.l===ans)x.classList.add('right');else if(x.dataset.l===L)x.classList.add('wrong');}});
    const fb=q.querySelector('.fb');fb.textContent=right?'\\u2713 Correct':(L?'\\u2717 You chose '+L+'; the answer is '+ans:'\\u2013 Not answered; the answer is '+ans);fb.className='fb '+(right?'ok':'bad');
    const t=q.dataset.topic;byTopic[t]=byTopic[t]||{{n:0,c:0}};byTopic[t].n++;if(right)byTopic[t].c++;
    window.TM.record(q.dataset.qid,right);window.TM.setProg(q.dataset.qid,right?2:1);}});
  const g=grade(score);const sc=window.TM.LS('tmua.scores')||{{}};sc[FILE]={{score,grade:g,date:Date.now(),paper:PNO,secs:timer.used()}};window.TM.SV('tmua.scores',sc);
  const rows=Object.entries(byTopic).sort((a,b)=>(a[1].c/a[1].n)-(b[1].c/b[1].n)).map(([t,v])=>'<tr><td><a href="../topic/'+t+'.html">'+window.TOPICS[t].name+'</a></td><td>'+v.c+'/'+v.n+'</td></tr>').join('');
  const mins=Math.round(timer.used()/60);
  document.getElementById('result').style.display='block';document.getElementById('result').innerHTML='<div style="display:flex;gap:28px;flex-wrap:wrap;align-items:center"><div><div class="big">'+score+'/20</div><div style="color:var(--stone)">raw score</div></div>'+(g!==null?'<div><div class="grade">'+g.toFixed(1)+'</div><div style="color:var(--stone)">estimated grade ('+window.DEFAULT_GRADE_SERIES+' table)</div></div>':'')+'<div><div class="grade" style="color:var(--teal)">'+mins+' min</div><div style="color:var(--stone)">time used</div></div></div><h3 style="margin:14px 0 6px">By topic (weakest first)</h3><table class="list">'+rows+'</table><p><a href="../planner.html">Open the planner</a> &middot; <a href="../grades.html">Grade tables</a></p>';
  document.getElementById('scoreBox').innerHTML='<b>'+score+'</b>/20';document.querySelectorAll('details.sol').forEach(d=>d.open=false);document.getElementById('result').scrollIntoView({{behavior:'smooth'}});window.TM.paint();}}
document.getElementById('submitBtn').onclick=submit;
if(state.done){{state.done=false;submit();}}
}})();</script>"""
    return page(f"Paper {pno} Set {n:02d}", body, depth=1, active="papers.html", hero=h, extra_head='<script src="../qdata.js"></script>', extra_js=js)


def official_page(files):
    by = {}
    for f in files:
        by.setdefault(f["series"], {})[f["kind"]] = f["name"]
    rows = ""
    for sid, label, year, note in sorted(SERIES, key=lambda s: -s[2]):
        d = by.get(sid, {})
        links = ""
        for pno in (1, 2):
            nm = d.get(f"P{pno}")
            if nm:
                links += f'<a href="official/{nm}">Paper {pno} (PDF)</a><a href="real/{sid}-P{pno}.html"><b>Sit Paper {pno} online</b></a>'
        if d.get("KEY"):
            links += f'<a href="official/{d["KEY"]}">Answer key (PDF)</a>'
        conv = "yes" if sid in GRADES else "no"
        rows += f'<tr><td><b>{esc(label)}</b><br><span style="font-size:.85rem;color:var(--stone)">{esc(note)}</span></td><td class="links">{links}</td><td>{conv}</td><td class="score" data-series="{sid}">-</td></tr>'
    h = hero("Official past papers", "Every TMUA paper published by Cambridge Assessment Admissions Testing / UAT-UK, with the official answer keys and score conversions. Sit any paper online: the PDF is shown alongside an answer grid and a 75-minute clock, and your answers are marked against the real key with the grade conversion and a topic breakdown.",
             pills=[f"{len(SERIES)} series", "Answer keys", "Grade conversions"])
    body = f"""<table class="list"><tr><th>Series</th><th>Papers</th><th>Grade conversion</th><th>Your scores</th></tr>{rows}</table>
<p class="note">The specification says the test will be delivered in the same two-paper format from October 2026; the content specification was unchanged apart from presentation, so all of these papers remain valid practice. Every real question is also indexed by topic on the <a href="pastq.html">real questions by topic</a> page.</p>"""
    js = """<script>(function(){const sc=window.TM.LS('tmua.scores')||{};document.querySelectorAll('td.score').forEach(td=>{const out=[];for(const p of [1,2]){const s=sc['real-'+td.dataset.series+'-P'+p];if(s)out.push('P'+p+': <b>'+s.score+'/20</b>'+(s.grade?' ('+s.grade+')':''));}td.innerHTML=out.join('<br>')||'-';});})();</script>"""
    return page("Official past papers", body, hero=h, active="official.html", extra_js=js)


def real_paper_page(series, pno):
    key = KEYS[series][pno]
    idx = OFFICIAL_INDEX.get(series, {}).get(pno, {})
    grid = "".join(f'<div class="cell" data-n="{i}"><b>{i}</b><span class="ls">' + "".join(f'<button data-l="{L}">{L}</button>' for L in "ABCDEFGH") + '</span><span class="k"></span></div>' for i in range(1, 21))
    topics = {i: idx[i][0] for i in idx}
    descs = {i: idx[i][1] for i in idx}
    label = series_label(series)
    conv = "p1" if pno == 1 else "p2"
    has_conv = series in GRADES
    h = hero(f"{esc(label)} &middot; Paper {pno}", f"{TEST['papers'][pno]['title']}. The official paper is shown below; answer on the grid, then submit to mark against the published key" + (" and convert to a grade." if has_conv else "."),
             crumbs=[("index.html", "Home"), ("official.html", "Past papers"), (None, f"{label} Paper {pno}")], cls=f"p{pno}", depth=1, pills=["Official paper", "75 minutes", "Real answer key"])
    body = f"""
<div class="tools"><span class="time" id="clock">75:00</span><button class="primary" id="startBtn">Start</button><button id="pauseBtn">Pause</button><button id="resetBtn">Reset</button>
<span class="score" id="scoreBox"></span><button class="primary" id="submitBtn" style="margin-left:auto">Submit answers</button><a class="btn ghost" href="../official/TMUA-{series}-P{pno}.pdf" target="_blank" style="padding:6px 12px;font-size:.88rem">Open PDF</a></div>
<div class="result" id="result" style="display:none"></div>
<h3>Answer grid</h3><div class="agrid" id="agrid">{grid}</div>
<iframe class="pdfbox" id="pdf" src="../official/TMUA-{series}-P{pno}.pdf#page=3"></iframe>
<p class="note">If the PDF does not display in this browser, use <b>Open PDF</b> and keep this tab for the answer grid. Question $n$ is on page $n + 2$ of the PDF.</p>
"""
    js = f"""<script>(function(){{
const SER='{series}',PNO={pno},KEY='{key}';const TOP={json.dumps(topics)};const DESC={json.dumps(descs)};const HAS={'true' if has_conv else 'false'};
const cells=[...document.querySelectorAll('#agrid .cell')];const key='tmua.real.'+SER+'.'+PNO;let state=window.TM.LS(key)||{{picks:{{}},done:false}};
function save(){{window.TM.SV(key,state);}}
function pick(n,L){{if(state.done)return;state.picks[n]=L;save();cells[n-1].querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.l===L));}}
cells.forEach(c=>c.querySelectorAll('button').forEach(b=>b.onclick=()=>pick(+c.dataset.n,b.dataset.l)));
Object.entries(state.picks).forEach(([n,L])=>pick(+n,L));
const clock=document.getElementById('clock');const timer=window.TM.timer(key+'.t',{EXAM_SECONDS},clock,()=>{{alert('Time is up - your answers will be submitted.');submit();}});
document.getElementById('startBtn').onclick=()=>timer.start();document.getElementById('pauseBtn').onclick=()=>timer.pause();
document.getElementById('resetBtn').onclick=()=>{{if(!confirm('Clear your answers and restart the timer?'))return;state={{picks:{{}},done:false}};save();timer.reset();location.reload();}};
const qp=new URLSearchParams(location.search).get('q');if(qp){{document.getElementById('pdf').src='../official/TMUA-'+SER+'-P'+PNO+'.pdf#page='+(+qp+2);}}
function submit(){{if(state.done)return;const blanks=cells.filter((c,i)=>!state.picks[i+1]).length;if(blanks&&!confirm(blanks+' question(s) unanswered. Submit anyway?'))return;
  state.done=true;save();timer.pause();let score=0;const byTopic={{}};
  cells.forEach((c,i)=>{{const L=state.picks[i+1];const ans=KEY[i];const right=L===ans;if(right)score++;c.classList.add(L?(right?'right':'wrong'):'blank');c.querySelector('.k').textContent='key '+ans+(TOP[i+1]?' \\u00b7 '+window.TOPICS[TOP[i+1]].name:'');
    const t=TOP[i+1];if(t){{byTopic[t]=byTopic[t]||{{n:0,c:0,miss:[]}};byTopic[t].n++;if(right)byTopic[t].c++;else byTopic[t].miss.push(i+1);}}}});
  let g=null;if(HAS){{g=window.GRADES[SER][PNO===1?'p1':'p2'][score];}}
  const sc=window.TM.LS('tmua.scores')||{{}};sc['real-'+SER+'-P'+PNO]={{score,grade:g,date:Date.now(),paper:PNO,real:true,secs:timer.used()}};window.TM.SV('tmua.scores',sc);
  const rows=Object.entries(byTopic).sort((a,b)=>(a[1].c/a[1].n)-(b[1].c/b[1].n)).map(([t,v])=>'<tr><td><a href="../topic/'+t+'.html">'+window.TOPICS[t].name+'</a></td><td>'+v.c+'/'+v.n+'</td><td style="font-size:.85rem;color:var(--stone)">'+(v.miss.length?'missed Q'+v.miss.join(', Q')+' - <a href="../notes/'+t+'.html">notes</a> &middot; <a href="../quickfire.html?topic='+t+'">practise</a>':'')+'</td></tr>').join('');
  document.getElementById('result').style.display='block';document.getElementById('result').innerHTML='<div style="display:flex;gap:28px;flex-wrap:wrap;align-items:center"><div><div class="big">'+score+'/20</div><div style="color:var(--stone)">raw score</div></div>'+(g!==null?'<div><div class="grade">'+Number(g).toFixed(1)+'</div><div style="color:var(--stone)">official '+SER+' grade for this paper</div></div>':'<div style="color:var(--stone)">No conversion table was published for this series - see <a href="../grades.html">other years</a>.</div>')+'<div><div class="grade" style="color:var(--teal)">'+Math.round(timer.used()/60)+' min</div><div style="color:var(--stone)">time used</div></div></div><h3 style="margin:14px 0 6px">By topic (weakest first)</h3><table class="list">'+rows+'</table>';
  document.getElementById('scoreBox').innerHTML='<b>'+score+'</b>/20';document.getElementById('result').scrollIntoView({{behavior:'smooth'}});}}
document.getElementById('submitBtn').onclick=submit;if(state.done){{state.done=false;submit();}}
}})();</script>"""
    return page(f"{label} Paper {pno}", body, depth=1, active="official.html", hero=h, extra_head='<script src="../qdata.js"></script>', extra_js=js)


def pastq_page():
    rb = real_by_topic()
    secs = ""
    for g in GROUPS:
        for t in g["topics"]:
            lst = rb.get(t["slug"], [])
            if not lst:
                continue
            rows = "".join(real_row_html(*x) for x in lst)
            secs += f'<h2 class="sec" id="{t["slug"]}">{esc(t["name"])} <small style="font-family:Source Sans 3;font-size:.8rem;font-weight:400;color:var(--stone)">{len(lst)} questions</small></h2><div class="real">{rows}</div>'
    total = sum(len(v) for v in rb.values())
    jump = "".join(f'<a href="#{t["slug"]}">{esc(t["name"])} ({len(rb.get(t["slug"], []))})</a>' for g in GROUPS for t in g["topics"] if rb.get(t["slug"]))
    h = hero("Real questions by topic", f"All {total} questions from the published TMUA papers, indexed by specification topic. Use it to see what a topic really looks like in the exam, or to find every past question on your weakest area.", pills=[f"{total} questions", f"{len(SERIES)} series"])
    body = f'<div class="jump">{jump}</div>{secs}'
    return page("Real questions by topic", body, hero=h, active="official.html")


def practice_page(counts):
    h = hero("Practice modes", "Different ways to work the bank: random questions with spaced repetition, timed sprints, formula recall and fresh-number skill drills.")
    body = f"""
<div class="modecard"><div class="mi">&#9889;</div><div><h3>Quick-fire</h3><p>One random question at a time from the whole bank or a chosen paper, group or topic. Keyboard answers (A-H), a per-question stopwatch against the 3&frac34;-minute budget, and spaced repetition: secure questions come back after 1, 3, 7, 14 and 30 days.</p><div class="links"><a href="quickfire.html">Start</a><a href="quickfire.html?due=1">Due for review</a><a href="quickfire.html?weak=1">Needs-work only</a><a href="quickfire.html?paper=2">Paper 2 only</a></div></div></div>
<div class="modecard"><div class="mi">&#9201;</div><div><h3>Sprint</h3><p>Ten random questions against the clock - a compressed simulation of exam pace.</p><div class="links"><a href="quickfire.html?sprint=10">10-question sprint</a><a href="quickfire.html?sprint=20&paper=1">Full-length Paper 1 sprint</a></div></div></div>
<div class="modecard"><div class="mi">&#128203;</div><div><h3>Formula recall</h3><p>{counts['facts']} flashcards covering every formula and fact the specification expects you to remember. Rate yourself and the cards you fail come round again sooner.</p><div class="links"><a href="facts.html">Drill all</a><a href="facts.html?topic=trig-functions">Exact trig values</a><a href="facts.html?topic=logic">Logic vocabulary</a></div></div></div>
<div class="modecard"><div class="mi">&#127922;</div><div><h3>Skill drills</h3><p>Generated questions with fresh numbers every time: index laws, surds, log laws, quadratics, arithmetic and geometric series, binomial coefficients, differentiation and integration of powers, percentages, converse/contrapositive.</p><div class="links"><a href="drills.html">Practise</a></div></div></div>
<div class="modecard"><div class="mi">&#128221;</div><div><h3>Mock and past papers</h3><p>Timed full papers with automatic marking and grade conversion.</p><div class="links"><a href="papers.html">Mock papers</a><a href="official.html">Official papers</a><a href="grades.html">Grade calculator</a></div></div></div>
<div class="modecard"><div class="mi">&#128218;</div><div><h3>Exam technique</h3><p>How the papers are built, timing, the answer sheet, guessing strategy and the Paper 2 vocabulary (necessary, sufficient, converse, contrapositive).</p><div class="links"><a href="technique.html">Read</a></div></div></div>
"""
    return page("Practice", body, hero=h, active="practice.html")
