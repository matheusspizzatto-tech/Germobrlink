# Menu "Soluções" compartilhado entre a landing principal e as páginas de nicho.
# Gera HTML, CSS e JS. Usado por scripts/nichos.py.

AGENTES = [
    ("planilha", "#19E35F", "Controle da fazenda sem abrir o computador"),
    ("clima", "#1FC7B6", "Chuva e geada antes da hora"),
    ("campo", "#A0673A", "Relatório de visita em PDF"),
    ("agronomo", "#D93A2B", "Dúvida da lavoura respondida"),
    ("vendas", "#F2C230", "Proposta pronta para mandar"),
    ("viral", "#F26B1D", "Roteiro de reels"),
    ("vitrine", "#3AA0FF", "Post e legenda"),
    ("apresenta", "#7B5CFF", "Slides em minutos"),
    ("juridico", "#8E2443", "Contrato lido e explicado"),
    ("contabil", "#24408E", "Imposto de renda do produtor"),
]
NOME = {"agronomo": "agrônomo", "juridico": "jurídico", "contabil": "contábil"}

NICHOS_MENU = [
    ("graos", "Grãos", "Soja, milho e trigo", True),
    ("pecuaria-leite", "Pecuária de leite", "Ordenha, custos e laticínio", True),
    ("pecuaria-corte", "Pecuária de corte", "Rebanho, pesagem e venda", True),
    ("cafe", "Café", "Da florada à saca", True),
    ("hortifruti", "Hortifrúti e orgânicos", "Feira, mercado e entrega", True),
    ("tecnicos", "Técnicos e agrônomos", "Visitas, relatórios e clientes", True),
    ("estudantes", "Estudantes de agronomia", "Estágio, TCC e apresentações", True),
    ("creators", "Criadores de conteúdo do agro", "Roteiros, posts e parcerias", True),
]
TAREFAS = [
    ("vender-producao", "Vender a produção", "Propostas e comparação de preço"),
    ("imposto-papelada", "Imposto e papelada", "Livro caixa e imposto de renda"),
    ("contratos", "Contratos e arrendamento", "Leitura e pontos de atenção"),
    ("instagram", "Instagram e vendas online", "Posts, legendas e reels"),
    ("controle-custos", "Controle de custos", "Custo por hectare e por litro"),
]

CHEV = '<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5 5 6.5 8 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def nome(k):
    return NOME.get(k, k)


def links_html(home="/paginainicial"):
    return (
        '<nav class="links" aria-label="Seções">'
        f'<button type="button" class="mtr" id="mtr" aria-expanded="false" aria-controls="mega">Soluções {CHEV}</button>'
        f'<a href="{home}#como">Como funciona</a>'
        f'<a href="{home}#ajudantes">Os 10 ajudantes</a>'
        f'<a href="{home}#exemplos">Exemplos</a>'
        f'<a href="{home}#perguntas">Perguntas</a>'
        '</nav>'
    )


def burger_html():
    return ('<button type="button" class="mbtn" id="mbtn" aria-label="Abrir o menu" aria-expanded="false" aria-controls="mega">'
            '<i></i><i></i></button>')


def panel_html(home="/paginainicial", atual=None):
    col1 = "".join(
        (f'<a class="mi{" cur" if s == atual else ""}" href="/para/{s}"><b>{t}</b><small>{d}</small></a>' if live else
         f'<span class="mi off"><b>{t} <em>em breve</em></b><small>{d}</small></span>')
        for s, t, d, live in NICHOS_MENU)
    col2 = "".join(
        f'<a class="mi mag{" cur" if k == atual else ""}" href="/ajudante/{k}"><img src="/img/{k}.webp" alt="" loading="lazy" width="30" height="30">'
        f'<span><b style="--c:{c}">{nome(k)}</b><small>{d}</small></span></a>'
        for k, c, d in AGENTES)
    col3 = "".join(
        f'<a class="mi{" cur" if s == atual else ""}" href="/tarefa/{s}"><b>{t}</b><small>{d}</small></a>' for s, t, d in TAREFAS)
    return (
        '<div class="mega" id="mega" hidden><div class="in"><div class="mcols">'
        f'<div class="mcol"><p class="mh">Para quem faz o agro</p><div class="ml">{col1}</div></div>'
        f'<div class="mcol two"><p class="mh">Os 10 ajudantes</p><div class="ml g2">{col2}</div></div>'
        f'<div class="mcol"><p class="mh">Por tarefa</p><div class="ml">{col3}</div></div>'
        '</div>'
        f'<div class="mfoot"><span>Todos os ajudantes ficam no mesmo WhatsApp.</span><a href="{home}#planos">Entrar na lista de espera →</a></div>'
        '</div></div>'
    )


MENU_CSS = """
/* menu Soluções */
.mtr{display:inline-flex;align-items:center;gap:6px;border:0;background:none;cursor:pointer;font-weight:600;font-size:15px;color:var(--ink2);padding:10px 14px;border-radius:999px}
.mtr:hover,.mtr[aria-expanded="true"]{background:var(--soft)}
.mtr svg{transition:transform .2s}
.mtr[aria-expanded="true"] svg{transform:rotate(180deg)}
.mega{position:absolute;left:0;right:0;top:100%;background:#fff;border-top:1px solid var(--line);box-shadow:0 30px 60px -30px rgba(21,32,26,.28);opacity:0;transform:translateY(-6px);transition:opacity .18s ease,transform .18s ease}
.mega.on{opacity:1;transform:none}
.nav .mega .in{display:block;height:auto;padding-top:30px;padding-bottom:22px}
.mcols{display:grid;grid-template-columns:1fr 1.55fr 1fr;gap:48px}
.mh{margin:0 0 14px;padding-bottom:12px;border-bottom:1px solid var(--line);font-size:12.5px;font-weight:600;color:var(--mute);letter-spacing:.01em}
.ml{display:flex;flex-direction:column;gap:2px}
.ml.g2{display:grid;grid-template-columns:1fr 1fr;gap:2px 18px}
.mi{display:flex;flex-direction:column;gap:2px;padding:9px 10px;margin:0 -10px;border-radius:12px;text-decoration:none;color:var(--ink)}
a.mi:hover{background:var(--soft)}
.mi b{font-size:14.5px;font-weight:600;letter-spacing:-.01em}
.mi small{font-size:13px;color:var(--mute);font-weight:500;line-height:1.35}
.mi.cur b{color:var(--verde-lab)}
.mi.off b{color:#8A938D}
.mi.off small{color:#A3ABA6}
.mi em{font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#8A938D;background:var(--soft);border-radius:999px;padding:2px 7px;margin-left:4px;vertical-align:2px}
.mi.mag{flex-direction:row;align-items:center;gap:10px}
.mi.mag img{width:30px;height:30px;object-fit:contain;flex:none}
.mi.mag span{display:flex;flex-direction:column;gap:1px;min-width:0}
.mi.mag b:before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--c);margin-right:7px;vertical-align:2px}
.mfoot{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-top:20px;padding-top:16px;border-top:1px solid var(--line);font-size:13.5px;color:var(--mute);font-weight:500}
.mfoot a{color:var(--verde-lab);font-weight:700;text-decoration:none}
.mbtn{display:none;width:42px;height:42px;border-radius:50%;border:0;background:var(--soft);cursor:pointer;flex:none;flex-direction:column;align-items:center;justify-content:center;gap:5px}
.mbtn i{display:block;width:16px;height:1.8px;border-radius:2px;background:var(--ink);transition:transform .2s}
.mbtn[aria-expanded="true"] i:first-child{transform:translateY(3.4px) rotate(45deg)}
.mbtn[aria-expanded="true"] i:last-child{transform:translateY(-3.4px) rotate(-45deg)}
@media (max-width:920px){
  .mbtn{display:flex}
  .mega{position:absolute;top:100%;height:calc(100vh - 72px);height:calc(100dvh - 72px);overflow-y:auto;overscroll-behavior:contain;border-top:1px solid var(--line);box-shadow:none;-webkit-overflow-scrolling:touch}
  .nav .mega .in{padding-top:8px;padding-bottom:calc(28px + env(safe-area-inset-bottom,0px))}
  .mcols{grid-template-columns:1fr;gap:0}
  .mcol{border-bottom:1px solid var(--line);padding:18px 0 12px}
  .mh{border:0;padding:0;margin-bottom:8px}
  .ml.g2{grid-template-columns:1fr 1fr;gap:0 10px}
  .mi.mag small{display:none}
  .mfoot{flex-direction:column;align-items:flex-start;border:0;margin-top:6px}
  body.mopen{overflow:hidden}
}
@media (max-width:420px){.nav .in{gap:8px}.mbtn{width:38px;height:38px}.ncta i{display:none}.ncta{padding-left:13px!important}.wm{font-size:19px!important}}
"""

MENU_JS = """
(function(){const mega=document.getElementById('mega'),tr=document.getElementById('mtr'),mb=document.getElementById('mbtn');if(!mega)return;
  let t;const open=()=>{clearTimeout(t);if(!mega.hidden&&mega.classList.contains('on'))return;mega.hidden=false;requestAnimationFrame(()=>mega.classList.add('on'));tr&&tr.setAttribute('aria-expanded','true');mb&&mb.setAttribute('aria-expanded','true');if(matchMedia('(max-width:920px)').matches)document.body.classList.add('mopen')};
  const close=()=>{mega.classList.remove('on');tr&&tr.setAttribute('aria-expanded','false');mb&&mb.setAttribute('aria-expanded','false');document.body.classList.remove('mopen');t=setTimeout(()=>{mega.hidden=true},180)};
  const isOpen=()=>!mega.hidden&&mega.classList.contains('on');
  tr&&tr.addEventListener('click',()=>isOpen()?close():open());
  mb&&mb.addEventListener('click',()=>isOpen()?close():open());
  if(matchMedia('(hover:hover)').matches){let h;const wrap=[tr,mega];wrap.forEach(el=>el&&el.addEventListener('mouseenter',()=>{clearTimeout(h);h=setTimeout(open,90)}));wrap.forEach(el=>el&&el.addEventListener('mouseleave',()=>{clearTimeout(h);h=setTimeout(close,220)}))}
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&isOpen()){close();(tr||mb).focus()}});
  document.addEventListener('click',e=>{if(isOpen()&&!mega.contains(e.target)&&e.target!==tr&&!tr?.contains(e.target)&&!mb?.contains(e.target))close()});
  mega.addEventListener('click',e=>{if(e.target.closest('a'))close()});
})();
"""
