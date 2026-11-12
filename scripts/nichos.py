# Gera as páginas de nicho em /para/<slug>/index.html a partir de um modelo único.
# Uso: python3 scripts/nichos.py   (rodar na raiz do repositório)
import os, html
import json
from menu import links_html, burger_html, panel_html, MENU_CSS, MENU_JS, nome, NICHOS_MENU, TAREFAS, AGENTES
from dados_extra import paginas

CF = "https://d2ol7oe51mr4n9.cloudfront.net/user_2vVA8WvBFtZCaqwnis3S3BiJPUC/"
COR = {"planilha": "#19E35F", "clima": "#1FC7B6", "campo": "#A0673A", "agronomo": "#D93A2B", "vendas": "#F2C230",
       "viral": "#F26B1D", "vitrine": "#3AA0FF", "apresenta": "#7B5CFF", "juridico": "#8E2443", "contabil": "#24408E"}
TXT = {"planilha": "#0F8A3D", "clima": "#0E8C80", "campo": "#8A5530", "agronomo": "#C8402F", "vendas": "#9A7708",
       "viral": "#C9520F", "vitrine": "#1F7FD6", "apresenta": "#5B3FE0", "juridico": "#8E2443", "contabil": "#24408E"}

_FJ = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fotos.json")))
F = {k: CF + v for k, v in _FJ.items()}

# ---------- maquetes do que fica pronto ----------
def tabela(titulo, sub, cab, linhas, total=None, destaque=None):
    th = "".join(f'<th{" class=r" if i else ""}>{c}</th>' for i, c in enumerate(cab))
    tr = ""
    for ln in linhas:
        tds = "".join(f'<td{" class=r" if i else ""}{(" data-"+(destaque[2] if len(destaque)>2 else "dn")) if destaque and (destaque[0], destaque[1]) == (ln[0], i) else ""}>{c}</td>' for i, c in enumerate(ln))
        tr += f"<tr>{tds}</tr>"
    if total:
        tr += "<tr class=tt>" + "".join(f'<td{" class=r" if i else ""}>{c}</td>' for i, c in enumerate(total)) + "</tr>"
    return f'<div class="mk tb"><div class="mkh"><b>{titulo}</b><small>{sub}</small></div><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def contas(titulo, sub, linhas, fim, nota=None):
    rows = "".join(f'<div class="rw"><span>{a}</span><b>{b}</b></div>' for a, b in linhas)
    n = f'<p class="nt">{nota}</p>' if nota else ""
    return f'<div class="mk ct2"><div class="mkh"><b>{titulo}</b><small>{sub}</small></div>{rows}<div class="rw fim"><span>{fim[0]}</span><b>{fim[1]}</b></div>{n}</div>'

def msg(quem, cor, texto, para):
    return (f'<div class="mk wam"><div class="wah"><span class="wav">{para[0]}</span><span><b>{para}</b><small>rascunho pronto para enviar</small></span></div>'
            f'<div class="bb"><span class="who" style="color:{cor}">{quem}</span>{texto}</div></div>')

def dias(titulo, sub, ds, aviso):
    cel = "".join(f'<div class="d{" hot" if h else ""}"><small>{d}</small><b>{t}</b><span>{c}</span></div>' for d, t, c, h in ds)
    return f'<div class="mk dias"><div class="mkh"><b>{titulo}</b><small>{sub}</small></div><div class="dg">{cel}</div><p class="nt ok">{aviso}</p></div>'

def doc(tag, titulo, foto, kv, alerta):
    k = "".join(f'<div class="kv"><span>{a}</span><span{" class=ok" if ok else ""}>{b}</span></div>' for a, b, ok in kv)
    return (f'<div class="mk docm"><div class="dh"><small>{tag}</small><b>{titulo}</b></div><div class="ph" style="background-image:url({foto})"></div>'
            f'{k}<div class="al">{alerta}</div><div class="ln"></div><div class="ln s"></div></div>')

def slide(tag, titulo, num, rot, foto):
    return (f'<div class="mk sld"><div class="sl"><small>{tag}</small><b>{titulo}</b><div class="big"><span>{num}</span><small>{rot}</small></div></div>'
            f'<div class="sr2" style="background-image:url({foto})"></div></div>')

def post(marca, ini, chamada, titulo, foto, legenda):
    return (f'<div class="mk igp"><div class="igh"><span class="iga">{ini}</span><b>{marca}</b></div><div class="igi" style="background-image:url({foto})">'
            f'<div class="igt"><small>{chamada}</small><b>{titulo}</b></div></div><p class="igc"><b>{marca}</b> {legenda}</p></div>')

def roteiro(titulo, foto, passos):
    li = "".join(f"<li><b>{t}</b>{x}</li>" for t, x in passos)
    return f'<div class="mk reel"><div class="ph" style="background-image:url({foto})"><span>{titulo}</span></div><ol>{li}</ol></div>'

def contrato(tag, titulo, marcas, rodape):
    m = "".join(f'<div class="ln"></div><div class="ln s"></div><div class="mkr">{x}</div>' for x in marcas)
    return f'<div class="mk docm ctr"><div class="dh"><small>{tag}</small><b>{titulo}</b></div>{m}<div class="ln"></div><div class="ft2"><span>jurídico</span><span>{rodape}</span></div></div>'

# ---------- conteúdo dos nichos ----------
N = {}
N["pecuaria-leite"] = dict(
    titulo="Germo para pecuária de leite",
    desc="Controle de ordenha, custo do litro e proposta para o laticínio, tudo pelo WhatsApp. Você manda um áudio do curral e recebe pronto.",
    eyebrow="Para pecuária de leite",
    h1='Sua ordenha, seus custos e seu leite vendido, <span class="g">tudo pelo WhatsApp.</span>',
    lead="Você manda um áudio do curral e os ajudantes da Germo devolvem o controle das vacas, o custo real do litro e a proposta para o laticínio. Sem abrir o computador.",
    foto=CF + "1e32365a-32bc-449b-a8a8-95e80f0f9ac5.webp", foto_alt="Vaca holandesa no galpão de uma fazenda de leite",
    chat=("Anota aí: a Pintada deu 21 litros hoje, as outras normal.", "planilha", "Anotado. A Pintada está 15% abaixo da média dela nos últimos 30 dias. Vale ficar de olho."),
    dor_t='O leite não espera, <span class="g">a papelada também não devia.</span>',
    dor=[("Caderno do curral", "Os litros de cada vaca ficam anotados no papel e ninguém soma no fim do mês."),
         ("Custo no escuro", "Ração, mão de obra e energia sobem, e fica difícil saber quanto custa cada litro."),
         ("Preço na mão do comprador", "Sem números organizados, a conversa com o laticínio começa em desvantagem.")],
    entregas=[
        ("planilha", "Controle de ordenha por vaca", "Você fala os litros, a planilha soma, tira a média e avisa quem caiu.",
         tabela("Ordenha de novembro", "litros por dia", ["Vaca", "Hoje", "Média 30 dias"],
                [["Mimosa", "28,0", "27,4"], ["Estrela", "31,5", "30,1"], ["Pintada", "21,0", "24,8"], ["Morena", "26,2", "25,9"]],
                ["Total", "106,7", "108,2"], ("Pintada", 1))),
        ("planilha", "Custo real do litro", "Junta as notas do mês e mostra quanto sobra em cada litro vendido.",
         contas("Custo do litro · outubro", "com base nas notas enviadas",
                [("Ração e concentrado", "R$ 0,98"), ("Mão de obra", "R$ 0,41"), ("Energia e outros", "R$ 0,23"), ("Custo por litro", "R$ 1,62")],
                ("Sobra por litro, a R$ 2,35", "R$ 0,73"))),
        ("vendas", "Proposta para o laticínio", "Uma mensagem clara, com volume e qualidade, pronta para mandar.",
         msg("vendas", TXT["vendas"], "Oi, Marcos! Produzo 3.200 litros por mês, com CCS abaixo de 300 mil. Consigo entregar a partir de março. Qual o preço que vocês pagam com o bônus de qualidade?", "Laticínio Serra Verde")),
    ],
    foto2=CF + "1290ef20-afee-4069-80c6-93e9644acc5b.webp", foto2_alt="Mãos do produtor segurando um balde de leite na sala de ordenha",
    pedidos_t='Do jeito que você <span class="g">já fala no curral.</span>',
    pedidos=["Quanto eu gastei de ração esse mês?", "Monta o calendário de vacinação do rebanho.",
             "A Mimosa foi inseminada dia 3 de agosto, quando ela pare?", "Escreve um post pra vender o queijo da fazenda."],
    ajudantes=[("planilha", "Ordenha, rebanho e custos do mês em planilha."), ("vendas", "Proposta para o laticínio e venda do queijo."),
               ("contabil", "Livro caixa e imposto de renda do produtor."), ("clima", "Calor e chuva que mexem com o pasto e a produção.")],
    faq=[("Preciso ter um sistema de gestão do leite?", "Não. Você manda os números por áudio ou mensagem e a planilha é montada para você. Se já tem uma planilha, é só mandar que nós continuamos a partir dela."),
         ("Serve para quem tem poucas vacas?", "Sim. Funciona do mesmo jeito para 10 ou para 300 vacas. Você paga pelo plano, não pelo tamanho do rebanho."),
         ("O ajudante substitui o veterinário?", "Não. Ele organiza os dados e avisa quando algo foge do normal, como uma queda de produção. Diagnóstico e tratamento são sempre com o seu veterinário.")],
)
N["graos"] = dict(
    titulo="Germo para grãos",
    desc="Custo por hectare, janela de chuva para a colheita e comparação de propostas da saca, tudo pelo WhatsApp. Soja, milho e trigo.",
    eyebrow="Para grãos: soja, milho e trigo",
    h1='Da compra do insumo à venda da saca, <span class="g">tudo pelo WhatsApp.</span>',
    lead="Você manda um áudio da lavoura e os ajudantes da Germo devolvem o custo por hectare, o aviso de chuva para a colheita e as propostas de venda lado a lado.",
    foto=CF + "8d1cbb5f-96f0-49d8-958e-0442b9b5b015.webp", foto_alt="Colheitadeira colhendo soja no fim da tarde",
    chat=("Vai dar pra colher o talhão 3 essa semana?", "clima", "Quinta e sexta sem chuva, com umidade baixa à tarde. A melhor janela é quinta, depois das 11h."),
    dor_t='A safra é grande, <span class="g">a margem é apertada.</span>',
    dor=[("Custo espalhado", "Nota de semente, adubo e defensivo em pastas diferentes, e o custo por hectare só aparece no fim."),
         ("Colheita na sorte", "Uma chuva fora de hora atrasa a colheita e derruba a qualidade do grão."),
         ("Venda sem comparação", "Cada comprador fala um preço e um prazo, e comparar tudo de cabeça custa dinheiro.")],
    entregas=[
        ("planilha", "Custo por hectare da safra", "Você manda as notas e recebe o custo por hectare e o ponto de equilíbrio.",
         contas("Soja 26/27 · custo por hectare", "talhões 1 a 4 · 420 ha",
                [("Sementes", "R$ 820"), ("Fertilizantes", "R$ 1.640"), ("Defensivos", "R$ 1.120"), ("Operações e frete", "R$ 690")],
                ("Total por hectare", "R$ 4.270"), "Ponto de equilíbrio: 34 sacas por hectare a R$ 126.")),
        ("clima", "Janela de colheita", "A previsão da sua propriedade, dia a dia, com a melhor hora para entrar.",
         dias("Previsão para a sua fazenda", "Sorriso, MT", [("Seg", "31°", "8 mm", False), ("Ter", "30°", "3 mm", False), ("Qua", "32°", "0 mm", False), ("Qui", "33°", "0 mm", True), ("Sex", "32°", "0 mm", True)],
              "Melhor janela: quinta e sexta, depois das 11h.")),
        ("vendas", "Para quem vender a saca", "As propostas que você recebeu, lado a lado, com o valor líquido.",
         tabela("Propostas da semana", "soja, 60 kg", ["Comprador", "Preço", "Líquido"],
                [["Cooperativa", "R$ 131", "R$ 131"], ["Cerealista do trevo", "R$ 133", "R$ 133"], ["Trading", "R$ 134", "R$ 129"]],
                None, ("Cerealista do trevo", 2, "up"))),
    ],
    foto2=CF + "27208630-676d-4548-af26-5108db224014.webp", foto2_alt="Mão do produtor pegando grãos de soja na carreta",
    pedidos_t='Do jeito que você <span class="g">já fala na lavoura.</span>',
    pedidos=["Quanto eu preciso colher pra pagar a safra?", "Lê esse contrato de arrendamento pra mim.",
             "Monta a planilha de custos do milho safrinha.", "Me avisa se vier geada no trigo."],
    ajudantes=[("planilha", "Custos, talhões e safra em planilha."), ("clima", "Chuva, geada e janela de plantio e colheita."),
               ("vendas", "Comparação de propostas e mensagem para o comprador."), ("juridico", "Arrendamento e contrato de venda explicados.")],
    faq=[("Funciona para soja, milho e trigo?", "Sim, e para qualquer outra cultura. Você fala o que planta e os ajudantes usam isso em cada resposta."),
         ("Os preços da saca são em tempo real?", "O ajudante de vendas organiza e compara as propostas e cotações que você recebe e manda para ele. O preço que vale é sempre o que o comprador confirmar."),
         ("O ajudante substitui o agrônomo?", "Não. Ele organiza custos, previsão e documentos. Recomendação técnica e receituário são sempre com o seu agrônomo.")],
)
N["tecnicos"] = dict(
    titulo="Germo para técnicos e agrônomos",
    desc="Relatório de visita em PDF, apresentação de resultados e posts para o seu perfil, tudo pelo WhatsApp. Você grava um áudio e recebe pronto.",
    eyebrow="Para técnicos e agrônomos",
    h1='Mais visitas no dia e <span class="g">o relatório pronto antes de voltar.</span>',
    lead="Você grava um áudio no fim da visita e recebe o relatório em PDF com as fotos, a apresentação para o cliente e os posts para o seu perfil profissional.",
    foto=CF + "848e5dee-a7b6-4e07-91ac-dc4f0a1bb466.webp", foto_alt="Técnica agrícola avaliando uma folha de soja na lavoura",
    chat=("Visita na Fazenda Boa Vista: soja em R3, ferrugem na reboleira do talhão 2, recomendei aplicação.", "campo", "Relatório pronto: 3 páginas com as 6 fotos. Quer que eu deixe a mensagem pronta para o produtor?"),
    dor_t='O seu tempo vale mais <span class="g">no campo do que no computador.</span>',
    dor=[("Noite de relatório", "A visita acaba às 17h e o relatório só fica pronto depois das 22h."),
         ("Fotos perdidas", "As fotos ficam no celular, sem ordem, e montar o PDF leva mais tempo que a visita."),
         ("Perfil parado", "Você vê casos ótimos todo dia, mas não sobra tempo para mostrar o seu trabalho.")],
    entregas=[
        ("campo", "Relatório de visita em PDF", "Com as suas fotos, a fase da lavoura e o que você recomendou.",
         doc("RELATÓRIO DE VISITA · PDF", "Fazenda Boa Vista · Talhão 2", CF + "848e5dee-a7b6-4e07-91ac-dc4f0a1bb466.webp",
             [("Cultura e fase", "Soja · R3", False), ("Ocorrência", "Ferrugem em reboleira", False), ("Recomendação", "Registrada", True)],
             "Retorno em 7 dias para avaliar a aplicação")),
        ("apresenta", "Apresentação de resultados", "A safra do cliente em slides prontos para a reunião.",
         slide("SAFRA 25/26 · FAZENDA BOA VISTA", "Resultado da safra", "68", "sacas por hectare", CF + "8d1cbb5f-96f0-49d8-958e-0442b9b5b015.webp")),
        ("vitrine", "Post para o seu perfil", "A visita do dia vira conteúdo, com imagem e legenda.",
         post("eng.agro.carla", "C", "NO CAMPO HOJE", "3 sinais de ferrugem para ficar de olho", CF + "848e5dee-a7b6-4e07-91ac-dc4f0a1bb466.webp",
              "Visita de hoje na soja em R3. O que eu olho primeiro quando suspeito de ferrugem 👇")),
    ],
    foto2=CF + "e75f3f04-f76f-48ee-9b08-b74b95da2532.webp", foto2_alt="Agrônomo conversando com o produtor ao lado da caminhonete",
    pedidos_t='Do jeito que você <span class="g">já fala entre uma visita e outra.</span>',
    pedidos=["Organiza minha agenda de visitas da semana.", "Faz uma proposta de consultoria mensal para esse produtor.",
             "Transforma essa visita num post pro meu Instagram.", "Monta a apresentação de resultados da safra."],
    ajudantes=[("campo", "Relatório de visita em PDF com as suas fotos."), ("apresenta", "Slides de resultado para o cliente."),
               ("vitrine", "Posts e legendas para o seu perfil."), ("vendas", "Proposta de consultoria pronta para mandar.")],
    faq=[("As recomendações técnicas são do ajudante?", "Não. O relatório é montado com o que você falou e fotografou. A recomendação é sempre sua, com o seu nome e o seu registro."),
         ("Funciona sem sinal no campo?", "Sim. Você grava o áudio e tira as fotos no campo, e o WhatsApp envia quando pegar sinal. O relatório chega assim que a mensagem sai."),
         ("Serve para estudante e estagiário?", "Sim. O mesmo ajudante monta o relatório de estágio e a apresentação para a banca.")],
)
for _s in ("pecuaria-leite", "graos", "tecnicos"):
    N[_s]["cat"] = "para"
N.update(paginas(F, TXT, tabela, contas, msg, dias, doc, slide, post, roteiro, contrato))
CATS = {"para": ("Soluções", [s for s, *_ in NICHOS_MENU]), "tarefa": ("Tarefas", [s for s, *_ in TAREFAS]), "ajudante": ("Ajudantes", [k for k, *_ in AGENTES])}
from chats import CHATS
for _k, _v in CHATS.items():
    if _k in N: N[_k]["chat"] = _v
ROT = {s: t for s, t, *_ in NICHOS_MENU}
ROT.update({s: t for s, t, _ in TAREFAS})
ROT.update({k: "Ajudante " + nome(k) for k, *_ in AGENTES})

LOGO = '<svg width="24" height="24" viewBox="134 134 372 372"><circle cx="320" cy="320" r="175" fill="none" stroke="#0A0C0B" stroke-width="26"/><circle cx="342" cy="298.5" r="111" fill="none" stroke="#0A0C0B" stroke-width="26"/><circle cx="357.5" cy="282.5" r="52.5" fill="none" stroke="#0A0C0B" stroke-width="24"/><circle cx="360" cy="279" r="24" fill="#0A0C0B"/></svg>'
CHK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
ARR = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#15201A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

CSS = """
:root{--bg:#fff;--soft:#F5F8F5;--ink:#15201A;--ink2:#2E3A33;--mute:#5B665F;--ring:#E4EAE4;--pill:#DCE8DE;--line:#ECEFEC;--broto:#19E35F;--verde:#13A94B;--verde-lab:#0F8A3D;--mint:#EEFBF2;--mint2:#DDF6E5;
--display:"Archivo",system-ui,sans-serif;--body:"Manrope",system-ui,sans-serif;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:84px}body{margin:0;font-family:var(--body);color:var(--ink);background:#fff;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}img{max-width:100%;display:block}button,input{font:inherit;color:inherit}:focus-visible{outline:3px solid var(--broto);outline-offset:3px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
.in{max-width:1160px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.eyebrow{font-family:var(--display);font-stretch:112%;font-weight:700;letter-spacing:.1em;font-size:12.5px;color:var(--verde-lab);text-transform:uppercase}
h1,h2,h3{margin:0;text-wrap:balance}
h1{font-family:var(--display);font-weight:500;letter-spacing:-.045em;line-height:1.02;font-size:clamp(36px,5vw,62px)}
h2{font-family:var(--display);font-weight:500;letter-spacing:-.04em;line-height:1.05;font-size:clamp(30px,3.8vw,46px)}
h3{font-family:var(--display);font-weight:600;letter-spacing:-.025em;line-height:1.15;font-size:20px}
.g{color:var(--verde)}
.lead{font-size:clamp(17px,1.6vw,19px);line-height:1.55;color:var(--ink2);margin:0;max-width:54ch}
section{padding-block:clamp(56px,8vw,104px)}
.head{display:flex;flex-direction:column;gap:12px;max-width:720px;margin-bottom:clamp(28px,4vw,44px)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:0;cursor:pointer;border-radius:999px;padding:15px 24px;font-weight:700;font-size:16px;text-decoration:none;white-space:nowrap;transition:transform .15s,filter .15s}
.btn:hover{transform:translateY(-1px)}.btn.pr{background:var(--broto);color:#0A0C0B}.btn.ol{background:#fff;box-shadow:0 0 0 1.5px var(--ring)}
.btn .ar{display:grid;place-items:center;width:26px;height:26px;border-radius:50%;background:#15201A;color:var(--broto);font-size:14px}
/* topo */
.nav{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.94);-webkit-backdrop-filter:saturate(1.4) blur(10px);backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.nav .in{display:flex;align-items:center;gap:22px;height:72px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex:none}.gm{width:36px;height:36px;border-radius:9px;background:var(--broto);display:grid;place-items:center}
.wm{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:22px;letter-spacing:-.01em}.wm b{color:var(--broto);font-weight:800}
.links{display:flex;gap:2px;margin-left:8px;align-items:center}.links a{text-decoration:none;font-weight:600;font-size:15px;color:var(--ink2);padding:10px 14px;border-radius:999px}.links a:hover{background:var(--soft)}
.nav .sp{flex:1}
.ncta{text-decoration:none;display:inline-flex;align-items:center;gap:10px;background:rgba(255,255,255,.72);color:var(--ink);border-radius:999px;padding:6px 6px 6px 16px;font-weight:700;font-size:14.5px;white-space:nowrap;box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 0 0 1.5px rgba(21,32,26,.08),0 10px 24px -12px rgba(21,32,26,.35);transition:transform .2s}
.ncta:hover{transform:translateY(-1px)}.ncta i{position:relative;width:8px;height:8px;border-radius:50%;background:var(--verde);flex:none}
.ncta i:after{content:"";position:absolute;inset:0;border-radius:50%;background:var(--verde);animation:nping 1.8s ease-out infinite}@keyframes nping{0%{transform:scale(1);opacity:.7}100%{transform:scale(2.8);opacity:0}}
.ncta span{display:grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--broto);flex:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.5)}
@media (max-width:920px){.links{display:none}}
@media (max-width:420px){.wm{font-size:20px}.ncta{font-size:13.5px;gap:8px;padding:5px 5px 5px 13px}.ncta span{width:30px;height:30px}}
/* migalha */
.crumb{display:flex;gap:8px;align-items:center;font-size:13.5px;font-weight:600;color:var(--mute);margin-bottom:22px}.crumb a{text-decoration:none}.crumb a:hover{color:var(--ink)}.crumb i{font-style:normal;color:#B5BDB8}
/* herói */
.hero{padding-top:clamp(28px,4vw,48px);background:linear-gradient(180deg,#fff 0%,var(--mint) 100%)}
.hg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.02fr);gap:clamp(28px,5vw,64px);align-items:center}
.ht{display:flex;flex-direction:column;gap:20px}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:6px}
.chk{display:flex;gap:10px 18px;flex-wrap:wrap;font-size:14.5px;font-weight:600;color:var(--ink2)}.chk span{display:inline-flex;align-items:center;gap:7px}.chk svg{color:var(--verde)}
.hp{position:relative}
.hp .ph{aspect-ratio:4/3.1;border-radius:32px;background-size:cover;background-position:center;box-shadow:0 40px 80px -40px rgba(21,32,26,.45)}
.wa{position:absolute;left:-28px;bottom:-30px;width:min(340px,82%);background:#EFEAE2;border-radius:22px;padding:12px;display:flex;flex-direction:column;gap:8px;box-shadow:0 24px 50px -20px rgba(21,32,26,.5)}
.wa .b{max-width:92%;border-radius:12px;padding:8px 11px;font-size:13.5px;line-height:1.4;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.wa .o{align-self:flex-end;background:#D9FDD3;border-top-right-radius:3px}.wa .i{align-self:flex-start;background:#fff;border-top-left-radius:3px}
.wa .who{display:block;font-weight:800;font-size:12.5px;margin-bottom:2px}
.wa .wh{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;color:#54656F;padding:0 2px 2px}.wa .wh img{width:22px;height:22px;object-fit:contain}
/* dores */
.dores{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.dor{border-radius:24px;padding:24px;background:#fff;box-shadow:0 0 0 1.5px var(--ring)}
.dor small{display:block;font-family:var(--display);font-stretch:112%;font-weight:700;letter-spacing:.08em;font-size:12px;color:var(--mute);text-transform:uppercase;margin-bottom:10px}
.dor b{display:block;font-family:var(--display);font-weight:600;font-size:19px;letter-spacing:-.02em;margin-bottom:8px}.dor p{margin:0;color:var(--ink2);font-size:15px;line-height:1.5}
/* entregas */
.ents{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.ent{display:flex;flex-direction:column;border-radius:28px;background:#fff;box-shadow:0 0 0 1.5px var(--ring);overflow:hidden}
.ent .pv{background:var(--soft);padding:22px;min-height:290px;display:flex;align-items:center;justify-content:center}
.ent .tx{padding:20px 22px 22px;display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line)}
.ent .tg{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:800}.ent .tg img{width:26px;height:26px;object-fit:contain}
.ent p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.5}
.mk{width:100%;max-width:300px;background:#fff;border-radius:16px;box-shadow:0 1px 2px rgba(0,0,0,.06),0 16px 30px -18px rgba(21,32,26,.35);font-size:13px}
.mkh{padding:12px 14px 10px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:baseline;gap:8px}.mkh b{font-size:13.5px}.mkh small{color:var(--mute);font-size:11.5px;font-weight:600}
.tb table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}.tb th{font-size:11px;color:var(--mute);font-weight:700;text-align:left;padding:8px 14px 6px}.tb td{padding:7px 14px;border-top:1px solid var(--line)}
.tb .r{text-align:right}.tb [data-dn]{color:#C23B3B;font-weight:800}.tb [data-up]{color:var(--verde-lab);font-weight:800;background:var(--mint)}.tb tr.tt td{font-weight:800;background:var(--mint)}
.ct2 .rw{display:flex;justify-content:space-between;gap:10px;padding:8px 14px;border-top:1px solid var(--line);font-variant-numeric:tabular-nums}.ct2 .rw:first-of-type{border-top:0}.ct2 .rw span{color:var(--ink2)}
.ct2 .fim{background:var(--mint);font-weight:800}.ct2 .fim b{color:var(--verde-lab)}.nt{margin:0;padding:9px 14px 12px;font-size:12px;color:var(--mute);font-weight:600;border-top:1px solid var(--line)}.nt.ok{color:var(--verde-lab)}
.wam{background:#EFEAE2;padding:10px}.wah{display:flex;align-items:center;gap:9px;padding:2px 2px 10px}.wav{width:28px;height:28px;border-radius:50%;background:#C9D4CC;display:grid;place-items:center;font-weight:800;font-size:12px}
.wah b{display:block;font-size:13px}.wah small{display:block;font-size:11px;color:#667781;font-weight:600}
.wam .bb{background:#fff;border-radius:12px;border-top-left-radius:3px;padding:9px 11px;line-height:1.45;box-shadow:0 1px 1px rgba(0,0,0,.08)}.wam .who{display:block;font-weight:800;font-size:12px;margin-bottom:2px}
.dias .dg{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;padding:10px}.dias .d{border-radius:10px;padding:8px 0;text-align:center;background:var(--soft)}
.dias .d small{display:block;font-size:11px;color:var(--mute);font-weight:700}.dias .d b{display:block;font-size:14px;margin:2px 0}.dias .d span{font-size:11px;color:#2D7FC1;font-weight:700}
.dias .d.hot{background:var(--mint2);box-shadow:inset 0 0 0 1.5px #9FE3B5}
.docm{padding:14px;transform:rotate(-1.2deg)}.docm .dh small{display:block;font-size:10.5px;letter-spacing:.08em;font-weight:800;color:var(--mute)}.docm .dh b{display:block;font-size:14px;margin:2px 0 10px}
.docm .ph{height:92px;border-radius:8px;background-size:cover;background-position:center;margin-bottom:8px}.docm .kv{display:flex;justify-content:space-between;gap:8px;font-size:12px;padding:5px 0;border-bottom:1px solid var(--line)}
.docm .kv span:first-child{color:var(--mute);font-weight:600}.docm .kv .ok{color:var(--verde-lab);font-weight:800}.docm .al{margin:9px 0;background:#FFF6DC;border-radius:8px;padding:7px 9px;font-size:12px;font-weight:700;color:#7A5B00}
.docm .ln{height:6px;border-radius:3px;background:var(--line);margin-top:6px}.docm .ln.s{width:60%}
.sld{display:grid;grid-template-columns:1.1fr .9fr;overflow:hidden;aspect-ratio:16/10}.sld .sl{padding:14px;display:flex;flex-direction:column;gap:4px}.sld .sl small{font-size:9.5px;letter-spacing:.06em;font-weight:800;color:var(--mute)}
.sld .sl b{font-family:var(--display);font-size:17px;letter-spacing:-.02em}.sld .big{margin-top:auto}.sld .big span{display:block;font-family:var(--display);font-weight:700;font-size:44px;line-height:1;color:var(--verde);letter-spacing:-.04em}.sld .big small{font-size:11px;color:var(--ink2);letter-spacing:0;font-weight:700}
.sld .sr2{background-size:cover;background-position:center}
.igp{overflow:hidden}.igh{display:flex;align-items:center;gap:8px;padding:9px 11px}.iga{width:24px;height:24px;border-radius:50%;background:var(--broto);display:grid;place-items:center;font-size:11px;font-weight:800}.igh b{font-size:12.5px}
.igi{aspect-ratio:1/1;background-size:cover;background-position:center;position:relative}.igt{position:absolute;left:10px;right:10px;bottom:10px;background:rgba(255,255,255,.94);border-radius:10px;padding:8px 10px}
.igt small{display:block;font-size:9.5px;font-weight:800;letter-spacing:.08em;color:var(--verde-lab)}.igt b{font-family:var(--display);font-size:14px;letter-spacing:-.01em;line-height:1.2}
.igc{margin:0;padding:9px 11px 11px;font-size:12px;line-height:1.4;color:var(--ink2)}
.reel{overflow:hidden}.reel .ph{height:120px;background-size:cover;background-position:center;position:relative}.reel .ph span{position:absolute;left:10px;right:10px;bottom:10px;background:rgba(255,255,255,.94);border-radius:10px;padding:7px 9px;font-weight:800;font-size:12.5px;line-height:1.25}
.reel ol{margin:0;padding:10px 14px 12px 14px;list-style:none;display:flex;flex-direction:column;gap:7px}.reel li{font-size:12px;line-height:1.4;color:var(--ink2)}.reel li b{display:block;font-size:10.5px;color:var(--verde-lab);letter-spacing:.04em}
.ctr .mkr{margin:8px 0;background:#FFF6DC;border-left:3px solid #E0B12E;border-radius:6px;padding:7px 9px;font-size:12px;font-weight:700;color:#7A5B00}.ctr .ft2{display:flex;justify-content:space-between;margin-top:10px;font-size:11px;font-weight:800;color:var(--mute)}
.hag{position:absolute;right:-18px;bottom:-26px;height:56%;width:auto;filter:drop-shadow(0 18px 18px rgba(21,32,26,.35));pointer-events:none}
/* faixa com foto */
.band{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,64px);align-items:center}
.band .ph{aspect-ratio:4/3.2;border-radius:32px;background-size:cover;background-position:center}
.peds{display:flex;flex-direction:column;gap:10px;margin-top:22px}
.ped{align-self:flex-start;max-width:100%;background:#D9FDD3;border-radius:14px;border-top-left-radius:4px;padding:11px 14px;font-size:15.5px;font-weight:600;color:#1F3A27;box-shadow:0 1px 1px rgba(0,0,0,.06)}
.ped:nth-child(even){margin-left:clamp(0px,4vw,40px)}
/* ajudantes */
.ags{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.ag{border-radius:24px;padding:20px 18px 18px;background:#fff;box-shadow:0 0 0 1.5px var(--ring);display:flex;flex-direction:column;gap:8px;position:relative;overflow:hidden}
.ag:before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:var(--c)}
.ag img{height:92px;width:auto;align-self:flex-start;filter:drop-shadow(0 10px 8px rgba(21,32,26,.16))}.ag b{font-family:var(--display);font-size:19px;font-weight:600;letter-spacing:-.02em}.ag p{margin:0;font-size:14.5px;color:var(--ink2);line-height:1.45}
/* passos */
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;counter-reset:s}
.step{border-radius:24px;padding:22px;background:var(--soft)}.step em{font-style:normal;font-family:var(--display);font-weight:700;font-size:13px;color:var(--verde-lab);letter-spacing:.06em}.step b{display:block;font-family:var(--display);font-size:19px;font-weight:600;letter-spacing:-.02em;margin:6px 0}.step p{margin:0;font-size:14.5px;color:var(--ink2);line-height:1.5}
/* lista */
.wait{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);border-radius:36px;overflow:hidden;box-shadow:0 0 0 1.5px var(--ring),0 40px 80px -40px rgba(21,32,26,.3)}
.wait .l{background:linear-gradient(165deg,#F3FDF6 0%,#E1F7E8 100%);border-right:1.5px solid #D3EEDC;padding:clamp(26px,4vw,44px);display:flex;flex-direction:column;gap:16px}
.wait .l p{margin:0;color:var(--ink2);font-size:16px;line-height:1.55}.soon{display:flex;flex-direction:column;gap:10px}.soon span{display:flex;align-items:center;gap:10px;font-weight:600}
.soon svg{flex:none;width:14px;height:14px;padding:4px;border-radius:50%;background:var(--verde);color:#fff;box-sizing:content-box}
.wait .r{background:#fff;padding:clamp(26px,4vw,44px);display:flex;flex-direction:column;gap:14px;justify-content:center}
.f{display:flex;flex-direction:column;gap:12px}.f label{display:flex;flex-direction:column;gap:7px;font-size:12.5px;font-weight:800;letter-spacing:.06em;color:var(--mute);text-transform:uppercase}
.f input{border:0;border-radius:16px;background:var(--soft);box-shadow:0 0 0 1.5px var(--ring);padding:15px 16px;font-weight:600;font-size:16px;color:var(--ink);letter-spacing:0;text-transform:none;outline:0}
.f input:focus{box-shadow:0 0 0 2.5px var(--broto);background:#fff}.f input.erro{box-shadow:0 0 0 2px #D64545}.f .btn{margin-top:4px;width:100%}.f .btn:disabled{opacity:.6}
.isca{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}.fmsg{margin:0;font-size:14px;font-weight:700;color:#C23B3B}.fmsg:empty{display:none}
.ok{display:none;flex-direction:column;gap:12px}.ok b{font-family:var(--display);font-weight:600;font-size:28px;letter-spacing:-.03em}.ok p{margin:0;color:var(--ink2);line-height:1.5}.done .f,.done .rh{display:none}.done .ok{display:flex}
.rh h3{font-size:24px}.rh p{margin:6px 0 0;color:var(--mute);font-size:14.5px}
/* perguntas */
.faq{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
.faq details{border-radius:20px;box-shadow:0 0 0 1.5px var(--ring);background:#fff}.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:18px 20px;font-weight:700;font-size:15.5px}
.faq summary::-webkit-details-marker{display:none}.faq summary i{font-style:normal;flex:none;width:26px;height:26px;border-radius:50%;background:var(--soft);display:grid;place-items:center;transition:transform .2s}.faq details[open] summary i{transform:rotate(45deg)}
.faq p{margin:0;padding:0 20px 18px;color:var(--ink2);line-height:1.55;font-size:15px}
/* outras */
.outras{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.outra{display:flex;align-items:center;gap:14px;text-decoration:none;border-radius:22px;padding:12px;background:#fff;box-shadow:0 0 0 1.5px var(--ring);transition:box-shadow .2s}.outra:hover{box-shadow:0 0 0 1.5px #BFE6CB}
.outra .th{width:64px;height:64px;border-radius:14px;background-size:cover;background-position:center;flex:none}.outra b{display:block;font-size:15.5px}.outra small{font-size:13px;color:var(--mute);font-weight:600}
.outra.cur{background:var(--mint);box-shadow:0 0 0 1.5px #C6EFD3}
footer{padding-block:36px calc(36px + env(safe-area-inset-bottom,0px));border-top:1px solid var(--line)}footer .in{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;color:var(--mute);font-size:14px;font-weight:600}footer nav{display:flex;gap:18px;flex-wrap:wrap}footer a{text-decoration:none}
.rv{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}.rv.on{opacity:1;transform:none}.nojs .rv{opacity:1;transform:none}
@media (max-width:980px){.hg,.band{grid-template-columns:minmax(0,1fr)}.hp{margin:10px 0 40px}.wa{left:12px}.ents,.ags{grid-template-columns:repeat(2,minmax(0,1fr))}.dores,.steps,.outras{grid-template-columns:minmax(0,1fr)}.band .ph{order:-1}}
@media (max-width:640px){.ents,.ags{grid-template-columns:minmax(0,1fr)}.wait{grid-template-columns:minmax(0,1fr);border-radius:28px}.wait .l{border-right:0;border-bottom:1.5px solid #D3EEDC}
 .hag{height:46%;right:-6px;bottom:-14px} .hp .ph,.band .ph{border-radius:24px}.hp .ph{aspect-ratio:1/1.08}.hp{margin-bottom:96px}.wa{width:calc(100% - 24px);bottom:-84px}.cta .btn{width:100%}.ags{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.ag{padding:16px 14px}.ag img{height:70px}.ag b{font-size:17px}.ag p{font-size:13.5px}
 .ent .pv{min-height:0;padding:20px 16px}.crumb{margin-bottom:16px}}
"""

JS = """
document.documentElement.classList.remove('nojs');
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const URL_PLANILHA="https://script.google.com/macros/s/AKfycbwFZGzhpXW8fAUdNYUvxYoQhVjRmIm-I8Qynyp70Pi396rTL8psG7z0NyNCm7HUa7TQ/exec";
const $=id=>document.getElementById(id);const wf=$('wf'),fw=$('fw'),fn=$('fn'),fc=$('fc'),fm=$('fmsg');
fw.addEventListener('input',()=>{fw.classList.remove('erro');fm.textContent='';if(fw.value.trim().startsWith('+'))return;let d=fw.value.replace(/\\D/g,'').slice(0,11);fw.value=d.length>6?`(${d.slice(0,2)}) ${d.slice(2,d.length-4)}-${d.slice(-4)}`:d.length>2?`(${d.slice(0,2)}) ${d.slice(2)}`:d});
fn.addEventListener('input',()=>{fn.classList.remove('erro');fm.textContent=''});
wf.addEventListener('submit',async e=>{e.preventDefault();if(!fn.value.trim()){fn.classList.add('erro');fm.textContent='Digite o seu nome.';fn.focus();return}
 const dig=fw.value.replace(/\\D/g,'');const ok=fw.value.trim().startsWith('+')?dig.length>=8:dig.length>=10;if(!ok){fw.classList.add('erro');fm.textContent='Digite o seu WhatsApp com DDD.';fw.focus();return}
 if(wf.site.value)return;$('fb').disabled=true;const q=new URLSearchParams(location.search);
 try{await fetch(URL_PLANILHA,{method:'POST',mode:'no-cors',body:new URLSearchParams({nome:fn.value.trim(),whatsapp:fw.value.trim(),cidade:fc.value.trim(),origem:q.get('origem')||q.get('utm_source')||ORIGEM,campanha:q.get('utm_campaign')||'pagina-nicho'})})}catch(_){}
 $('wait').classList.add('done')});
"""


def pagina(slug, d):
    e = html.escape
    chat_o, chat_ag, chat_r = d["chat"]
    dores = "".join(f'<div class="dor rv"><small>Hoje</small><b>{t}</b><p>{p}</p></div>' for t, p in d["dor"])
    ents = "".join(
        f'<div class="ent rv"><div class="pv">{mk}</div><div class="tx"><span class="tg" style="color:{TXT[k]}"><img src="/img/{k}.webp" alt="" loading="lazy">{nome(k)}</span>'
        f'<h3>{t}</h3><p>{p}</p></div></div>' for k, t, p, mk in d["entregas"])
    peds = "".join(f'<div class="ped">"{p}"</div>' for p in d["pedidos"])
    ags = "".join(f'<div class="ag rv" style="--c:{COR[k]}"><img src="/img/{k}.webp" alt="" loading="lazy"><b>{nome(k)}</b><p>{t}</p></div>' for k, t in d["ajudantes"])
    faq = "".join(f'<details><summary>{q}<i aria-hidden="true">+</i></summary><p>{a}</p></details>' for q, a in d["faq"])
    cat = d["cat"]; cat_nome, lista = CATS[cat]
    i0 = lista.index(slug); viz = [lista[(i0 + j) % len(lista)] for j in range(1, len(lista))][:3]
    outras = "".join(
        f'<a class="outra" href="/{cat}/{s}"><span class="th" style="background-image:url({N[s]["foto"]})"></span><span><b>{ROT[s]}</b><small>Ver a página</small></span></a>'
        for s in viz)
    hag = f'<img class="hag" src="/img/{d["ag"]}.webp" alt="" style="--c:{COR[d["ag"]]}">' if d.get("ag") else ""
    return f"""<!doctype html>
<html lang="pt-BR" class="nojs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(d["titulo"])} · 10 ajudantes no WhatsApp</title>
<meta name="description" content="{e(d["desc"])}">
<meta property="og:title" content="{e(d["titulo"])}">
<meta property="og:description" content="{e(d["desc"])}">
<meta property="og:image" content="{d["foto"]}">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..800&family=Manrope:wght@400..800&display=swap">
<link rel="preload" as="image" href="{d["foto"]}">
<style>{CSS}{MENU_CSS}</style>
</head>
<body>
<header class="nav" id="nav">
  <div class="in">
    <a class="logo" href="/paginainicial" aria-label="Germo, página inicial"><span class="gm" aria-hidden="true">{LOGO}</span><span class="wm">germo<b>.br</b></span></a>
    {links_html()}
    <span class="sp"></span>
    {burger_html()}
    <a class="ncta" href="#lista"><i aria-hidden="true"></i>Entrar na lista<span aria-hidden="true">{ARR}</span></a>
  </div>
  {panel_html(atual=slug)}
</header>

<main>
<section class="hero">
  <div class="in">
    <div class="crumb"><a href="/paginainicial">Germo</a><i>/</i><span>{cat_nome}</span><i>/</i><span>{ROT[slug]}</span></div>
    <div class="hg">
      <div class="ht">
        <span class="eyebrow">{d["eyebrow"]}</span>
        <h1>{d["h1"]}</h1>
        <p class="lead">{d["lead"]}</p>
        <div class="cta"><a class="btn pr" href="#lista">Entrar na lista de espera <span class="ar" aria-hidden="true">→</span></a><a class="btn ol" href="#pronto">Ver o que fica pronto</a></div>
        <div class="chk"><span>{CHK}Não instale nada</span><span>{CHK}Sem login e senha</span><span>{CHK}Somente o seu WhatsApp</span></div>
      </div>
      <div class="hp">
        <div class="ph" role="img" aria-label="{e(d["foto_alt"])}" style="background-image:url({d["foto"]})"></div>{hag}
        <div class="wa" aria-label="Exemplo de conversa no WhatsApp da Germo">
          <div class="wh"><img src="/img/{chat_ag}.webp" alt="">Germo · WhatsApp</div>
          <div class="b o">{chat_o}</div>
          <div class="b i"><span class="who" style="color:{TXT[chat_ag]}">{nome(chat_ag)}</span>{chat_r}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="in">
    <div class="head rv"><span class="eyebrow">O seu dia a dia</span><h2>{d["dor_t"]}</h2></div>
    <div class="dores">{dores}</div>
  </div>
</section>

<section id="pronto" style="padding-top:0">
  <div class="in">
    <div class="head rv"><span class="eyebrow">O que fica pronto</span><h2>Você pede no WhatsApp. <span class="g">Recebe assim.</span></h2><p class="lead">Exemplos do trabalho que os ajudantes devolvem para quem vive essa rotina.</p></div>
    <div class="ents">{ents}</div>
  </div>
</section>

<section style="background:var(--soft)">
  <div class="in band">
    <div class="ph rv" role="img" aria-label="{e(d["foto2_alt"])}" style="background-image:url({d["foto2"]})"></div>
    <div class="rv">
      <span class="eyebrow">Como você pede</span>
      <h2 style="margin-top:12px">{d["pedidos_t"]}</h2>
      <p class="lead" style="margin-top:14px">Por áudio, foto ou mensagem. Sem palavra difícil e sem escolher qual ajudante chamar.</p>
      <div class="peds">{peds}</div>
    </div>
  </div>
</section>

<section>
  <div class="in">
    <div class="head rv"><span class="eyebrow">Os ajudantes que mais vão trabalhar para você</span><h2>Uma equipe <span class="g">no mesmo WhatsApp.</span></h2><p class="lead">Os 10 ajudantes ficam no mesmo número. Para a sua rotina, estes são os que mais entram em ação.</p></div>
    <div class="ags">{ags}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="in">
    <div class="head rv"><span class="eyebrow">Como começa</span><h2>3 passos, <span class="g">nenhum aplicativo.</span></h2></div>
    <div class="steps">
      <div class="step rv"><em>PASSO 1</em><b>Entre na lista</b><p>Deixe o seu nome e o seu WhatsApp aqui embaixo. Leva 10 segundos.</p></div>
      <div class="step rv"><em>PASSO 2</em><b>Receba o acesso</b><p>No lançamento, a Germo chama você no WhatsApp com a oferta da lista.</p></div>
      <div class="step rv"><em>PASSO 3</em><b>Mande o primeiro pedido</b><p>Um áudio, uma foto ou uma mensagem. O ajudante certo devolve pronto.</p></div>
    </div>
  </div>
</section>

<section id="lista" style="padding-top:0">
  <div class="in">
    <div class="wait rv" id="wait">
      <div class="l">
        <span class="eyebrow">Lista de espera</span>
        <h2 style="font-size:clamp(28px,3vw,38px)">Seja um dos primeiros a ter os 10 ajudantes.</h2>
        <p>Nós vamos abrir aos poucos. A lista define quem entra primeiro.</p>
        <div class="soon"><span>{CHK}Acesso antes do lançamento aberto</span><span>{CHK}Oferta de lançamento só para a lista</span><span>{CHK}Aviso direto no seu WhatsApp</span></div>
      </div>
      <div class="r">
        <div class="rh"><h3>Deixe o seu contato</h3><p>Leva 10 segundos. Nós só usamos para avisar sobre a Germo.</p></div>
        <form class="f" id="wf" novalidate>
          <label for="fn">Nome<input id="fn" name="nome" autocomplete="name" placeholder="Seu nome"></label>
          <label for="fw">WhatsApp com DDD<input id="fw" name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" placeholder="(41) 99999-0000"></label>
          <label for="fc">Cidade<input id="fc" name="cidade" autocomplete="address-level2" placeholder="Ex.: Castro, PR"></label>
          <input class="isca" name="site" tabindex="-1" autocomplete="off" aria-hidden="true">
          <p class="fmsg" id="fmsg" role="status" aria-live="polite"></p>
          <button class="btn pr" type="submit" id="fb">Entrar na lista de espera <span class="ar" aria-hidden="true">→</span></button>
        </form>
        <div class="ok" role="status"><b>Pronto, você está na lista.</b><p>Nós vamos te avisar no WhatsApp assim que a Germo abrir, com a oferta de lançamento.</p><a class="btn ol" href="/paginainicial">Conhecer a Germo</a></div>
      </div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="in">
    <div class="head rv" style="margin-inline:auto;text-align:center;align-items:center"><span class="eyebrow">Perguntas</span><h2>Dúvidas de quem é <span class="g">da área.</span></h2></div>
    <div class="faq rv">{faq}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="in">
    <div class="head rv"><span class="eyebrow">Veja também</span><h2 style="font-size:clamp(26px,3vw,34px)">{ {"para":"A Germo também é para…","tarefa":"Outras tarefas que a Germo resolve","ajudante":"Conheça outros ajudantes"}[cat] }</h2></div>
    <div class="outras rv">{outras}</div>
  </div>
</section>
</main>

<footer>
  <div class="in">
    <span class="wm" style="font-size:17px">germo<b>.br</b></span>
    <nav aria-label="Rodapé"><a href="/paginainicial">Página inicial</a><a href="https://instagram.com/germo.br" target="_blank" rel="noopener">Instagram</a><a href="https://wa.me/5541988840707?text=Ol%C3%A1%21%20Preciso%20de%20ajuda%20com%20a%20Germo." target="_blank" rel="noopener">Central de Ajuda</a></nav>
    <span>germo.br · Todos os direitos reservados.</span>
  </div>
</footer>
<script>const ORIGEM="{cat}-{slug}";{JS}{MENU_JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for slug, d in N.items():
        pasta = os.path.join(raiz, d["cat"], slug)
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, "index.html"), "w") as f:
            f.write(pagina(slug, d))
        print("ok", slug)
