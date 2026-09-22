"""The JavaScript-driven pages: quick-fire, search, formula flashcards, skill drills, planner,
exam technique and the grade tables. They read site/qdata.js (built by build.py)."""
import json, html
from bank.topics import GROUPS, topic_index, TEST
from bank.official_keys import GRADES, SERIES, DEFAULT_GRADE_SERIES
from .site import page, hero, esc, NOTES_ALL
from . import mathtex

IDX = topic_index()


def _topic_options():
    out = '<option value="">All topics</option>'
    for g in GROUPS:
        out += f'<optgroup label="{esc(g["name"])}">' + "".join(f'<option value="{t["slug"]}">{esc(t["name"])}</option>' for t in g["topics"]) + "</optgroup>"
    return out


def quickfire_page():
    h = hero("Quick-fire", "One question at a time. Answer with the keys A-H or by clicking. Wrong answers are weighted three times more heavily next time; secure questions return on a spaced-repetition schedule.", pills=["Keyboard: A-H answer, N next, S solution"])
    body = f"""
<div class="qf-controls"><label>Paper <select id="fPaper"><option value="">Both</option><option value="1">Paper 1 style</option><option value="2">Paper 2 style</option></select></label>
<label>Group <select id="fGroup"><option value="">All</option><option value="part1">Part 1 (AS pure)</option><option value="part2">Part 2 (GCSE)</option><option value="section2">Section 2 (reasoning)</option></select></label>
<label>Topic <select id="fTopic">{_topic_options()}</select></label>
<label>Difficulty <select id="fDiff"><option value="">Any</option><option value="1">&#9733;</option><option value="2">&#9733;&#9733;</option><option value="3">&#9733;&#9733;&#9733;</option></select></label>
<label><input type="checkbox" id="fDue"> due for review only</label><label><input type="checkbox" id="fWeak"> needs-work only</label>
<span class="kbd" id="stats"></span></div>
<div class="tools" style="position:static"><span class="time" id="qclock">0:00</span><span class="pct">this question (budget 3:45)</span><span class="score" id="sessionScore"><b>0</b>/0 this session</span><span class="pct" id="sprintBox"></span><button class="primary" id="nextBtn" style="margin-left:auto">Next question (N)</button></div>
<div id="stage"></div>
"""
    js = r"""<script src="qdata.js"></script><script>(function(){
const P=new URLSearchParams(location.search);const $=id=>document.getElementById(id);
if(P.get('paper'))$('fPaper').value=P.get('paper');if(P.get('group'))$('fGroup').value=P.get('group');if(P.get('topic'))$('fTopic').value=P.get('topic');if(P.get('due'))$('fDue').checked=true;if(P.get('weak'))$('fWeak').checked=true;
const sprint=+P.get('sprint')||0;let sprintN=0,sprintC=0,sprintT0=0;
let sess={n:0,c:0},cur=null,t0=0,tick=null,recent=[];
function pool(){const prog=window.TM.prog();return window.QDATA.filter(q=>{if($('fPaper').value&&String(q.paper)!==$('fPaper').value)return false;if($('fGroup').value&&q.group!==$('fGroup').value)return false;if($('fTopic').value&&q.topic!==$('fTopic').value)return false;if($('fDiff').value&&String(q.diff)!==$('fDiff').value)return false;
  const s=prog[q.id]||0;if($('fWeak').checked&&s!==1)return false;if($('fDue').checked&&!(s===2&&window.TM.isDue(q.id)))return false;if(!$('fDue').checked&&s===2&&!window.TM.isDue(q.id))return false;return true;});}
function weight(q){const s=window.TM.prog()[q.id]||0;let w=s===1?3:1;if(recent.includes(q.id))w*=0.05;return w;}
function pickQ(){const p=pool();if(!p.length)return null;const tot=p.reduce((a,q)=>a+weight(q),0);let r=Math.random()*tot;for(const q of p){r-=weight(q);if(r<=0)return q;}return p[p.length-1];}
function fmt(s){return Math.floor(s/60)+':'+(s%60<10?'0':'')+s%60;}
function render(q){cur=q;const st=$('stage');if(!q){st.innerHTML='<p class="empty">No questions match these filters (or everything is secure and not yet due - well done). Change the filters or reset.</p>';return;}
  recent.push(q.id);if(recent.length>15)recent.shift();
  const opts=q.opts.map((o,i)=>'<li data-l="'+'ABCDEFGH'[i]+'"><span class="lt">'+'ABCDEFGH'[i]+'</span><span>'+o+'</span></li>').join('');
  const stars='\u2605'.repeat(q.diff)+'\u2606'.repeat(3-q.diff);
  st.innerHTML='<div class="q" id="'+q.id+'" data-qid="'+q.id+'" data-ans="'+q.ans+'" data-topic="'+q.topic+'"><div class="qh"><span class="num">'+q.id+'</span><span class="meta"><a href="topic/'+q.topic+'.html">'+q.tname+'</a> &middot; spec '+q.spec+' &middot; Paper '+q.paper+' style &middot; <span class="d">'+stars+'</span></span><div class="st"><button data-s="1">Needs work</button><button data-s="2">Secure</button></div></div><div class="qt">'+q.text+'</div><ol class="opts">'+opts+'</ol><div class="fb"></div><details class="sol"><summary>Worked solution (S)</summary><div class="sb">'+q.sol+'</div><div class="src">Answer <b>'+q.ans+'</b> &middot; <a href="topic/'+q.topic+'.html#'+q.id+'">open on its topic page</a> &middot; <a href="notes/'+q.topic+'.html">notes</a></div></details></div>';
  window.TM.math(st);window.TM.paint();t0=Date.now();clearInterval(tick);tick=setInterval(()=>{const s=Math.floor((Date.now()-t0)/1000);$('qclock').textContent=fmt(s);$('qclock').classList.toggle('low',s>225);},500);
  const p=pool();$('stats').textContent=p.length+' questions in the current pool';}
window.TM.focusQ=()=>document.querySelector('#stage .q');
window.TM.onAnswer=(q,right)=>{clearInterval(tick);sess.n++;if(right)sess.c++;$('sessionScore').innerHTML='<b>'+sess.c+'</b>/'+sess.n+' this session';
  if(sprint){sprintN++;if(right)sprintC++;$('sprintBox').textContent='Sprint: '+sprintN+'/'+sprint+' done';if(sprintN>=sprint){const secs=Math.round((Date.now()-sprintT0)/1000);setTimeout(()=>{alert('Sprint finished: '+sprintC+'/'+sprint+' in '+fmt(secs)+' ('+fmt(Math.round(secs/sprint))+' per question).');},50);}}};
function next(){if(sprint&&sprintN>=sprint){location.search='';return;}render(pickQ());}
$('nextBtn').onclick=next;document.addEventListener('keydown',e=>{if(e.target&&e.target.matches&&e.target.matches('input,select,textarea'))return;const k=e.key.toUpperCase();if(k==='N'||e.key===' '){e.preventDefault();next();}if(k==='S'){const d=document.querySelector('#stage details.sol');if(d)d.open=!d.open;}});
['fPaper','fGroup','fTopic','fDiff','fDue','fWeak'].forEach(id=>$(id).onchange=next);
if(sprint){sprintT0=Date.now();$('sprintBox').textContent='Sprint: 0/'+sprint+' done';}
const go=()=>window.renderMathInElement?next():setTimeout(go,60);go();
})();</script>"""
    return page("Quick-fire", body, hero=h, active="practice.html", extra_js=js)


def search_page():
    h = hero("Search", "Full-text search of every question, option and worked solution in the bank (and the real-question index).", cls="small")
    body = """<div class="qf-controls"><input type="search" id="q" placeholder="e.g. discriminant, contrapositive, trapezium rule, 2^x" style="flex:1 1 320px" autofocus><label>Paper <select id="p"><option value="">Both</option><option value="1">1</option><option value="2">2</option></select></label><span class="kbd" id="n"></span></div><div id="out"></div>"""
    js = r"""<script src="qdata.js"></script><script>(function(){
const $=id=>document.getElementById(id);let t=null;
function run(){const k=$('q').value.trim().toLowerCase();const p=$('p').value;const out=$('out');if(k.length<2){out.innerHTML='';$('n').textContent='';return;}
  const words=k.split(/\s+/);const hits=window.QDATA.filter(q=>(!p||String(q.paper)===p)&&words.every(w=>q.search.includes(w))).slice(0,60);
  $('n').textContent=hits.length+' result'+(hits.length===1?'':'s')+(hits.length===60?' (first 60)':'');
  out.innerHTML=hits.map(q=>'<a class="res" href="topic/'+q.topic+'.html#'+q.id+'"><div class="t">'+q.id+' &middot; '+q.tname+'</div><div class="m">spec '+q.spec+' &middot; Paper '+q.paper+' style &middot; answer '+q.ans+'</div><div class="s">'+q.text+'</div></a>').join('')||'<p class="empty">Nothing found.</p>';
  window.TM.math(out);}
$('q').oninput=()=>{clearTimeout(t);t=setTimeout(run,200);};$('p').onchange=run;
const P=new URLSearchParams(location.search);if(P.get('q')){$('q').value=P.get('q');run();}
})();</script>"""
    return page("Search", body, hero=h, extra_js=js)


def facts_page(facts):
    data = [{"t": f.topic, "tn": IDX[f.topic]["name"], "p": mathtex.to_html(f.prompt).replace("<p>", "").replace("</p>", ""),
             "a": mathtex.to_html(f.answer).replace("<p>", "").replace("</p>", ""), "s": f.spec, "i": i} for i, f in enumerate(facts)]
    h = hero("Formula recall", "There is no formula booklet in the TMUA. Flip each card, then rate yourself: cards you get wrong come back sooner (spaced repetition). Filter by topic to drill one area.", pills=[f"{len(facts)} cards"])
    body = f"""<div class="qf-controls"><label>Topic <select id="fTopic">{_topic_options()}</select></label><label><input type="checkbox" id="fDue" checked> due cards first</label><span class="kbd" id="stats"></span><span class="kbd"><kbd>space</kbd> flip &middot; <kbd>1</kbd> again &middot; <kbd>2</kbd> hard &middot; <kbd>3</kbd> easy</span></div>
<div class="drill" id="card"></div>"""
    js = f"""<script>window.FACTS={json.dumps(data, ensure_ascii=False)};</script><script>(function(){{
const $=id=>document.getElementById(id);const P=new URLSearchParams(location.search);if(P.get('topic'))$('fTopic').value=P.get('topic');
let sr=window.TM.LS('tmua.facts')||{{}};let cur=null,flipped=false;const IV=[0,1,3,7,14,30];
function pool(){{const t=$('fTopic').value;let p=window.FACTS.filter(f=>!t||f.t===t);const due=p.filter(f=>!sr[f.i]||sr[f.i].due<=Date.now());if($('fDue').checked&&due.length)p=due;return p;}}
function next(){{const p=pool();$('stats').textContent=p.length+' cards in pool';if(!p.length){{$('card').innerHTML='<p class="empty">No cards match.</p>';return;}}
  let c;do{{c=p[Math.floor(Math.random()*p.length)];}}while(p.length>1&&cur&&c.i===cur.i);cur=c;flipped=false;draw();}}
function draw(){{const c=cur;$('card').innerHTML='<div class="src">'+c.tn+' &middot; '+c.s+'</div><div class="term">'+c.p+'</div>'+(flipped?'<div class="def">'+c.a+'</div><div class="btns"><button class="btn" data-r="1" style="background:var(--bad)">Again (1)</button><button class="btn" data-r="2" style="background:var(--warn);color:#222">Hard (2)</button><button class="btn" data-r="3" style="background:var(--ok)">Easy (3)</button></div>':'<div class="btns"><button class="btn" id="flip">Show answer (space)</button><button class="btn ghost" id="skip">Skip</button></div>');
  window.TM.math($('card'));const f=$('flip');if(f)f.onclick=flip;const s=$('skip');if(s)s.onclick=next;$('card').querySelectorAll('[data-r]').forEach(b=>b.onclick=()=>rate(+b.dataset.r));}}
function flip(){{flipped=true;draw();}}
function rate(r){{const e=sr[cur.i]||{{lvl:0}};if(r===1)e.lvl=0;else if(r===2)e.lvl=Math.max(1,e.lvl);else e.lvl=Math.min(IV.length-1,e.lvl+1);e.due=Date.now()+IV[e.lvl]*86400000;sr[cur.i]=e;window.TM.SV('tmua.facts',sr);next();}}
document.addEventListener('keydown',e=>{{if(e.target&&e.target.matches&&e.target.matches('input,select'))return;if(e.key===' '){{e.preventDefault();if(!flipped)flip();}}if(flipped&&'123'.includes(e.key)&&e.key)rate(+e.key);}});
$('fTopic').onchange=next;$('fDue').onchange=next;const go=()=>window.renderMathInElement?next():setTimeout(go,60);go();
}})();</script>"""
    return page("Formula recall", body, hero=h, active="practice.html", extra_js=js)


def drills_page():
    h = hero("Skill drills", "Generated questions with fresh numbers every time, for the mechanical skills that must be fast and automatic without a calculator. Type the answer (fractions as a/b, surds as 2sqrt3, powers as x^2) or pick from the options.", pills=["Unlimited questions", "Instant marking"])
    body = """<div class="qf-controls"><label>Drill <select id="type">
<option value="indices">Indices: evaluate a^(m/n)</option><option value="surds">Surds: simplify a square root</option><option value="rational">Surds: rationalise 1/(a+sqrt b)</option>
<option value="expand">Expand (ax+b)(cx+d)</option><option value="factor">Factorise x^2+bx+c</option><option value="solveq">Solve a quadratic (integer roots)</option><option value="disc">Discriminant: how many real roots?</option><option value="cts">Complete the square: vertex</option>
<option value="logs">Logarithms: evaluate log_a b</option><option value="loglaw">Log laws: simplify</option><option value="expeq">Solve a^x = b</option>
<option value="ap">Arithmetic series: S_n</option><option value="gp">Geometric series: sum to infinity</option><option value="ncr">Binomial coefficient nCr</option><option value="binom">Binomial: a coefficient in (1+kx)^n</option>
<option value="diff">Differentiate a x^n</option><option value="int">Integrate a x^n (definite)</option><option value="tangent">Gradient of a tangent</option>
<option value="trig">Exact trig values</option><option value="line">Gradient of a perpendicular line</option><option value="pct">Reverse percentages</option><option value="hcf">HCF and LCM</option>
<option value="logic">Converse / contrapositive</option><option value="neg">Negate a statement</option></select></label><label><input type="checkbox" id="mix"> mix all drills</label><span class="score" id="sc"><b>0</b>/0</span><span class="kbd"><kbd>Enter</kbd> check &middot; <kbd>N</kbd> next</span></div>
<div class="drill" id="d"></div>"""
    js = r"""<script>(function(){
const $=id=>document.getElementById(id);let cur=null,n=0,c=0;const ri=(a,b)=>a+Math.floor(Math.random()*(b-a+1));const pick=a=>a[Math.floor(Math.random()*a.length)];
function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b];}return a;}
function frac(p,q){if(q<0){p=-p;q=-q;}const g=gcd(p,q)||1;p/=g;q/=g;return q===1?String(p):p+'/'+q;}
function tex(p,q){if(q<0){p=-p;q=-q;}const g=gcd(p,q)||1;p/=g;q/=g;return q===1?String(p):(p<0?'-':'')+'\\frac{'+Math.abs(p)+'}{'+q+'}';}
const norm=s=>String(s).toLowerCase().replace(/\s+/g,'').replace(/\*\*/g,'^').replace(/\u221a/g,'sqrt').replace(/×/g,'*').replace(/^\+/,'');
const D={
 indices(){const b=pick([4,8,9,16,25,27,32,64,81,125]);const roots={4:2,8:2,9:3,16:2,25:5,27:3,32:2,64:2,81:3,125:5};const r=roots[b];const nn=Math.round(Math.log(b)/Math.log(r));const m=pick([1,2,3,-1,-2]);const val=Math.pow(r,m);const ans=m<0?frac(1,Math.pow(r,-m)):String(val);
   return{q:'Evaluate \\('+b+'^{'+(m<0?'-':'')+'\\frac{'+Math.abs(m)+'}{'+nn+'}}\\)',a:[ans],w:'\\('+b+'^{1/'+nn+'} = '+r+'\\), then raise to the power '+m+': '+ans};},
 surds(){const s=pick([2,3,5,6,7]);const k=pick([2,3,4,5,6]);const N=k*k*s;return{q:'Simplify \\(\\sqrt{'+N+'}\\)',a:[k+'sqrt'+s,k+'sqrt('+s+')',k+'root'+s],w:'\\(\\sqrt{'+N+'} = \\sqrt{'+k*k+'\\times '+s+'} = '+k+'\\sqrt{'+s+'}\\)'};},
 rational(){const a=ri(1,4),b=pick([2,3,5,6,7]);const den=a*a-b;const sign=den<0?-1:1;const dd=Math.abs(den);const p=a*sign,q=-sign;const ans=(q<0?'('+p+'-sqrt'+b+')':'('+p+'+sqrt'+b+')')+'/'+dd;
   return{q:'Rationalise \\(\\dfrac{1}{'+a+'+\\sqrt{'+b+'}}\\) (write as (p+qsqrtb)/d)',a:[ans,ans.replace('(','').replace(')','')],w:'Multiply by \\('+a+'-\\sqrt{'+b+'}\\): denominator \\('+a*a+'-'+b+'='+den+'\\), so \\(\\dfrac{'+(q<0?a+'-':'-'+a+'+')+'\\sqrt{'+b+'}}{'+dd+'}\\)'};},
 expand(){const a=ri(1,3),b=ri(-6,6)||1,cc=ri(1,3),d=ri(-6,6)||-2;const A=a*cc,B=a*d+b*cc,C=b*d;const poly=(A>1?A:'')+'x^2'+(B?(B>0?'+':'')+(Math.abs(B)===1?(B<0?'-':''):B)+'x':'')+(C?(C>0?'+':'')+C:'');
   const show=(k,v)=>'('+(k>1?k:'')+'x'+(v>=0?'+':'')+v+')';return{q:'Expand \\('+show(a,b)+show(cc,d)+'\\)',a:[poly],w:'\\('+A+'x^2 '+(B>=0?'+':'')+B+'x '+(C>=0?'+':'')+C+'\\)'};},
 factor(){const p=ri(-7,7)||2,q=ri(-7,7)||3;const b=p+q,c=p*q;const sh=k=>'(x'+(k>=0?'+':'')+k+')';const ans=sh(p)+sh(q);return{q:'Factorise \\(x^2'+(b?(b>0?'+':'')+(Math.abs(b)===1?(b<0?'-':''):b)+'x':'')+(c>0?'+':'')+c+'\\)',a:[ans,sh(q)+sh(p)],w:'Two numbers with product '+c+' and sum '+b+': '+p+' and '+q};},
 solveq(){const p=ri(-8,8),q=ri(-8,8);const b=-(p+q),c=p*q;return{q:'Solve \\(x^2'+(b?(b>0?'+':'')+(Math.abs(b)===1?(b<0?'-':''):b)+'x':'')+(c?(c>0?'+':'')+c:'')+'=0\\) (answers as p,q)',a:[p+','+q,q+','+p],w:'\\((x'+(-p>=0?'+':'')+(-p)+')(x'+(-q>=0?'+':'')+(-q)+')=0\\), so \\(x='+p+'\\) or \\(x='+q+'\\)'};},
 disc(){const a=ri(1,3),b=ri(-8,8),c=ri(-6,6);const D=b*b-4*a*c;const ans=D>0?'2':D===0?'1':'0';return{q:'How many real roots has \\('+(a>1?a:'')+'x^2'+(b>=0?'+':'')+b+'x'+(c>=0?'+':'')+c+'=0\\)?',a:[ans],w:'Discriminant \\('+b*b+'-'+4*a*c+'='+D+'\\): '+ans+' real root(s)'};},
 cts(){const h=ri(-6,6),k=ri(-9,9);const b=-2*h,c=h*h+k;return{q:'Find the vertex of \\(y=x^2'+(b?(b>0?'+':'')+b+'x':'')+(c?(c>0?'+':'')+c:'')+'\\) (as h,k)',a:[h+','+k],w:'\\((x'+(-h>=0?'+':'')+(-h)+')^2'+(k>=0?'+':'')+k+'\\): vertex \\(('+h+','+k+')\\)'};},
 logs(){const a=pick([2,3,4,5,10]);const m=pick([-2,-1,0,1,2,3,4]);const arg=Math.pow(a,m);return{q:'Evaluate \\(\\log_{'+a+'}'+(m<0?'\\frac{1}{'+Math.pow(a,-m)+'}':arg)+'\\)',a:[String(m)],w:'\\('+a+'^{'+m+'}='+(m<0?'1/'+Math.pow(a,-m):arg)+'\\)'};},
 loglaw(){const t=ri(1,3);if(t===1){const a=pick([2,3,10]),x=ri(2,9),y=ri(2,9);return{q:'Simplify \\(\\log_{'+a+'}'+x+'+\\log_{'+a+'}'+y+'\\) as a single log \\(\\log_{'+a+'}N\\): give \\(N\\)',a:[String(x*y)],w:'\\(\\log(xy)\\): '+x*y};}
   if(t===2){const a=pick([2,3,10]),x=ri(2,9),k=ri(2,4);return{q:'Simplify \\('+k+'\\log_{'+a+'}'+x+'\\) as \\(\\log_{'+a+'}N\\): give \\(N\\)',a:[String(Math.pow(x,k))],w:'\\(\\log x^'+k+'\\): '+Math.pow(x,k)};}
   const a=pick([2,3,10]),y=ri(2,6),x=y*ri(2,8);return{q:'Simplify \\(\\log_{'+a+'}'+x+'-\\log_{'+a+'}'+y+'\\) as \\(\\log_{'+a+'}N\\): give \\(N\\)',a:[String(x/y)],w:'\\(\\log(x/y)\\): '+x/y};},
 expeq(){const a=pick([2,3,5]);const m=ri(1,4),d=pick([1,2,3]);const b=Math.pow(a,m);return{q:'Solve \\('+a+'^{'+(d>1?d+'x':'x')+'}='+b+'\\)',a:[frac(m,d)],w:'\\('+b+'='+a+'^'+m+'\\), so \\('+(d>1?d+'x':'x')+'='+m+'\\): \\(x='+frac(m,d)+'\\)'};},
 ap(){const a=ri(-5,12),d=ri(-4,7)||2,nn=pick([10,12,15,20,25]);const S=nn/2*(2*a+(nn-1)*d);return{q:'Arithmetic series: first term '+a+', common difference '+d+'. Find \\(S_{'+nn+'}\\)',a:[String(S)],w:'\\(\\frac{'+nn+'}{2}(2('+a+')+'+(nn-1)+'('+d+'))='+S+'\\)'};},
 gp(){const a=ri(1,12)*pick([1,2,3]);const q=pick([2,3,4,5]);const p=ri(1,q-1);const S=frac(a*q,q-p);return{q:'Geometric series with first term '+a+' and ratio \\('+tex(p,q)+'\\). Find \\(S_\\infty\\)',a:[S],w:'\\(\\frac{a}{1-r}=\\frac{'+a+'}{'+tex(q-p,q)+'}='+tex(a*q,q-p)+'\\)'};},
 ncr(){const nn=ri(4,9),r=ri(1,nn-1);let v=1;for(let i=0;i<r;i++)v=v*(nn-i)/(i+1);return{q:'Evaluate \\(\\binom{'+nn+'}{'+r+'}\\)',a:[String(Math.round(v))],w:'\\(\\frac{'+nn+'!}{'+r+'!'+(nn-r)+'!}='+Math.round(v)+'\\)'};},
 binom(){const nn=ri(4,7),r=ri(2,3),k=ri(2,3);let cnr=1;for(let i=0;i<r;i++)cnr=cnr*(nn-i)/(i+1);const v=Math.round(cnr)*Math.pow(k,r);return{q:'Coefficient of \\(x^'+r+'\\) in \\((1+'+k+'x)^'+nn+'\\)',a:[String(v)],w:'\\(\\binom{'+nn+'}{'+r+'}\\cdot '+k+'^'+r+'='+Math.round(cnr)+'\\times '+Math.pow(k,r)+'='+v+'\\)'};},
 diff(){const a=ri(1,6),nn=pick([2,3,4,5,-1,-2,0.5,1.5]);const co=a*nn,ex=nn-1;const fm=v=>Number.isInteger(v)?String(v):frac(Math.round(v*2),2);const ans=fm(co)+'x^'+(ex===1?'':'')+(Number.isInteger(ex)?ex:'('+fm(ex)+')');
   const alt=ex===1?fm(co)+'x':ex===0?fm(co):null;return{q:'Differentiate \\('+a+'x^{'+fm(nn)+'}\\)',a:[ans,alt,fm(co)+'x^'+fm(ex),fm(co)+'x^('+fm(ex)+')'].filter(Boolean),w:'\\(nx^{n-1}\\): \\('+fm(co)+'x^{'+fm(ex)+'}\\)'};},
 int(){const a=ri(1,4),nn=pick([1,2,3]);const lo=ri(0,2),hi=lo+ri(1,3);const F=x=>a*Math.pow(x,nn+1)/(nn+1);const val=F(hi)-F(lo);const ans=frac(Math.round(val*(nn+1)),nn+1);return{q:'Evaluate \\(\\displaystyle\\int_{'+lo+'}^{'+hi+'}'+a+'x^'+nn+'\\,dx\\)',a:[ans],w:'\\(\\left[\\frac{'+a+'x^'+(nn+1)+'}{'+(nn+1)+'}\\right]_{'+lo+'}^{'+hi+'}='+tex(Math.round(val*(nn+1)),nn+1)+'\\)'};},
 tangent(){const a=ri(1,3),b=ri(-5,5),x0=ri(-3,3);const g=2*a*x0+b;return{q:'Gradient of the tangent to \\(y='+a+'x^2'+(b?(b>0?'+':'')+b+'x':'')+'\\) at \\(x='+x0+'\\)',a:[String(g)],w:'\\(y\'='+2*a+'x'+(b>=0?'+':'')+b+'\\) at \\(x='+x0+'\\): '+g};},
 trig(){const f=pick(['sin','cos','tan']);const ang=pick(f==='tan'?[0,30,45,60]:[0,30,45,60,90]);const T={sin:{0:'0',30:'1/2',45:'sqrt2/2',60:'sqrt3/2',90:'1'},cos:{0:'1',30:'sqrt3/2',45:'sqrt2/2',60:'1/2',90:'0'},tan:{0:'0',30:'1/sqrt3',45:'1',60:'sqrt3'}};const ans=T[f][ang];
   const alts={'sqrt2/2':['1/sqrt2'],'1/sqrt3':['sqrt3/3'],'sqrt3/2':[],'1/2':['0.5']};return{q:'Exact value of \\(\\'+f+' '+ang+'^\\circ\\)',a:[ans].concat(alts[ans]||[]),w:'\\(\\'+f+' '+ang+'^\\circ='+ans.replace('sqrt2/2','\\tfrac{\\sqrt2}{2}').replace('sqrt3/2','\\tfrac{\\sqrt3}{2}').replace('1/sqrt3','\\tfrac{1}{\\sqrt3}').replace('sqrt3','\\sqrt3').replace('1/2','\\tfrac12')+'\\)'};},
 line(){const a=ri(1,6),b=ri(1,6);const s=pick([1,-1]);const m=frac(s*a,b);const perp=frac(-s*b,a);return{q:'A line has gradient \\('+tex(s*a,b)+'\\). Gradient of a perpendicular line?',a:[perp],w:'Negative reciprocal: \\('+tex(-s*b,a)+'\\)'};},
 pct(){const p=pick([5,10,15,20,25,40,50]);const up=Math.random()<0.5;const orig=ri(2,40)*10;const fin=orig*(up?100+p:100-p)/100;return{q:'After a '+p+'% '+(up?'increase':'decrease')+' a price is '+fin+'. What was the original price?',a:[String(orig)],w:fin+' \\(\\div\\) '+(up?100+p:100-p)/100+' = '+orig};},
 hcf(){const g=pick([2,3,4,6,12]);const a=g*pick([2,3,5,7]),b=g*pick([2,3,5,7,4]);const h=gcd(a,b),l=a*b/h;return{q:'Find the HCF and LCM of '+a+' and '+b+' (as hcf,lcm)',a:[h+','+l],w:'HCF '+h+', LCM '+a+'\\(\\times\\)'+b+'/'+h+' = '+l};},
 logic(){const S=[['n is a multiple of 4','n is even'],['x > 3','x^2 > 9'],['a shape is a square','it has four equal sides'],['it is raining','the ground is wet'],['f\'(a) = 0','f has a stationary point at a']];const [A,B]=pick(S);const kind=pick(['converse','contrapositive','inverse']);const ans={converse:'if '+B+' then '+A,contrapositive:'if not '+B+' then not '+A,inverse:'if not '+A+' then not '+B};
   const opts=Object.values(ans);return{q:'Statement: <b>if '+A+' then '+B+'</b>. Which is its <b>'+kind+'</b>?',mc:opts,a:[ans[kind]],w:'Converse swaps; contrapositive swaps and negates (and is equivalent to the original); inverse negates both.'};},
 neg(){const S=[['every student passed','at least one student did not pass'],['there exists an x with x^2 < 0','for all x, x^2 >= 0'],['x > 3 and y <= 5','x <= 3 or y > 5'],['for all n, n^2 + n + 41 is prime','there exists n for which n^2 + n + 41 is not prime'],['some prime is even','no prime is even']];const [s,a]=pick(S);
   const wrong=S.filter(x=>x[1]!==a).map(x=>x[1]).sort(()=>Math.random()-0.5).slice(0,3);const opts=[a].concat(wrong).sort(()=>Math.random()-0.5);return{q:'Negate: <b>'+s+'</b>',mc:opts,a:[a],w:'Swap for-all/exists and negate the inner statement; not(A and B) = (not A) or (not B).'};}
};
function next(){const types=Object.keys(D);const t=$('mix').checked?pick(types):$('type').value;cur=D[t]();cur.t=t;const d=$('d');
  d.innerHTML='<div class="src">'+$('type').querySelector('[value="'+t+'"]').textContent+'</div><div class="term">'+cur.q+'</div>'+(cur.mc?'<div class="btns">'+cur.mc.map(o=>'<button class="btn ghost mc">'+o+'</button>').join('')+'</div>':'<input class="ans" id="ans" autocomplete="off" placeholder="your answer"><div class="btns"><button class="btn" id="chk">Check</button><button class="btn ghost" id="show">Show answer</button></div>')+'<div class="fbk" id="fbk"></div><div class="work" id="work" style="display:none"></div>';
  window.TM.math(d);const i=$('ans');if(i){i.focus();i.onkeydown=e=>{if(e.key==='Enter')check(i.value);};$('chk').onclick=()=>check(i.value);$('show').onclick=()=>reveal(false);}
  d.querySelectorAll('.mc').forEach(b=>b.onclick=()=>check(b.textContent));}
function check(v){if(cur.done)return;const ok=cur.a.some(a=>norm(a)===norm(v));cur.done=true;n++;if(ok)c++;$('sc').innerHTML='<b>'+c+'</b>/'+n;$('fbk').textContent=ok?'\u2713 Correct':'\u2717 Not quite - answer: '+cur.a[0];$('fbk').className='fbk '+(ok?'ok':'bad');reveal(true);}
function reveal(marked){if(!marked){cur.done=true;n++;$('sc').innerHTML='<b>'+c+'</b>/'+n;$('fbk').textContent='Answer: '+cur.a[0];$('fbk').className='fbk';}const w=$('work');w.style.display='block';w.innerHTML=cur.w;window.TM.math(w);}
document.addEventListener('keydown',e=>{if(e.key.toUpperCase()==='N'&&!e.target.matches('input')){next();}if(e.key==='Enter'&&cur&&cur.done)next();});
$('type').onchange=next;$('mix').onchange=next;const go=()=>window.renderMathInElement?next():setTimeout(go,60);go();
})();</script>"""
    return page("Skill drills", body, hero=h, active="practice.html", extra_js=js)


def planner_page(by_topic, real_counts):
    rows = ""
    for g in GROUPS:
        for t in g["topics"]:
            qs = by_topic.get(t["slug"], [])
            rows += f'<tr data-topic="{t["slug"]}" data-n="{len(qs)}"><td><a href="topic/{t["slug"]}.html">{esc(t["name"])}</a><br><span style="font-size:.8rem;color:var(--stone)">{esc(g["name"].split(":")[0])}</span></td><td>{real_counts.get(t["slug"], 0)}</td><td class="acc">-</td><td class="pr"></td><td class="links"><a href="notes/{t["slug"]}.html">notes</a><a href="quickfire.html?topic={t["slug"]}">practise</a><a href="quickfire.html?topic={t["slug"]}&weak=1">weak only</a></td></tr>'
    h = hero("Revision planner", "Countdown to your test date, your accuracy by topic (from every question you have answered anywhere on the site), your mock and past-paper scores, and what to do next.")
    body = f"""<div class="grid3 plan">
<div class="card"><h3>Test date</h3><input type="date" id="examDate"><div class="big" id="days">-</div><p id="daysNote">Set your TMUA sitting date (the test runs in October and January sittings).</p></div>
<div class="card"><h3>Questions answered</h3><div class="big" id="nAns">0</div><p id="accAll">accuracy -</p></div>
<div class="card"><h3>Due for review</h3><div class="big" id="nDue">0</div><p>secure questions whose spaced-repetition interval has expired &middot; <a href="quickfire.html?due=1">review now</a></p></div>
</div>
<h2 class="sec">Suggested next steps</h2><div class="card" id="next"></div>
<h2 class="sec">Topics, weakest first</h2>
<table class="list" id="tt"><tr><th>Topic</th><th>Real Qs</th><th>Your accuracy</th><th>Progress</th><th></th></tr>{rows}</table>
<h2 class="sec">Paper scores</h2><table class="list" id="scores"><tr><th>Paper</th><th>Score</th><th>Grade</th><th>Time</th><th>Date</th></tr></table>
"""
    js = r"""<script src="qdata.js"></script><script>(function(){
const $=id=>document.getElementById(id);const att=window.TM.att(),prog=window.TM.prog(),srs=window.TM.srs();
const d=$('examDate');d.value=window.TM.LS('tmua.examDate')||'';function days(){if(!d.value){$('days').textContent='-';return;}const n=Math.ceil((new Date(d.value)-new Date())/86400000);$('days').textContent=n;$('daysNote').textContent=n>0?'days to go':'the date has passed';}
d.onchange=()=>{window.TM.SV('tmua.examDate',d.value);days();};days();
let tot=0,cor=0;const byT={};window.QDATA.forEach(q=>{const a=att[q.id];if(a){tot+=a.n;cor+=a.c;byT[q.topic]=byT[q.topic]||{n:0,c:0};byT[q.topic].n+=a.n;byT[q.topic].c+=a.c;}});
$('nAns').textContent=tot;$('accAll').textContent=tot?'accuracy '+Math.round(100*cor/tot)+'%':'accuracy -';
$('nDue').textContent=Object.keys(prog).filter(id=>prog[id]===2&&window.TM.isDue(id)).length;
const rows=[...document.querySelectorAll('#tt tr[data-topic]')];const info=[];
rows.forEach(r=>{const t=r.dataset.topic;const v=byT[t];const acc=v?v.c/v.n:null;const n=+r.dataset.n;const ids=window.QDATA.filter(q=>q.topic===t).map(q=>q.id);const ok=ids.filter(i=>prog[i]===2).length,wk=ids.filter(i=>prog[i]===1).length;
  r.querySelector('.acc').innerHTML=v?Math.round(100*acc)+'% <span style="font-size:.8rem;color:var(--stone)">('+v.c+'/'+v.n+')</span>':'<span style="color:var(--stone)">not tried</span>';
  r.querySelector('.pr').innerHTML='<div class="bar"><div class="ok" style="width:'+(100*ok/n)+'%"></div><div class="wk" style="width:'+(100*wk/n)+'%"></div></div><span style="font-size:.8rem;color:var(--stone)">'+ok+'/'+n+' secure</span>';
  info.push({r,t,acc,tried:!!v,wk,ok,n});});
info.sort((a,b)=>(a.tried?a.acc:-1)-(b.tried?b.acc:-1)||(b.wk-a.wk));const tb=$('tt');info.forEach(i=>tb.appendChild(i.r));
const weak=info.filter(i=>i.tried&&i.acc<0.6).slice(0,3),untried=info.filter(i=>!i.tried).slice(0,3),due=+$('nDue').textContent;
let html='';if(weak.length)html+='<p><b>Fix the weak spots:</b> '+weak.map(i=>'<a href="notes/'+i.t+'.html">'+window.TOPICS[i.t].name+'</a> ('+Math.round(100*i.acc)+'%, <a href="quickfire.html?topic='+i.t+'">practise</a>)').join(', ')+'.</p>';
if(untried.length)html+='<p><b>Cover new ground:</b> '+untried.map(i=>'<a href="topic/'+i.t+'.html">'+window.TOPICS[i.t].name+'</a>').join(', ')+' have not been attempted yet.</p>';
if(due)html+='<p><b>Consolidate:</b> '+due+' secure questions are due for a spaced-repetition review - <a href="quickfire.html?due=1">review them</a>.</p>';
const sc=window.TM.LS('tmua.scores')||{};const keys=Object.keys(sc);if(!keys.length)html+='<p><b>Sit a paper:</b> you have no paper scores yet. Start with a <a href="papers.html">mock paper</a> or the <a href="official.html">specimen paper</a> under timed conditions.</p>';
else{const last=keys.map(k=>sc[k]).sort((a,b)=>b.date-a.date)[0];html+='<p><b>Papers:</b> your latest paper scored '+last.score+'/20'+(last.grade?' (grade '+last.grade+')':'')+'. Alternate Paper 1 and Paper 2 sittings, and always work through the solutions of every question you missed.</p>';}
if(!html)html='<p>Answer some questions and the planner will fill in.</p>';$('next').innerHTML=html;
const st=$('scores');keys.map(k=>[k,sc[k]]).sort((a,b)=>b[1].date-a[1].date).forEach(([k,s])=>{const tr=document.createElement('tr');const name=s.real?k.replace('real-','Official ').replace('-P',' Paper '):'Mock '+k.replace('P','Paper ').replace('-Set',' Set ');const href=s.real?'real/'+k.replace('real-','')+'.html':'paper/'+k+'.html';
  tr.innerHTML='<td><a href="'+href+'">'+name+'</a></td><td><b>'+s.score+'/20</b></td><td>'+(s.grade!=null?Number(s.grade).toFixed(1):'-')+'</td><td>'+(s.secs?Math.round(s.secs/60)+' min':'-')+'</td><td>'+new Date(s.date).toLocaleDateString()+'</td>';st.appendChild(tr);});
})();</script>"""
    return page("Revision planner", body, hero=h, active="planner.html", extra_js=js)


def technique_page():
    h = hero("Exam technique", "How the TMUA is built, how to use the 75 minutes, and the Paper 2 vocabulary you must read precisely.")
    body = r"""<div class="notes">
<h2>The format</h2>
<ul><li>Two papers of 20 multiple-choice questions, 75 minutes each, taken one after the other. Options run A to H (usually 5 to 8 of them). One mark per question, <b>no negative marking</b>: never leave a blank.</li>
<li>No calculator, no dictionary, no formula booklet. Rough working goes on the question paper; only the answer sheet is marked, so transfer answers carefully (in pencil) as you go rather than at the end.</li>
<li>Paper 1 tests Section 1 (AS pure plus Higher GCSE) as applications; Paper 2 tests reasoning: the same maths plus the logic and proof of Section 2. Both papers carry equal weight and grades run from 1.0 to 9.0 on the published conversion tables.</li></ul>
<h2>Timing</h2>
<ul><li>75 minutes for 20 questions is 3 minutes 45 seconds each. The papers are roughly ordered easy to hard, so bank the early marks quickly: aim to be at question 10 by 25-30 minutes.</li>
<li>Two-pass strategy: on the first pass answer anything you can do in under 4 minutes; mark the rest, put a provisional answer on the sheet, and return. Never let one question eat 10 minutes.</li>
<li>Use quick-fire's per-question stopwatch and the sprint mode to calibrate your pace before the real thing.</li></ul>
<h2>Answering multiple choice</h2>
<ul><li>Options are information. For 'find the value' questions, test the options (substitute back, check a boundary value, check signs and units). For 'complete set of values' questions, test one number from each candidate interval.</li>
<li>Eliminate: an option that fails a sanity check (negative area, a probability above 1, a root that makes a log argument negative) is gone. Then guess among what is left.</li>
<li>Statement questions (I, II, III): decide each statement independently, hunting for a counterexample before believing 'must be true'. The eight-option list is always the same, so you only need the pattern.</li>
<li>Draw. Sketching the graph or the sign chart is usually faster than algebra for 'how many solutions' and inequality questions.</li></ul>
<h2>Paper 2 vocabulary</h2>
<table class="list"><tr><th>Phrase</th><th>Meaning</th></tr>
<tr><td>if A then B; A implies B; A only if B; B if A</td><td>A &rArr; B. Whenever A holds, B holds. Says nothing about what happens when A is false.</td></tr>
<tr><td>converse</td><td>B &rArr; A. Not equivalent to the statement.</td></tr>
<tr><td>contrapositive</td><td>(not B) &rArr; (not A). Equivalent to the statement.</td></tr>
<tr><td>A if and only if B</td><td>A &rArr; B and B &rArr; A.</td></tr>
<tr><td>P is sufficient for Q</td><td>P &rArr; Q (P is enough to guarantee Q).</td></tr>
<tr><td>P is necessary for Q</td><td>Q &rArr; P (Q cannot happen without P).</td></tr>
<tr><td>for all / for every</td><td>Refuted by a single counterexample.</td></tr>
<tr><td>for some / there exists</td><td>Proved by a single example; means 'at least one'.</td></tr>
<tr><td>the negation of ...</td><td>Swap 'for all' with 'there exists', 'and' with 'or', and negate the inner statement; not(x &gt; 3) is x &le; 3.</td></tr>
<tr><td>counterexample to 'if A then B'</td><td>A case where A is true and B is false.</td></tr>
<tr><td>the first error occurs on line ...</td><td>Find the first line that is not a valid deduction from the lines before it (dividing by zero, squaring, sin&alpha; = sin&beta; &rArr; &alpha; = &beta;, multiplying an inequality by an unknown sign, assuming the conclusion).</td></tr></table>
<h2>Common mathematical traps</h2>
<ul><li>&radic;(x&sup2;) = |x|. Squaring an equation or an inequality can add solutions; taking a square root can lose the negative one.</li>
<li>Extraneous roots: solutions of a log or surd equation must be checked in the original.</li>
<li>Counting solutions of trig equations: count the periods in the interval, check the endpoints and whether the interval is open or closed.</li>
<li>Definite integral versus area: a region under the axis contributes a negative integral.</li>
<li>The trapezium rule over-estimates a convex curve and under-estimates a concave one.</li>
<li>Percentages compound multiplicatively; two successive 10% rises are 21%.</li></ul>
<h2>The week before</h2>
<ul><li>Sit the most recent official papers under full timed conditions (use the online marking to get the real grade).</li>
<li>Run the formula-recall deck until every card is 'easy' - there is no booklet.</li>
<li>Reread the notes for your three weakest topics in the planner and redo their needs-work questions.</li></ul>
</div>"""
    return page("Exam technique", body, hero=h, active="practice.html")


def grades_page():
    tabs = ""
    for sid, label, year, note in sorted(SERIES, key=lambda s: -s[2]):
        if sid not in GRADES:
            continue
        g = GRADES[sid]
        rows = "".join(f"<tr><td>{i}</td><td>{g['p1'][i]}</td><td>{g['p2'][i]}</td></tr>" for i in range(20, -1, -1))
        orows = "".join(f"<tr><td>{i}</td><td>{g['overall'][i]}</td></tr>" for i in range(40, -1, -1))
        tabs += f'<h2 class="sec" id="g{sid}">{esc(label)}</h2><div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start"><table class="grades"><tr><th>Raw</th><th>Paper 1</th><th>Paper 2</th></tr>{rows}</table><table class="grades"><tr><th>Raw /40</th><th>Overall</th></tr>{orows}</table></div>'
    h = hero("Grades", "The TMUA is reported on a scale from 1.0 to 9.0. Each year's raw-score conversion is published with the answer key; the calculator below converts a score on any published table, and the site's mock papers use the " + DEFAULT_GRADE_SERIES + " table.")
    opts = "".join(f'<option value="{sid}">{esc(label)}</option>' for sid, label, year, note in sorted(SERIES, key=lambda s: -s[2]) if sid in GRADES)
    body = f"""<div class="card plan"><h3>Grade calculator</h3><div class="qf-controls"><label>Conversion table <select id="ser">{opts}</select></label><label>Paper 1 raw <input type="number" id="r1" min="0" max="20" value="12" style="width:70px;font:inherit;padding:5px"></label><label>Paper 2 raw <input type="number" id="r2" min="0" max="20" value="12" style="width:70px;font:inherit;padding:5px"></label></div><div id="gout" style="font-size:1.1rem"></div></div>
<p class="note">Overall grade is read from the combined raw score out of 40 on the overall table, not by averaging the paper grades. No conversion was published with the 2023 key, so 2023 sittings use the calculator with another year's table as an estimate.</p>
{tabs}"""
    js = f"""<script>window.GRADES={json.dumps(GRADES)};(function(){{const $=id=>document.getElementById(id);function go(){{const g=window.GRADES[$('ser').value];const a=Math.max(0,Math.min(20,+$('r1').value||0)),b=Math.max(0,Math.min(20,+$('r2').value||0));
$('gout').innerHTML='Paper 1: <b>'+g.p1[a].toFixed(1)+'</b> &nbsp;&middot;&nbsp; Paper 2: <b>'+g.p2[b].toFixed(1)+'</b> &nbsp;&middot;&nbsp; Overall ('+(a+b)+'/40): <b style="color:var(--gold);font-size:1.4rem">'+g.overall[a+b].toFixed(1)+'</b>';}}
['ser','r1','r2'].forEach(i=>$(i).oninput=go);go();}})();</script>"""
    return page("Grades", body, hero=h, active="official.html", extra_js=js)
