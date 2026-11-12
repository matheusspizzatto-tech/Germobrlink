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
    ("fruticultura", "Fruticultura", "Pomar, colheita e atacado", True),
    ("avicultura-suinocultura", "Avicultura e suinocultura", "Lotes, ração e acerto", True),
    ("cana", "Cana e usinas", "ATR, custo e contrato", True),
    ("madeira", "Pínus e eucalipto", "Inventário, corte e venda", True),
    ("mel", "Mel e apicultura", "Colmeias, florada e venda", True),
    ("agroindustria", "Agroindústrias e fábricas", "Produção, custo e clientes", True),
    ("tecnicos", "Técnicos e agrônomos", "Visitas, relatórios e clientes", True),
    ("estudantes", "Estudantes de agronomia", "Estágio, TCC e slides", True),
    ("creators", "Criadores de conteúdo", "Roteiros, posts e parcerias", True),
]
TAREFAS = [
    ("vender-producao", "Vender a produção", "Propostas e melhor preço"),
    ("imposto-papelada", "Impostos e taxas", "Dúvidas explicadas"),
    ("contratos", "Contratos e leis", "Como fazer e o que diz a lei"),
    ("controle-custos", "Custos e taxas", "Para onde vai o seu dinheiro"),
    ("credito-rural", "Crédito rural", "Pronaf e financiamento"),
    ("licencas-ambientais", "Licenças ambientais", "CAR e outorga"),
    ("clima-safra", "Clima e safra", "Janela de plantio e alertas"),
    ("cobranca", "Cobrança de clientes", "Quem deve e como cobrar"),
    ("equipe", "Equipe e funcionários", "Salários e escala"),
    ("instagram", "Instagram e vendas online", "Posts, legendas e reels"),
]

CHEV = '<svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 3.5 5 6.5 8 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def nome(k):
    return NOME.get(k, k)


def links_html(home="/paginainicial"):
    return (
        '<nav class="links" aria-label="Seções">'
        f'<button type="button" class="mtr" id="mtr" data-p="mega" aria-expanded="false" aria-controls="mega">Soluções {CHEV}</button>'
        f'<button type="button" class="mtr" id="atr" data-p="mega2" aria-expanded="false" aria-controls="mega2">Os 10 ajudantes {CHEV}</button>'
        f'<a href="{home}#como">Como funciona</a>'
        f'<a href="{home}#exemplos">Exemplos</a>'
        f'<a href="{home}#perguntas">Perguntas</a>'
        '</nav>'
    )


def burger_html():
    return ('<button type="button" class="mbtn" id="mbtn" aria-label="Abrir o menu" aria-expanded="false" aria-controls="mega">'
            '<i></i><i></i></button>')


def _agentes(atual):
    return "".join(
        f'<a class="mi mag{" cur" if k == atual else ""}" style="--c:{c}" href="/ajudante/{k}"><img src="/img/{k}.webp" alt="" loading="lazy" width="40" height="40">'
        f'<span><b>{nome(k)}</b><small>{d}</small></span></a>'
        for k, c, d in AGENTES)


def panel_html(home="/paginainicial", atual=None):
    nichos = "".join(f'<a class="mi{" cur" if s == atual else ""}" href="/para/{s}"><b>{t}</b><small>{d}</small></a>' for s, t, d, live in NICHOS_MENU)
    tarefas = "".join(f'<a class="mi{" cur" if s == atual else ""}" href="/tarefa/{s}"><b>{t}</b><small>{d}</small></a>' for s, t, d in TAREFAS)
    foot = f'<div class="mfoot"><span>Todos os ajudantes ficam no mesmo número de WhatsApp.</span><a href="{home}#planos">Entrar na lista de espera →</a></div>'
    return (
        '<div class="mega" id="mega" hidden><div class="in"><div class="mcols">'
        f'<div class="mcol"><p class="mh">Para quem faz o agro</p><div class="ml g3">{nichos}</div></div>'
        f'<div class="mcol"><p class="mh">Por tarefa</p><div class="ml g2t">{tarefas}</div></div>'
        f'<div class="mcol monly"><p class="mh">Os 10 ajudantes</p><div class="ml g2">{_agentes(atual)}</div></div>'
        f'</div>{foot}</div></div>'
        '<div class="mega" id="mega2" hidden><div class="in">'
        f'<p class="mh">Os 10 ajudantes · cada um com uma função, todos no mesmo número de WhatsApp</p><div class="ml g5">{_agentes(atual)}</div>'
        f'{foot}</div></div>'
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
.mcols{display:grid;grid-template-columns:3fr 2fr;gap:48px}
.ml.g2t{display:grid;grid-template-columns:repeat(2,1fr);gap:2px 22px}
.monly{display:none}
.ml.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:2px 22px}
.ml.g5{display:grid;grid-template-columns:repeat(5,1fr);gap:6px 14px}
.ml.g5 .mi.mag{flex-direction:column;align-items:flex-start;gap:8px;padding:12px}
.ml.g5 .mi.mag img{width:52px;height:52px}
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
.mi.mag{transition:background .2s ease,box-shadow .2s ease}
a.mi.mag:hover,a.mi.mag:focus-visible{background:color-mix(in srgb,var(--c) 11%,#fff);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--c) 32%,transparent)}
.mi.mag img{transition:transform .25s cubic-bezier(.2,1.6,.4,1)}
a.mi.mag:hover img{transform:translateY(-3px) rotate(-4deg)}
a.mi.mag:hover b{color:color-mix(in srgb,var(--c) 70%,#15201A)}

/* desktop: painel flutuante que desce como uma aba (estilo AbacatePay) */
@media (min-width:921px){
  .mega{left:50%;right:auto;width:min(1180px,calc(100% - 32px));top:calc(100% + 10px);transform:translateX(-50%);border:1px solid var(--line);border-radius:24px;background:#fff;box-shadow:0 30px 70px -28px rgba(21,32,26,.32),0 2px 6px rgba(21,32,26,.04);overflow:hidden;
    opacity:0;clip-path:inset(0 0 100% 0 round 24px);transition:clip-path .38s cubic-bezier(.22,1,.36,1),opacity .2s ease}
  .mega.on{opacity:1;clip-path:inset(0 0 0 0 round 24px);transform:translateX(-50%)}
  .nav .mega .in{max-width:none;padding:30px 34px 0}
  .mega .mcols,.mega .ml.g5{transform:translateY(-8px);opacity:0;transition:transform .4s cubic-bezier(.22,1,.36,1) .05s,opacity .3s ease .05s}
  .mega.on .mcols,.mega.on .ml.g5{transform:none;opacity:1}
  .mega .mfoot{margin:26px -34px 0;padding:16px 34px;border-top:1px solid var(--line);background:#F7F9F7}
  .mega .mfoot a{color:var(--ink)}
  .mega .mfoot a:hover{color:var(--verde-lab)}
}

/* menu compacto e alinhado */
.links a,.mtr{white-space:nowrap}
@media (max-width:1200px){.links a,.mtr{padding:10px 11px;font-size:14.5px}}
@media (max-width:1080px){.links a{display:none}}
@media (min-width:921px){
  .mega{width:min(1080px,calc(100% - 32px))}
  .nav .mega .in{padding:26px 30px 0}
  .mega .mcols{grid-template-columns:auto auto;justify-content:space-between;gap:0}
  .mega .mcol+.mcol{border-left:1px solid var(--line);padding-left:30px;margin-left:30px}
  .mega .ml.g3{grid-template-columns:repeat(3,190px);gap:0 8px}
  .mega .ml.g2t{grid-template-columns:repeat(2,175px);gap:0 8px}
  .mega .mi{padding:8px 10px;margin:0 -10px}
  .mega .mi b{font-size:14px;white-space:nowrap}
  .mega .mi small{font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .mega .mh{margin-bottom:10px;padding-bottom:10px}
  .mega .mfoot{margin:22px -30px 0;padding:14px 30px}
}
/* topo no celular: menu à esquerda, logo no centro, botão à direita */
@media (max-width:920px){.nav>.in{display:grid!important;grid-template-columns:auto 1fr auto;gap:10px}.nav>.in .sp{display:none}.mbtn{order:-1;grid-column:1;grid-row:1}.nav>.in .logo{grid-column:2;grid-row:1;justify-self:center}.nav>.in .ncta{grid-column:3;grid-row:1}}
@media (max-width:400px){.nav>.in .logo .gm{display:none}}
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
  .monly{display:block}
  .ml.g3,.ml.g2t{grid-template-columns:1fr}
  #mega2{display:none!important}
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
(function(){const mb=document.getElementById('mbtn');const trs=[...document.querySelectorAll('.mtr[data-p]')];const pans=[...document.querySelectorAll('.mega')];if(!pans.length)return;
  let cur=null,t={};const mobile=()=>matchMedia('(max-width:920px)').matches;
  const trOf=p=>trs.find(x=>x.dataset.p===p.id);
  const close=p=>{if(!p)return;p.classList.remove('on');const tr=trOf(p);tr&&tr.setAttribute('aria-expanded','false');if(p.id==='mega'&&mb)mb.setAttribute('aria-expanded','false');clearTimeout(t[p.id]);t[p.id]=setTimeout(()=>{if(!p.classList.contains('on'))p.hidden=true},180);if(cur===p)cur=null;document.body.classList.remove('mopen')};
  const open=p=>{if(cur&&cur!==p){cur.classList.remove('on');cur.hidden=true;const o=trOf(cur);o&&o.setAttribute('aria-expanded','false')}clearTimeout(t[p.id]);p.hidden=false;requestAnimationFrame(()=>p.classList.add('on'));const tr=trOf(p);tr&&tr.setAttribute('aria-expanded','true');if(p.id==='mega'&&mb&&mobile()){mb.setAttribute('aria-expanded','true');document.body.classList.add('mopen')}cur=p};
  const isOpen=p=>p&&!p.hidden&&p.classList.contains('on');
  trs.forEach(tr=>{const p=document.getElementById(tr.dataset.p);tr.addEventListener('click',()=>isOpen(p)?close(p):open(p));
    if(matchMedia('(hover:hover)').matches){let h;[tr,p].forEach(el=>{el.addEventListener('mouseenter',()=>{clearTimeout(h);clearTimeout(t[p.id]);h=setTimeout(()=>open(p),90)});el.addEventListener('mouseleave',()=>{clearTimeout(h);h=setTimeout(()=>{if(cur===p)close(p)},220)})})}});
  mb&&mb.addEventListener('click',()=>{const p=document.getElementById('mega');isOpen(p)?close(p):open(p)});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&cur){const p=cur;close(p);(trOf(p)||mb).focus()}});
  document.addEventListener('click',e=>{if(cur&&!cur.contains(e.target)&&!trs.some(x=>x.contains(e.target))&&!mb?.contains(e.target))close(cur)});
  pans.forEach(p=>p.addEventListener('click',e=>{if(e.target.closest('a'))close(p)}));
})();
"""
