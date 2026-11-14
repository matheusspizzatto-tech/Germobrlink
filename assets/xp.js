/* Experiência ao vivo dos 10 ajudantes: áudio do pedido, ajudante trabalhando dentro do arquivo e entrega no WhatsApp */
(function(){
const CF='https://d2ol7oe51mr4n9.cloudfront.net/user_2vVA8WvBFtZCaqwnis3S3BiJPUC/';
const AU='https://d8j0ntlcm91z4.cloudfront.net/user_2vVA8WvBFtZCaqwnis3S3BiJPUC/hf_20261114_';
const RM=matchMedia('(prefers-reduced-motion:reduce)').matches, SP=RM?0.12:1;
const brl=v=>v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const FILE=(c,t,n,s)=>`<div class="xp-file"><i style="background:${c}">${t}</i><span><b>${n}</b><small>${s}</small></span></div>`;

/* cada ajudante: áudio, fala, documento e o trabalho dentro dele */
const S={
planilha:{a:'155845_671c25df-e8d1-418b-9ea2-1bedc6104b85.mp3',d:4.8,f:'Ô Germo, monta pra mim a planilha dos salários da equipe desse mês.',
 doc:()=>`<div class="xd"><div class="xd-h" style="background:#1D7A45"><i style="color:#1D7A45">XLS</i>Salários da equipe.xlsx<small>novembro</small></div><table><thead><tr><th>Funcionário</th><th>Função</th><th class="xn">Salário</th></tr></thead><tbody>${[0,1,2,3].map(i=>`<tr data-r="${i}"><td></td><td></td><td class="xn"></td></tr>`).join('')}<tr class="xtt"><td>Total</td><td></td><td class="xn" id="xt"></td></tr><tr class="xfg"><td>FGTS 8%</td><td>a recolher</td><td class="xn" id="xf"></td></tr></tbody></table></div>`,
 async run(x){const R=[['João Silva','Tratorista',2900],['Maria Souza','Ordenha',2450],['Pedro Lima','Operador',3100],['Ana Costa','Escritório',2700]];
  for(let i=0;i<4;i++){const tr=x.q(`tr[data-r="${i}"]`),td=tr.children;await x.hop(td[0],{dx:-72});x.type(td[0],R[i][0],18);await x.type(td[1],R[i][1],18);await x.hop(td[2],{dx:30});await x.count(td[2],R[i][2],380)}
  const t=x.q('#xt');await x.hop(t,{dx:30});await x.squash();await x.count(t,11150,600);const f=x.q('#xf');await x.hop(f,{dx:30});await x.count(f,892,450)},
 out:()=>`<span class="xwho">planilha</span>${FILE('#1D7A45','XLS','Salários da equipe.xlsx','Planilha · 12 KB')}Pronto! 4 funcionários, R$ 11.150,00 no mês. Já separei os 8% de FGTS: R$ 892,00.`},

clima:{a:'155845_f355e63e-e3c6-474e-97cf-09aa7ed6757d.mp3',d:5.5,f:'Germo, vai chover amanhã aqui na fazenda? Preciso saber se dá pra colher.',
 doc:()=>`<div class="xd"><div class="xd-h" style="background:#16A898"><i style="color:#16A898">☁</i>Fazenda Boa Vista · amanhã<small>previsão por talhão</small></div><div class="xm"><svg viewBox="0 0 440 200" preserveAspectRatio="none"><path d="M20 30 L210 18 L220 96 L28 104Z" fill="#C9E4B4" stroke="#fff" stroke-width="3"/><path d="M210 18 L420 26 L414 100 L220 96Z" fill="#B7DB9E" stroke="#fff" stroke-width="3"/><path d="M28 104 L220 96 L226 184 L34 186Z" fill="#D3E9BF" stroke="#fff" stroke-width="3"/><path d="M220 96 L414 100 L408 182 L226 184Z" fill="#A9D28D" stroke="#fff" stroke-width="3"/></svg>${[['T1',22,26],['T2',52,26],['T3',22,66],['T4',52,66]].map(([n,l,t],i)=>`<span class="xtl" style="left:${l-14}%;top:${t-16}%">${n}</span><span class="xrn" data-i="${i}" style="left:calc(${l}% - 28px);top:calc(${t}% - 23px)"></span><span class="xmm" data-i="${i}" style="left:calc(${l}% - 22px);top:calc(${t}% + 18px)">${[38,42,40,36][i]} mm</span>`).join('')}</div><div class="xh">${['12h','13h','14h','15h','16h','17h'].map((h,i)=>`<span data-h="${i}">${h}<b>${i<3?'—':[18,14,8][i-3]+' mm'}</b></span>`).join('')}</div></div>`,
 async run(x){for(let i=0;i<4;i++){const r=x.q(`.rn[data-i="${i}"]`);await x.hop(r,{dy:-6});r.classList.add('on');x.q(`.mm[data-i="${i}"]`).classList.add('on');await x.wait(260)}
  const hs=x.qa('.xh span');for(let i=0;i<6;i++){await x.hop(hs[i],{dy:-2,dur:260});if(i!==2)hs[i].classList.add(i<2?'xok':'xrain')}await x.squash()},
 out:()=>`<span class="xwho">clima</span>Amanhã chove forte a partir das 15h, cerca de 40 mm na fazenda. Dá para colher o talhão 2 até as 13h.<br><span class="chipx">Amanhã · 15h · 40 mm</span>`},

campo:{a:'155903_3e3f5e02-947c-42d4-b57a-6719437c47ea.mp3',d:5.1,f:'Germo, terminei a visita no talhão 4. Faz o relatório com essas fotos pra mim.',
 doc:()=>`<div class="xd"><div class="xd-h" style="background:#C8402F"><i style="color:#C8402F">PDF</i>Relatório de visita · Talhão 4<small>soja · R3</small></div><div class="xp-photos">${['848e5dee-a7b6-4e07-91ac-dc4f0a1bb466.webp','0d2389ca-1b73-444c-be28-840b2c688cec.jpg','e75f3f04-f76f-48ee-9b08-b74b95da2532.webp'].map(p=>`<span data-p="${CF+p}"></span>`).join('')}</div><div class="xln"></div><div class="xln"></div><div class="xln xsh"></div><div class="xrec">Recomendação: monitorar ferrugem no talhão 4 e voltar em 7 dias</div><div class="xsig"><span>Técnico responsável</span><svg width="110" height="30" viewBox="0 0 110 30"><path d="M4 22c8-14 14-16 16-6s6 10 12-4 10-8 10 2 8 8 14-6 10 2 16 4 18-2 12 4 16 0" fill="none" stroke="#24408E" stroke-width="2.2" stroke-linecap="round"/></svg></div></div>`,
 async run(x){const ph=x.qa('.xp-photos span');for(const p of ph){await x.hop(p,{dy:-4});p.style.backgroundImage=`url(${p.dataset.p})`;p.classList.add('on');await x.wait(200)}
  for(const l of x.qa('.xln')){await x.hop(l,{dx:40,dur:280});l.classList.add('on');await x.wait(250)}
  const r=x.q('.xrec');await x.hop(r,{dx:60});r.classList.add('on');await x.wait(350);const s=x.q('.xsig');await x.hop(s.querySelector('svg'),{});s.classList.add('on');await x.wait(900)},
 out:()=>`<span class="xwho">campo</span>${FILE('#C8402F','PDF','Relatorio_Talhao4.pdf','PDF · 3 páginas')}Relatório pronto, com as 3 fotos e a recomendação. É só mandar para o produtor.`},

agronomo:{a:'155845_10c2d76d-6fcd-4a60-b9f3-87003b35ce0a.mp3',d:4.1,f:'Apareceu essa mancha na folha da soja. O que pode ser?',
 doc:()=>`<div class="xd"><div class="xleaf" style="background-image:url(${CF}0d2389ca-1b73-444c-be28-840b2c688cec.jpg)">${[[30,34],[58,52],[44,70]].map(([l,t],i)=>`<span class="xring" data-i="${i}" style="left:calc(${l}% - 21px);top:calc(${t}% - 21px)"></span>`).join('')}</div><div class="xdx"><b>Causa mais provável: ferrugem asiática, no início</b><p>Olhe o verso da folha: pontinhos em relevo confirmam. Chame o seu agrônomo hoje, antes de aplicar qualquer produto.</p></div></div>`,
 async run(x){for(const r of x.qa('.xring')){await x.hop(r,{dy:8});await x.wait(250);r.classList.add('on');await x.wait(300)}const d=x.q('.xdx');await x.hop(d,{dx:-120});d.classList.add('on');await x.squash();await x.wait(700)},
 out:()=>`<span class="xwho">agrônomo</span>Pelas manchas e pelas pústulas no verso, parece ferrugem asiática no início. Confirme com o seu agrônomo hoje: quanto antes, melhor.<span class="btn2">Falar com um agrônomo parceiro</span>`},

vendas:{a:'155845_ac27156e-c263-451f-b880-f43eebbad44a.mp3',d:4.0,f:'Recebi três propostas pela soja. Qual tá pagando melhor?',
 doc:()=>`<div class="xv">${[['Cooperativa',128,0,'frete incluso'],['Trading',134,5,'frete: R$ 5,00'],['Cerealista',131.5,1,'frete: R$ 1,00']].map(([n,v,f,t],i)=>`<div data-i="${i}" data-v="${v-f}"><small>${n}</small><b>R$ ${brl(v)}</b><span class="xfr">${t}</span><div class="xlq">líquido por saca<strong>R$ —</strong></div>${i===2?'<span class="xstp">Melhor</span>':''}</div>`).join('')}</div>`,
 async run(x){for(const c of x.qa('.xv>div')){await x.hop(c,{dy:-2});const l=c.querySelector('.xlq');l.classList.add('on');await x.count(l.querySelector('strong'),+c.dataset.v,420,'R$ ');await x.wait(200)}
  const b=x.q('.xv>div[data-i="2"]');await x.hop(b,{dy:-10});await x.squash();b.classList.add('xbest');b.querySelector('.xstp').classList.add('on');await x.wait(700)},
 out:()=>`<span class="xwho">vendas</span>${FILE('#B88F0E','PDF','Comparativo_propostas.pdf','PDF · 1 página')}A melhor é a Cerealista: R$ 130,50 por saca já sem o frete. A Trading parece maior, mas o frete come R$ 5,00.`},

viral:{a:'155903_c797f287-d3fc-448b-8d5a-9f5d49320c4f.mp3',d:3.3,f:'Germo, me dá um roteiro de reels pra mostrar a colheita do milho.',
 doc:()=>`<div class="xr"><div class="xfr" style="background-image:url(${CF}8d1cbb5f-96f0-49d8-958e-0442b9b5b015.webp)"><em>Ninguém mostra isso da colheita do milho</em></div><ol>${[['0 a 3 s','Gancho: "Ninguém mostra isso da colheita do milho."'],['Cena 1','Colheitadeira entrando no talhão'],['Cena 2','Grão caindo na caçamba, em câmera lenta'],['Cena 3','Você contando quantas sacas deu'],['Final','"Comenta MILHO que eu te conto o resto."']].map(([a,b])=>`<li><b>${a}</b>${b}</li>`).join('')}</ol></div>`,
 async run(x){const li=x.qa('.xr li');for(let i=0;i<li.length;i++){await x.hop(li[i],{dx:-90,dur:300});li.forEach(l=>l.classList.remove('xcur'));li[i].classList.add('on','xcur');if(i===0)x.q('.xr em').classList.add('on');await x.wait(420)}li.forEach(l=>l.classList.remove('xcur'));await x.squash()},
 out:()=>`<span class="xwho">viral</span>${FILE('#D9590E','PDF','Roteiro_reels_colheita.pdf','PDF · 2 páginas')}Roteiro pronto: gancho nos 3 primeiros segundos, 4 cenas e a legenda para postar.`},

vitrine:{a:'155845_d4502e72-46c8-4499-bc38-6b2d222fb4af.mp3',d:4.0,f:'Faz um post pra eu vender os morangos da colheita de hoje no Instagram.',
 doc:()=>`<div class="xig"><div class="xpo" style="background-image:url(${CF}8b42cec8-a51b-44e3-b668-79895802a247.jpg)"><span class="xpr">1 kg · R$ 25</span><b id="xpt"></b><span class="xlk2" id="xlk">♥ 0</span></div><div class="xcap"><small>LEGENDA PRONTA</small><span id="xcap"></span><br><span class="xhs2" id="xhs"></span></div></div>`,
 async run(x){const t=x.q('#xpt');await x.hop(t,{dy:-30});await x.type(t,'Colheita de hoje, do pé para a sua mesa.',22);const p=x.q('.xpr');await x.hop(p,{dy:-4});p.classList.add('on');await x.wait(300);
  const c=x.q('#xcap');await x.hop(c,{dx:-60});await x.type(c,'Colhemos hoje cedo, no ponto certo. Caixa de 1 kg por R$ 25, entrega no sábado.',14);await x.type(x.q('#xhs'),'#morangos #docampoparaamesa',16);
  const lk=x.q('#xlk');await x.hop(lk,{dy:-2});const t0=performance.now();await new Promise(r=>{const f=n=>{const k=Math.min(1,(n-t0)/(700*SP||1));lk.textContent='♥ '+Math.round(248*k);k<1?requestAnimationFrame(f):r()};requestAnimationFrame(f)})},
 out:()=>`<span class="xwho">vitrine</span>${FILE('#2585E0','IMG','Post_morangos.png','Imagem · 1080 × 1350')}Post pronto com a legenda e as hashtags. É só publicar.`},

apresenta:{a:'155903_bc1053df-c90d-4af2-947b-76aaab20d976.mp3',d:5.0,f:'Monta uma apresentação do meu estágio na cooperativa, com 8 slides.',
 doc:()=>`<div class="xs"><div class="xfr"><div class="xsl" data-s="0"><small>ESTÁGIO · 2026</small><b>Estágio na Cooperativa Agrária</b></div><div class="xsl" data-s="1"><small>RESULTADOS</small><b>Produtividade por talhão</b><div class="xbars"><i data-h="48"></i><i data-h="62"></i><i data-h="55"></i><i data-h="80"></i><i data-h="92"></i></div></div><div class="xsl" data-s="2"><small>FIM</small><b>Obrigada!</b></div></div><div class="xth">${Array.from({length:8},()=>'<span></span>').join('')}</div></div>`,
 async run(x){const sl=x.qa('.xsl'),th=x.qa('.xth span'),fr=x.q('.xfr');let k=0;
  for(let s=0;s<3;s++){await x.hop(fr,{dx:150,dy:-6});sl.forEach(e=>e.classList.remove('on'));sl[s].classList.add('on');if(s===1){await x.wait(250);x.qa('.xbars i').forEach(b=>b.style.height=b.dataset.h+'%')}
   const n=s<2?3:2;for(let j=0;j<n;j++){await x.hop(th[k],{dur:220});th[k++].classList.add('on')}await x.wait(350)}await x.squash()},
 out:()=>`<span class="xwho">apresenta</span>${FILE('#6846F0','PPT','Estagio_Cooperativa.pptx','Apresentação · 8 slides')}Pronto: capa, objetivos, atividades, resultados e agradecimentos, em 8 slides.`},

juridico:{a:'155912_03427bc5-ce0a-4b5e-b5e9-7c0a33a4c354.mp3',d:3.8,f:'Analisa esse contrato de arrendamento e me fala o que tá faltando.',
 doc:()=>`<div class="xd xc"><div class="xd-h" style="background:#8E2443"><i style="color:#8E2443">PDF</i>Contrato de arrendamento<small>6 páginas</small></div>${[['1. Partes e propriedade',1],['2. Área: 48 ha, talhões 1 a 3',1],['3. Prazo: 3 anos',1],['4. Pagamento: 12 sacas por hectare',1],['5. Renovação do contrato',0],['6. Quem paga o ITR',0]].map(([t,o])=>`<div class="xcl" data-o="${o}"><span>${t}</span><em>${o?'ok':'falta'}</em></div>`).join('')}</div>`,
 async run(x){for(const c of x.qa('.xcl')){await x.hop(c,{dx:120,dur:280});c.classList.add('xscan');await x.wait(220);c.classList.remove('xscan');c.classList.add(c.dataset.o==='1'?'xok':'xbad');if(c.dataset.o==='0'){await x.squash()}await x.wait(120)}await x.wait(400)},
 out:()=>`<span class="xwho">jurídico</span>${FILE('#8E2443','PDF','Analise_contrato.pdf','PDF · 2 páginas')}Faltam 2 cláusulas: a renovação e quem paga o ITR. Peça para incluir antes de assinar.<span class="btn2">Falar com um advogado parceiro</span>`},

contabil:{a:'155913_78c847c6-725a-449a-884d-8b3905b2f358.mp3',d:3.6,f:'Organiza as notas do mês no livro caixa pro meu contador.',
 doc:()=>`<div class="xk"><div class="xpile">${[['03/11','Diesel','1.240,00'],['07/11','Adubo','8.900,00'],['10/11','Peças','760,00'],['15/11','Venda de leite','14.320,00'],['18/11','Defensivo','2.150,00']].map(([d,n,v],i)=>`<div class="xnt" data-i="${i}" data-d="${d}" data-n="${n}" data-v="${v}" style="top:${8+i*34}px;z-index:${10-i}"><b>${n}</b>${d} · R$ ${v}</div>`).join('')}</div><div class="xd"><div class="xd-h" style="background:#24408E"><i style="color:#24408E">XLS</i>Livro caixa · novembro</div><table><thead><tr><th>Data</th><th>Lançamento</th><th class="xn">Valor</th></tr></thead><tbody id="xkb"></tbody></table></div></div>`,
 async run(x){const tb=x.q('#xkb');for(const n of x.qa('.xnt')){await x.hop(n,{dx:20,dy:6,dur:280});await x.wait(150);if(n.dataset.i==='2'){n.classList.add('xflag');await x.squash();await x.wait(350);continue}
   n.classList.add('xgone');const tr=document.createElement('tr');tr.className='new';const ent=n.dataset.n==='Venda de leite';tr.innerHTML=`<td>${n.dataset.d}</td><td>${n.dataset.n}</td><td class="xn" style="color:${ent?'#0F8A3D':'#15201A'}">${ent?'+':'−'} ${n.dataset.v}</td>`;tb.appendChild(tr);await x.hop(tr.children[1],{dur:300});await x.wait(150)}},
 out:()=>`<span class="xwho">contábil</span>${FILE('#24408E','XLS','Livro_caixa_novembro.xlsx','Planilha · 1 aba')}4 notas lançadas no livro caixa. 1 nota veio sem o seu CPF: peça a correção ao fornecedor.`}
};

const audio=new Audio();audio.preload='none';
let run=0,state=null;
const wait=ms=>new Promise(r=>setTimeout(r,ms*SP));

function stop(){run++;try{audio.pause()}catch(e){}if(state){state.root.classList.remove('run');state.big&&state.big.classList.remove('away');state.ag.classList.remove('on','work')}}

function mount(root,ag,big,auto){
  stop();const k=ag.k,s=S[k];if(!s){root.innerHTML='';return}
  const color=ag.t;root.style.setProperty('--ac',color);
  const words=s.f.split(' ');
  const bars=Array.from({length:30},(_,i)=>`<i style="height:${6+Math.round(Math.abs(Math.sin(i*1.7+k.length)+Math.sin(i*.6))*8)}px"></i>`).join('');
  root.innerHTML=`<div class="xp-req"><div class="xp-row"><button class="xp-play" type="button" aria-label="Ouvir o pedido e ver o ${esc(ag.n)} trabalhar"><svg width="15" height="15" viewBox="0 0 24 24" fill="#0A0C0B"><path d="M7 4.5v15l13-7.5z"/></svg></button><span class="xp-wv" aria-hidden="true">${bars}</span><span class="xp-du">0:0${Math.round(s.d)}</span></div><p class="xp-tr">"${words.map(w=>`<span>${esc(w)}</span>`).join(' ')}"</p></div>
  <div class="xp-stage" aria-hidden="true"><div class="xp-doc">${s.doc()}</div><img class="xp-ag" src="/img/${k}.webp" alt=""><span class="xp-idle">Toque no play e veja o ${esc(ag.n)} trabalhar</span></div>
  <div class="xp-dock" aria-live="polite"><span class="xp-ph">O arquivo chega aqui, no seu WhatsApp</span></div>
  <div class="xp-end"><span>Esse foi 1 pedido. Toque em outro ajudante.</span><button type="button" class="xp-again">Ver de novo</button></div>`;
  root.classList.remove('run','done');
  state={root,ag:root.querySelector('.xp-ag'),big,s,k,n:ag.n};
  root.querySelector('.xp-play').addEventListener('click',()=>start());
  root.querySelector('.xp-again').addEventListener('click',()=>mount(root,ag,big,true));
  if(auto)start();
}

async function start(){
  if(!state)return;const st=state,{root,ag,s}=st;const id=++run;const alive=()=>id===run;
  if(root.classList.contains('run'))return;
  root.classList.remove('done');root.classList.add('run');window._lpPause&&window._lpPause();
  {const r=root.getBoundingClientRect();if(r.top>innerHeight*0.55||r.bottom<0)root.scrollIntoView({behavior:RM?'auto':'smooth',block:'start'})}
  const stage=root.querySelector('.xp-stage'),doc=root.querySelector('.xp-doc');
  const wv=[...root.querySelectorAll('.xp-wv i')],tw=[...root.querySelectorAll('.xp-tr span')],du=root.querySelector('.xp-du');
  const prog=t=>{const p=Math.min(1,t/s.d);wv.forEach((b,i)=>b.classList.toggle('on',i/wv.length<p));tw.forEach((w,i)=>w.classList.toggle('on',i/tw.length<p*1.1));du.textContent='0:0'+Math.min(9,Math.floor(t))};
  let played=false;
  try{audio.src=AU+s.a;audio.currentTime=0;await Promise.race([audio.play(),new Promise((_,j)=>setTimeout(()=>j(0),2500))]);played=true;if(isFinite(audio.duration)&&audio.duration>1)s.d=audio.duration}catch(e){}
  if(!alive())return;
  await new Promise(res=>{
    if(played){const h=()=>{if(!alive()){c();return res()}prog(audio.currentTime)},e=()=>{prog(s.d);c();res()},c=()=>{audio.removeEventListener('timeupdate',h);audio.removeEventListener('ended',e)};audio.addEventListener('timeupdate',h);audio.addEventListener('ended',e)}
    else{const t0=performance.now();const f=()=>{if(!alive())return res();const t=(performance.now()-t0)/1000/(SP||1);prog(t);t<s.d?requestAnimationFrame(f):res()};requestAnimationFrame(f)}
  });
  if(!alive())return;
  /* o ajudante sai do card e entra no arquivo */
  const A=st.ag,W=()=>A.offsetWidth||58,H=()=>A.offsetHeight||58;
  let pos={x:stage.clientWidth/2-W()/2,y:stage.clientHeight/2-H()/2};
  const set=(p,sc=1)=>{A.style.transform=`translate(${p.x}px,${p.y}px) scale(${sc})`};
  const rel=el=>{const a=el.getBoundingClientRect(),b=stage.getBoundingClientRect();return{x:a.left-b.left,y:a.top-b.top,w:a.width,h:a.height}};
  const x={
    q:sel=>doc.querySelector(sel),qa:sel=>[...doc.querySelectorAll(sel)],
    wait:ms=>alive()?wait(ms):Promise.resolve(),
    async hop(el,o={}){if(!alive()||!el)return;const r=rel(el);const to={x:Math.max(-6,Math.min(stage.clientWidth-W()+6,r.x+r.w/2-W()/2+(o.dx||0))),y:Math.max(-10,Math.min(stage.clientHeight-H(),r.y-H()*0.72+(o.dy||0)))};
      const mid={x:(pos.x+to.x)/2,y:Math.min(pos.y,to.y)-26};const d=(o.dur||340)*SP;
      if(d>20)await A.animate([{transform:`translate(${pos.x}px,${pos.y}px)`},{transform:`translate(${mid.x}px,${mid.y}px) scale(1.04,.96)`},{transform:`translate(${to.x}px,${to.y}px)`}],{duration:d,easing:'cubic-bezier(.4,0,.2,1)'}).finished.catch(()=>{});
      pos=to;set(pos)},
    async squash(){if(!alive())return;await A.animate([{transform:`translate(${pos.x}px,${pos.y}px)`},{transform:`translate(${pos.x}px,${pos.y+4}px) scale(1.18,.8)`},{transform:`translate(${pos.x}px,${pos.y-10}px) scale(.92,1.1)`},{transform:`translate(${pos.x}px,${pos.y}px)`}],{duration:420*SP||1,easing:'ease-out'}).finished.catch(()=>{})},
    async type(el,t,ms=30){if(!alive())return;el.classList.add('xact');el.textContent='';for(const ch of t){if(!alive())return;el.textContent+=ch;await wait(ms)}el.classList.remove('xact')},
    async count(el,v,ms=420,pre=''){if(!alive())return;el.classList.add('xact');const t0=performance.now();await new Promise(r=>{const f=n=>{if(!alive())return r();const p=Math.min(1,(n-t0)/(ms*SP||1));el.textContent=pre+brl(v*(1-Math.pow(1-p,3)));p<1?requestAnimationFrame(f):r()};requestAnimationFrame(f)});el.classList.remove('xact')}
  };
  // entrada: vem do personagem grande do card
  const big=st.big;let from={x:pos.x,y:-80,s:1.6};
  if(big){const r=rel(big);from={x:r.x+r.w/2-W()/2,y:r.y+r.h-H(),s:Math.max(1,r.h/H())}}
  A.classList.add('on');big&&big.classList.add('away');
  if(SP>0.5)await A.animate([{transform:`translate(${from.x}px,${from.y}px) scale(${from.s})`},{transform:`translate(${(from.x+pos.x)/2}px,${Math.min(from.y,pos.y)-40}px) scale(${(from.s+1)/2})`},{transform:`translate(${pos.x}px,${pos.y}px) scale(1)`}],{duration:650,easing:'cubic-bezier(.3,0,.2,1)'}).finished.catch(()=>{});
  set(pos);if(!alive())return;await x.squash();A.classList.add('work');
  await s.run(x);
  if(!alive())return;
  A.classList.remove('work');await x.wait(300);
  /* o arquivo voa para o WhatsApp */
  const dock=root.querySelector('.xp-dock');dock.innerHTML='';
  const b=document.createElement('div');b.className='xp-b';b.style.visibility='hidden';b.innerHTML=s.out().replace('class="xwho"',`class="xwho" style="color:${root.style.getPropertyValue('--ac')}"`)+'<span class="xtm">agora</span>';dock.appendChild(b);
  const dr=doc.getBoundingClientRect(),br=b.getBoundingClientRect();
  const dx=(br.left+br.width/2)-(dr.left+dr.width/2),dy=(br.top+br.height/2)-(dr.top+dr.height/2),sc=Math.max(.15,Math.min(.5,br.width/dr.width));
  const fly=doc.animate([{transform:'none',opacity:1},{transform:`translate(${dx}px,${dy}px) scale(${sc})`,opacity:0}],{duration:700*SP||1,easing:'cubic-bezier(.6,0,.3,1)',fill:'forwards'});
  if(big){const r=rel(big);A.animate([{transform:`translate(${pos.x}px,${pos.y}px)`},{transform:`translate(${r.x+r.w/2-W()/2}px,${r.y+r.h-H()}px) scale(${Math.max(1,r.h/H())})`,opacity:.2}],{duration:600*SP||1,easing:'cubic-bezier(.4,0,.2,1)',fill:'forwards'}).finished.then(()=>{A.classList.remove('on');A.getAnimations().forEach(a=>a.cancel());big.classList.remove('away')}).catch(()=>{})}
  await fly.finished.catch(()=>{});if(!alive())return;
  b.style.visibility='';b.style.animation='xpPop .4s cubic-bezier(.2,1.3,.4,1) both';
  await x.wait(500);fly.cancel();doc.animate([{opacity:0},{opacity:1}],{duration:400});
  root.classList.remove('run');root.classList.add('done');
  const pick=document.getElementById('pick');if(pick){pick.classList.remove('nudge');void pick.offsetWidth;pick.classList.add('nudge')}
}

window.GXP={mount,stop,start,S};
})();
