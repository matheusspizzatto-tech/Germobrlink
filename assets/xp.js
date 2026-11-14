/* Experiência dos 10 ajudantes: pedido por áudio, ajudante vivo trabalhando dentro do arquivo real e entrega no WhatsApp */
(function(){
'use strict';
const CF='https://d2ol7oe51mr4n9.cloudfront.net/user_2vVA8WvBFtZCaqwnis3S3BiJPUC/';
const DW=440,DH=330;
const RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
/* personagens animados (WebP com transparência) */
const AN={planilha:'77a84634-ab19-4f8e-a4f5-e97493e27a06',clima:'ab8082e3-903d-4a59-b901-6ea26a474f92',campo:'9ff8c61b-3ece-4cb8-8399-fb46017d4306',agronomo:'aa94c436-e32f-4c43-90eb-963ef23d06b9',vendas:'026844e3-3cc1-4d5e-8005-7fe68de5dcea',viral:'9df7c9b2-ac45-4982-859d-4954442f6d45',vitrine:'f489cd79-a787-433c-88a0-76fcdf9c442b',apresenta:'ef1af3ce-1917-407d-955e-47f075c847fa',juridico:'3a2cffde-0b79-4d84-b6f2-bd812e13df05',contabil:'cbe1841b-dbb3-453d-bb67-8077ed0d99da'};
const PH={aerea:'d9ae5b6b-5bf8-49ab-8454-350a35fa3cf4',silos:'4e0ac8fb-31ef-4c3d-89aa-9c29377f6494',morango:'ce620c4e-5d99-443a-aea1-b8b56270f901',estagio:'15aef3f0-240c-4aec-9129-109c269ff03f',reel:'22c8564d-e21b-47ff-92eb-962f4eb2818c',folha:'1884ab02-874f-40bf-9f5c-8615cadff4c5',soja:'9fc7ae9e-623f-4bab-a29e-c56c5065a0b9',pano:'d010c10b-c21c-4bd9-9899-6d1827433d3f'};
const ph=k=>CF+PH[k]+'.jpg';
const brl=v=>v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const FILE=(c,t,n,s)=>`<div class="xp-file"><i style="background:${c}">${t}</i><span><b>${n}</b><small>${s}</small></span></div>`;
const IC={heart:'<svg viewBox="0 0 24 24"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',msg:'<svg viewBox="0 0 24 24"><path d="M20 11.5a8 8 0 0 1-11.6 7.1L4 20l1.4-4.2A8 8 0 1 1 20 11.5z"/></svg>',send:'<svg viewBox="0 0 24 24"><path d="M21 3 10 14M21 3l-7 18-4-7-7-4z"/></svg>',save:'<svg viewBox="0 0 24 24"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>'};
const PLAY='<svg width="14" height="14" viewBox="0 0 24 24" fill="#0A0C0B" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>';

/* slides da apresentação */
const SL=()=>[
`<div class="sl-cv"><div><span class="k">RELATÓRIO DE ESTÁGIO</span><h6>Assistência técnica na Cooperativa Vale Verde</h6><p>Ana Clara Souza<br>Agronomia · 2026</p></div><div style="background-image:url(${ph('estagio')});background-position:82% center"></div></div>`,
`<div class="sl-2"><div class="sl-im" style="background-image:url(${ph('silos')})"></div><div class="pad"><span class="k">ONDE ESTAGIEI</span><h6>A cooperativa</h6><ul><li>1.240 cooperados na região</li><li>Recebe soja, milho e trigo</li><li>Equipe de 14 técnicos de campo</li></ul></div></div>`,
`<div class="pad"><span class="k">OBJETIVOS</span><h6>O que eu fui aprender</h6><ol><li>Acompanhar as visitas técnicas</li><li>Praticar a amostragem de solo</li><li>Entender o recebimento de grãos</li></ol></div>`,
`<div class="pad"><span class="k">ATIVIDADES</span><h6>O que eu fiz</h6><ul><li>Visitas a propriedades com o técnico</li><li>Coleta e envio de amostras de solo</li><li>Monitoramento de pragas na soja</li><li>Classificação de grãos na recepção</li></ul></div>`,
`<div class="pad"><span class="k">EM NÚMEROS</span><h6>4 meses de estágio</h6><div class="sl-st"><div><b>320</b>horas de estágio</div><div><b>38</b>propriedades visitadas</div><div><b>112</b>amostras de solo</div></div></div>`,
`<div class="pad"><span class="k">RESULTADO</span><h6>Produtividade da soja, em sacas por hectare</h6><div class="sl-ch"><div style="--h:66px"><b>58</b><span>Média da região</span></div><div style="--h:80px"><b>64</b><span>Áreas acompanhadas</span></div></div></div>`,
`<div class="pad"><span class="k">APRENDIZADOS</span><h6>O que eu levo comigo</h6><ul><li>Recomendação boa começa na amostra de solo</li><li>O produtor decide melhor com número na mão</li><li>O campo ensina mais do que a sala de aula</li></ul></div>`,
`<div class="sl-end"><div><h6>Obrigada!</h6><p>Ana Clara Souza · Agronomia</p></div></div>`];

/* cada ajudante: áudio (a), duração (d), fala (f), arquivo (doc), trabalho (run), resposta (out) */
const S={
planilha:{a:'90123b73-0960-4cc5-ac36-cba4b15e5f31',d:4.4,t:9,f:'Ô Germo, monta pra mim a planilha dos salários do pessoal desse mês.',
 doc(){const row=(n,c='')=>`<tr class="${c}"><th>${n}</th>${'ABCD'.split('').map((l,i)=>`<td data-c="${l}${n}"${i>1?' class="n"':''}></td>`).join('')}</tr>`;
  return `<div class="xw xls"><div class="xw-bar"><i>X</i><b>Salários_Novembro.xlsx</b><em>Salvo</em></div><div class="xls-tabs"><span>Arquivo</span><span class="on">Página Inicial</span><span>Inserir</span><span>Fórmulas</span><span>Dados</span></div><div class="xls-fx"><b class="xref">A2</b><i>fx</i><span class="xfx"></span></div><table class="xls-g"><colgroup><col style="width:22px"><col style="width:132px"><col style="width:104px"><col style="width:94px"><col style="width:88px"></colgroup><tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th></tr><tr class="hd"><th>1</th><td>Funcionário</td><td>Função</td><td class="n">Salário</td><td class="n">FGTS 8%</td></tr>${[2,3,4,5].map(n=>row(n)).join('')}${row(6,'tot')}${row(7)}${row(8)}</table><div class="xls-sh"><span class="on">Novembro</span><span>Outubro</span><span>Resumo</span><em class="xst">Pronto</em></div></div>`},
 async run(x){const R=[['João Silva','Tratorista',2900],['Maria Souza','Ordenhadora',2450],['Pedro Lima','Operador',3100],['Ana Costa','Administrativo',2700]];
  const ref=x.q('.xref'),fx=x.q('.xfx'),c=id=>x.q(`[data-c="${id}"]`);
  const sel=(td,f)=>{x.qa('.sel').forEach(e=>e.classList.remove('sel'));td.classList.add('sel');ref.textContent=td.dataset.c;fx.textContent=f||''};
  await x.cam([176,150],1.3);
  for(let i=0;i<4;i++){const n=i+2,a=c('A'+n),b=c('B'+n),s=c('C'+n);sel(a);await x.to(s,{side:'b',dx:.1,dy:.02});await x.type(a,R[i][0],20,fx);sel(b);await x.type(b,R[i][1],20,fx);sel(s,brl(R[i][2]));await x.count(s,R[i][2],240)}
  await x.cam([330,170],1.3);
  for(let i=0;i<4;i++){const n=i+2,d=c('D'+n);sel(d,`=C${n}*8%`);if(i===0)await x.to(c('B7'),{side:'b',dy:-.14});await x.count(d,R[i][2]*.08,220);await x.wait(90)}
  c('A6').textContent='Total';const tc=c('C6'),td=c('D6');sel(tc,'=SOMA(C2:C5)');await x.count(tc,11150,420);sel(td,'=SOMA(D2:D5)');await x.count(td,892,340);
  x.q('.xst').textContent='Soma: 11.150,00';await x.wait(350);x.qa('.sel').forEach(e=>e.classList.remove('sel'))},
 out:()=>`${FILE('#1D6F42','XLS','Salários_Novembro.xlsx','Planilha · 1 aba')}Pronto! 4 funcionários, R$ 11.150,00 de folha no mês. Já calculei os 8% de FGTS: R$ 892,00.`},

clima:{a:'22a0578b-3d78-4705-82c0-aaca0b46beaa',d:4.8,t:8,f:'Germo, vai chover amanhã aqui na fazenda? Preciso saber se dá pra colher.',
 doc(){const H=[['07h',0],['09h',0],['11h',0],['13h',0],['15h',18],['17h',14],['19h',6],['21h',2]];
  return `<div class="xw wx"><div class="wx-map" style="background-image:url(${ph('aerea')})"><div class="wx-rad"><i></i><i></i><i></i></div><div class="wx-pin"><b></b><span>Fazenda Boa Vista</span></div><div class="wx-top"><b>Radar de chuva · amanhã</b><span class="wxh">07h</span></div><div class="wx-leg"><i style="background:#3896FF"></i>fraca<i style="background:#34C759"></i>moderada<i style="background:#FFC400"></i>forte<i style="background:#FF4030"></i>muito forte</div></div><div class="wx-pan"><div class="wx-now"><small>CHUVA PREVISTA</small><strong><span class="wxm">0</span><u>mm</u></strong><span class="wxs">amanhã, na fazenda</span><span class="wx-win">Colher: das 7h às 13h</span></div><div class="wx-bars">${H.map(([h,m])=>`<div data-m="${m}"><u>${m?m+' mm':'seco'}</u><i></i>${h}</div>`).join('')}</div></div></div>`},
 async run(x){const bars=x.qa('.wx-bars div'),rad=x.q('.wx-rad'),hh=x.q('.wxh'),mm=x.q('.wxm'),P=[-78,-66,-54,-42,-12,6,26,48];let acc=0;
  await x.to(x.q('.wxh'),{side:'b',dx:.03,dy:.05});
  for(let i=0;i<8;i++){const b=bars[i],m=+b.dataset.m;bars.forEach(e=>e.classList.remove('cur'));b.classList.add('cur','on',m?'wet':'dry');b.querySelector('i').style.height=(m?16+m*4:9)+'px';hh.textContent=b.lastChild.textContent;rad.style.transform=`translateX(${P[i]}%)`;
   if(m){acc+=m;mm.textContent=acc}
   if(i===3)x.on(x.q('.wx-win'));
   if(i===4){x.q('.wxs').textContent='amanhã, a partir das 15h';await x.hop()}
   await x.wait(i===4?900:520)}
  bars.forEach(e=>e.classList.remove('cur'));hh.textContent='15h às 21h';rad.style.transform='translateX(6%)';await x.wait(500)},
 out:()=>`Amanhã chove 40 mm na fazenda, começando às 15h. Dá para colher das 7h às 13h.`},

campo:{a:'7f90076d-2d0b-4f5b-9ff2-e04eb82fbf5a',d:4.7,t:11,f:'Germo, acabei a visita no talhão 4. Faz o relatório com essas fotos pra mim.',
 doc(){const F=['Produtor','Propriedade','Município','Cultura','Estádio','Área'];
  const T=[['Ferrugem asiática','Lesões em 8% das folhas de baixo','xat','Atenção'],['Percevejos','1,5 por metro, no pano de batida','xok','Abaixo do nível de ação'],['Lagartas','4 por metro, no pano de batida','xok','Abaixo do nível de ação']];
  return `<div class="xw pdf"><div class="xw-bar"><i>PDF</i><b>Relatorio_Visita_Talhao4.pdf</b><em>1 / 2</em></div><div class="pg"><div class="pg-h"><div><small>RELATÓRIO DE VISITA TÉCNICA</small><b>Talhão 4 · Soja</b></div><span>Nº 047/2026<br>Safra 2026/27</span></div><div class="pg-f">${F.map(f=>`<div><small>${f}</small><span></span></div>`).join('')}</div><h5>1. Registro fotográfico</h5><div class="pg-ph">${[['soja','Foto 1: lavoura em R3, com bom estande'],['folha','Foto 2: lesões nas folhas de baixo'],['pano','Foto 3: pano de batida entre as linhas']].map(([p,c])=>`<figure><span style="background-image:url(${ph(p)})"></span><figcaption>${c}</figcaption></figure>`).join('')}</div><h5>2. Monitoramento</h5><table class="pg-t"><thead><tr><th>Alvo</th><th>O que encontramos</th><th>Situação</th></tr></thead><tbody>${T.map(([a,b,c,d])=>`<tr><td><b>${a}</b></td><td>${b}</td><td><em class="${c}">${d}</em></td></tr>`).join('')}</tbody></table><h5>3. Recomendações</h5><ol class="pg-r"><li></li><li></li><li></li></ol><div class="pg-s"><div><svg viewBox="0 0 110 34"><path d="M4 26c8-14 14-20 16-12s-6 16-2 14 10-18 16-16-4 14 2 12 8-10 14-10 2 8 8 6 10-8 18-8 10 6 26 2"/></svg>Técnico responsável</div><span>Página 1 de 2</span></div></div></div>`},
 async run(x){const V=['José Almeida','Fazenda Boa Vista','Rio Verde, GO','Soja','R3, formação de vagens','62 hectares'],f=x.qa('.pg-f span');
  await x.cam(x.q('.pg-f'),1.3);await x.to(f[4],{side:'b',dy:.07});
  for(let i=0;i<6;i++)await x.type(f[i],V[i],13);
  const figs=x.qa('.pg-ph figure');await x.cam(x.q('.pg-ph'),1.25);await x.to(figs[1],{side:'b',dy:-.05});
  for(const g of figs){x.on(g);await x.wait(330)}
  const rows=x.qa('.pg-t tbody tr');await x.cam(x.q('.pg-t'),1.3);await x.to(rows[2],{side:'b',dx:.2});
  for(const r of rows){x.on(r);await x.wait(380)}
  const li=x.qa('.pg-r li'),L=['Confirmar a ferrugem com lupa de 20x no verso das folhas.','Nova vistoria em 5 dias, com foco nas folhas de baixo.','Decidir o controle com o agrônomo responsável.'];
  await x.cam(x.q('.pg-r'),1.3);await x.to(x.q('.pg-s'),{side:'r',dx:-.3,dy:-.06});
  for(let i=0;i<3;i++)await x.type(li[i],L[i],11);
  x.on(x.q('.pg-s'));await x.wait(1150)},
 out:()=>`${FILE('#C8402F','PDF','Relatorio_Visita_Talhao4.pdf','PDF · 2 páginas')}Relatório pronto, com as 3 fotos, o monitoramento e as recomendações. É só enviar ao produtor.`},

agronomo:{a:'5208050f-a0bb-4fbc-83b3-2b0868545835',d:3.6,t:7,f:'Apareceu essa mancha na folha da soja. O que pode ser?',
 doc:()=>`<div class="xw dx"><div class="dx-ph" style="background-image:url(${ph('folha')})"><span class="dx-tag">Foto enviada pelo produtor</span><i class="dx-scan"></i>${[[57,27],[68,69],[27,60]].map(([l,t],i)=>`<span class="dx-ring" style="left:${l}%;top:${t}%"><b>${i+1}</b></span>`).join('')}<div class="dx-lp" style="background-image:url(${ph('folha')});background-position:-813px -365px"><small>zoom na lesão 1</small></div></div><div class="dx-c"><div><small>TRIAGEM DA FOTO</small><div class="dx-r t1" style="--w:74%"><b>Ferrugem asiática</b><em>mais provável</em><i></i></div><div class="dx-r" style="--w:26%"><b>Mancha-parda</b><em>possível</em><i></i></div><div class="dx-r" style="--w:10%"><b>Crestamento bacteriano</b><em>menos provável</em><i></i></div></div><div class="dx-n"><b>Como confirmar</b><p>Lupa de 20x no verso da folha: pústulas salientes indicam ferrugem.</p><p class="w">Chame o seu agrônomo antes de aplicar qualquer produto.</p></div></div></div>`,
 async run(x){const rg=x.qa('.dx-ring');x.on(x.q('.dx-scan'));await x.to(rg[2],{side:'b',dy:-.1});await x.wait(900);
  for(const r of rg){x.on(r);await x.wait(330)}
  await x.to(rg[0],{side:'l',dy:.1});x.on(x.q('.dx-lp'));await x.wait(800);
  const rs=x.qa('.dx-r');await x.to(x.q('.dx-n'),{side:'b',dy:-.34});
  for(const r of rs){x.on(r);await x.wait(420)}
  await x.to(rg[2],{side:'a',dx:.02,dy:.12});x.on(x.q('.dx-n'));await x.wait(900)},
 out:()=>`Pela foto, o mais provável é ferrugem asiática no início. Confirme com lupa no verso da folha e chame o seu agrônomo hoje.<span class="xbtn">Falar com um agrônomo parceiro</span>`},

vendas:{a:'1ac5537b-3a53-4d86-9c66-7592b35f3de7',d:4,t:9,f:'Recebi 3 propostas pela soja. Qual que tá pagando melhor?',
 doc(){const P=[['Cooperativa',128,0,'30 dias'],['Trading',134,5,'à vista'],['Cerealista',131.5,1,'7 dias']],lq=p=>p[1]-p[2]-p[1]*.015;
  const tr=(c,l,f)=>`<tr class="${c}"><td>${l}</td>${P.map((p,i)=>`<td data-c="${i}"><span>${f(p)}</span></td>`).join('')}</tr>`;
  return `<div class="xw xcmp"><div class="xw-bar"><i>PDF</i><b>Comparativo_Propostas_Soja.pdf</b><em>1 / 1</em></div><div class="cmp-pg"><div class="cmp-h"><div><small>COMPARATIVO DE PROPOSTAS</small><b>Soja · 2.000 sacas</b></div><span>valores em reais,<br>por saca de 60 kg</span></div><table class="cmp-t"><thead><tr><th></th>${P.map((p,i)=>`<th data-c="${i}">${i===2?'<em class="cmp-st" style="font-style:normal">MELHOR</em>':''}${p[0]}</th>`).join('')}</tr></thead><tbody>${tr('','Preço oferecido',p=>brl(p[1]))}${tr('','Frete até a entrega',p=>p[2]?'<span class="neg on">− '+brl(p[2])+'</span>':'incluso')}${tr('','Funrural (1,5%)',p=>'<span class="neg on">− '+brl(p[1]*.015)+'</span>')}${tr('lq','Líquido por saca',p=>brl(lq(p)))}${tr('','Prazo de pagamento',p=>p[3])}${tr('tt','Total em 2.000 sacas',p=>brl(lq(p)*2000))}</tbody></table><div class="cmp-f"><b>Melhor proposta: Cerealista.</b> São R$ 4.895,00 a mais que na Cooperativa.</div></div></div>`},
 async run(x){const rows=x.qa('.cmp-t tbody tr');
  await x.cam([220,150],1.12);
  for(let r=0;r<rows.length;r++){const sp=[...rows[r].querySelectorAll('td>span')];if(r===0)await x.to(rows[3].firstElementChild,{side:'b',dy:-.05});if(r===3)await x.to(x.q('.cmp-t thead th'),{side:'a',dx:-.03,dy:.2});
   for(const s of sp){x.on(s);await x.wait(r===3?260:150)}
   if(r===3){await x.wait(250);x.qa('[data-c="2"]').forEach(e=>e.classList.add('best'));x.on(x.q('.cmp-st'));await x.hop();await x.wait(450)}
   await x.wait(140)}
  x.on(x.q('.cmp-f'));await x.wait(800)},
 out:()=>`${FILE('#B88F0E','PDF','Comparativo_Propostas_Soja.pdf','PDF · 1 página')}A melhor é a Cerealista: R$ 128,53 líquidos por saca, já sem frete e Funrural. Em 2.000 sacas, são R$ 4.895,00 a mais que na Cooperativa.`},

viral:{a:'4040b006-bd5e-4c02-9f75-a47ba37def5e',d:4,t:9,f:'Germo, me dá um roteiro de reels pra mostrar a colheita do milho.',
 doc(){const L=[['0:00','Gancho','"Ninguém mostra isso da colheita do milho."'],['0:03','Cena 1','Plano aberto: a colheitadeira entrando no talhão.'],['0:08','Cena 2','Câmera lenta: o grão caindo no caminhão.'],['0:14','Cena 3','Você na frente da lavoura, contando quantas sacas deu.'],['0:20','Chamada','"Comenta MILHO que eu te conto o resto."']];
  return `<div class="xw rl"><div class="rl-ph" style="background-image:url(${ph('reel')})"><span class="rl-tp">Reels</span><span class="rl-ch">0:00 · Gancho</span><b class="rl-hk"></b><div class="rl-sd">${IC.heart}${IC.msg}${IC.send}</div><div class="rl-bt"><b>fazendaboavista</b>Um ano de trabalho em 25 segundos.</div><div class="rl-pb"><i></i></div></div><div class="rl-sc"><small>ROTEIRO · 25 SEGUNDOS</small>${L.map(([t,a,b])=>`<div class="rl-l" data-t="${t}" data-a="${a}"><em>${t}</em><div><b>${a}</b><span>${b}</span></div></div>`).join('')}<div class="rl-cp"><b>Legenda:</b> Um ano de trabalho em 25 segundos. <u>#colheita #milho #agro</u></div></div></div>`},
 async run(x){const ls=x.qa('.rl-l'),ch=x.q('.rl-ch'),pb=x.q('.rl-pb i'),W=[12,32,56,80,100];
  await x.to(x.q('.rl-sd'),{side:'l',dy:.12});await x.type(x.q('.rl-hk'),'Ninguém mostra isso da colheita do milho',24);
  for(let i=0;i<ls.length;i++){ls.forEach(l=>l.classList.remove('cur'));ls[i].classList.add('on','cur');ch.textContent=ls[i].dataset.t+' · '+ls[i].dataset.a;pb.style.width=W[i]+'%';if(i===2)await x.to(ls[4],{side:'b',dx:.2,dy:-.1});await x.wait(i?620:420)}
  ls.forEach(l=>l.classList.remove('cur'));x.on(x.q('.rl-cp'));await x.wait(800)},
 out:()=>`${FILE('#D9590E','PDF','Roteiro_Reels_Colheita.pdf','PDF · 1 página')}Roteiro de 25 segundos pronto: gancho, 3 cenas, chamada e a legenda para postar.`},

vitrine:{a:null,d:2.6,t:9,f:'Faz um post pra eu vender os morangos que eu colhi hoje.',
 doc:()=>`<div class="xw xig"><div class="ig-p"><div class="ig-u"><i>SD</i><span><b>sitiodocecolheita</b><small>Sítio Doce Colheita</small></span></div><div class="ig-a" style="background-image:url(${ph('morango')})"><span class="ig-k">COLHEITA DE HOJE</span><div class="ig-t"></div><div class="ig-pr"><span>1 kg por</span><b>R$ 25</b></div><div class="ig-ft">Entrega no sábado<br><b>Peça pelo WhatsApp</b></div></div><div class="ig-ac">${IC.heart}${IC.msg}${IC.send}${IC.save}</div><div class="ig-cp"><b>sitiodocecolheita</b> Colhemos hoje cedo, no ponto certo.</div></div><div class="ig-s"><small>LEGENDA PRONTA</small><p class="cp"></p><small>HASHTAGS</small><p class="hs"></p><div class="ig-f"><span>Feed · 1080 × 1350</span><span>Stories · 1080 × 1920</span></div></div></div>`,
 async run(x){const a=x.q('.ig-a');await x.to(a,{side:'r',dx:-.16,dy:.22});x.on(a);x.on(x.q('.ig-k'));await x.wait(350);
  await x.type(x.q('.ig-t'),'Morango doce, direto do pé',34);x.on(x.q('.ig-pr'));await x.hop();await x.wait(350);x.on(x.q('.ig-ft'));await x.wait(450);
  await x.to(x.q('.ig-f'),{side:'b',dx:.1,dy:-.14});
  await x.type(x.q('.ig-s .cp'),'Colhemos hoje cedo, no ponto certo. Caixa de 1 kg por R$ 25. Entrega no sábado. Peça pelo WhatsApp.',15);
  await x.type(x.q('.ig-s .hs'),'#morango #colheitadodia #diretodoprodutor #frutafresca',15);
  for(const f of x.qa('.ig-f span')){x.on(f);await x.wait(300)}await x.wait(400)},
 out:()=>`${FILE('#2585E0','PNG','Post_Morangos.png','Imagem · 1080 × 1350')}Arte pronta, com a legenda e as hashtags. É só publicar.`},

apresenta:{a:null,d:2.8,t:8,f:'Monta uma apresentação do meu estágio na cooperativa, com 8 slides.',
 doc(){const s=SL();return `<div class="xw pp"><div class="xw-bar"><i>P</i><b>Estagio_Cooperativa_Vale_Verde.pptx</b><em>8 slides</em></div><div class="pp-b"><div class="pp-r">${s.map((h,i)=>`<div class="pp-th">${i+1}<span><div class="sl">${h}</div></span></div>`).join('')}</div><div class="pp-m"><div class="pp-v">${s.map(h=>`<div class="sl">${h}</div>`).join('')}</div><span class="pp-n">Slide 1 de 8</span></div></div></div>`},
 async run(x){const th=x.qa('.pp-th'),sl=x.qa('.pp-v .sl'),n=x.q('.pp-n'),T=[1000,650,480,480,850,950,480,700];
  await x.to(x.q('.pp-n'),{side:'r',dx:.3,dy:.2});
  for(let i=0;i<8;i++){th.forEach(t=>t.classList.remove('cur'));th[i].classList.add('on','cur');sl.forEach(s=>s.classList.remove('on'));sl[i].classList.add('on');n.textContent=`Slide ${i+1} de 8`;if(i===4||i===7)await x.hop();await x.wait(T[i])}
  if(x.fast){th.forEach(t=>t.classList.remove('cur'));th[0].classList.add('cur');sl.forEach(s=>s.classList.remove('on'));sl[0].classList.add('on');n.textContent='Slide 1 de 8'}},
 out:()=>`${FILE('#5B3FD6','PPT','Estagio_Cooperativa_Vale_Verde.pptx','Apresentação · 8 slides')}8 slides prontos: capa, cooperativa, objetivos, atividades, números, resultado, aprendizados e agradecimento.`},

juridico:{a:null,d:2.8,t:15,f:'Analisa esse contrato de arrendamento e me fala o que tá faltando.',
 doc:()=>`<div class="xw xct"><div class="xw-bar"><i>W</i><b>Contrato_Arrendamento.docx</b><em>Revisão</em></div><div class="ct-b"><div class="ct-p"><h6>CONTRATO DE ARRENDAMENTO RURAL</h6><p>Pelo presente instrumento particular, JOSÉ CARLOS ALMEIDA, produtor rural, doravante ARRENDADOR, e MARCOS VIEIRA LIMA, produtor rural, doravante ARRENDATÁRIO, ajustam o que segue, nos termos da Lei nº 4.504/64 e do Decreto nº 59.566/66:</p><p data-k="1"><b>CLÁUSULA 1ª. DO OBJETO.</b> O ARRENDADOR cede ao ARRENDATÁRIO o uso e gozo de 48 (quarenta e oito) hectares da Fazenda Boa Vista, matrícula nº 12.345 do Registro de Imóveis de Rio Verde, GO, para o cultivo de soja e milho.</p><p data-k="2"><b>CLÁUSULA 2ª. DO PRAZO.</b> O prazo é de 3 (três) anos, de 1º de setembro de 2026 a 31 de agosto de 2029.</p><p data-k="3"><b>CLÁUSULA 3ª. DO PREÇO.</b> O ARRENDATÁRIO pagará <mark>12 (doze) sacas de soja por hectare ao ano</mark>, até 30 de abril de cada ano agrícola.</p><p data-k="4"><b>CLÁUSULA 4ª. DA CONSERVAÇÃO.</b> O ARRENDATÁRIO obriga-se a conservar o solo, as cercas e as benfeitorias existentes.</p><div class="ct-ins" data-k="i1"><span>+ Cláusula ausente: renovação e preferência</span></div><div class="ct-ins" data-k="i2"><span>+ Cláusula ausente: ITR e benfeitorias</span></div><p data-k="5"><b>CLÁUSULA 5ª. DO FORO.</b> Fica eleito o foro da comarca de Rio Verde, GO.</p><div class="ct-sg"><div>ARRENDADOR</div><div>ARRENDATÁRIO</div></div></div><div class="ct-m"><div class="ct-c" data-f="3"><b>Preço em sacas</b>A lei pede o preço em dinheiro (Decreto 59.566/66, art. 18). O pagamento pode ser em produto.</div><div class="ct-c" data-f="i1"><b>Falta a renovação</b>Inclua a preferência para renovar (Estatuto da Terra, art. 95, IV).</div><div class="ct-c" data-f="i2"><b>Falta o ITR</b>Defina quem paga o imposto e as benfeitorias.</div></div></div></div>`,
 async run(x){const k=id=>x.q(`[data-k="${id}"]`),m=x.q('.ct-m');let low=0;
  const note=async id=>{const t=k(id),c=x.q(`.ct-c[data-f="${id}"]`);const y=Math.max(low,x.wpos(t).y-x.wpos(m).y-4);c.style.top=y+'px';if(!x.fast){await x.cam([318,x.wpos(t).y+20],1.4);await x.to(c,{side:'b',dx:-.3,dy:-.04})}x.on(c);low=y+c.offsetHeight+5;await x.wait(800)};
  const read=async(id,ok)=>{const p=k(id);await x.cam([156,x.wpos(p).y+18],1.4);await x.to(p,{side:'b',dx:.16});x.on(p,'rd');await x.wait(380);x.off(p,'rd');x.on(p,ok?'okc':'bad');await x.wait(160)};
  await read(1,1);await read(2,1);await read(3,0);await note(3);
  await read(4,1);x.on(k('i1'));await x.wait(380);await note('i1');x.on(k('i2'));await x.wait(380);await note('i2');
  await read(5,1)},
 out:()=>`${FILE('#7A1F3A','DOC','Contrato_revisado.docx','Word · 3 comentários')}Achei 3 pontos: o preço está em sacas e a lei pede em dinheiro; falta a cláusula de renovação; falta dizer quem paga o ITR. Leve ao seu advogado antes de assinar.<span class="xbtn">Falar com um advogado parceiro</span>`},

contabil:{a:null,d:2.6,t:10,f:'Organiza as notas do mês no livro caixa pro meu contador.',
 N:[['NF-e 4.812','03/11','Óleo diesel S10',-1240],['NF-e 15.207','07/11','Adubo NPK',-8900],['NFP-e 311','12/11','Venda de leite',14320],['NF-e 9.044','18/11','Defensivo',-2150],['NF-e 2.376','21/11','Peças do trator',-760]],
 doc(){return `<div class="xw lc"><div class="xw-bar"><i>X</i><b>Livro_Caixa_Novembro.xlsx</b><em>Salvo</em></div><div class="lc-b"><div class="lc-n"><small>NOTAS DO MÊS</small>${this.N.map(([n,d,h,v])=>`<div class="nf"><u>${n} · ${d}</u><b>${h}</b><s></s>R$ ${brl(Math.abs(v))}</div>`).join('')}</div><div><div class="lc-t"><h6>Livro Caixa do Produtor Rural<span>novembro</span></h6><table><colgroup><col style="width:38px"><col><col style="width:60px"><col style="width:60px"><col style="width:64px"></colgroup><thead><tr><th>Data</th><th>Histórico</th><th class="n">Entrada</th><th class="n">Saída</th><th class="n">Saldo</th></tr></thead><tbody><tr><td>01/11</td><td>Saldo anterior</td><td></td><td></td><td class="n">18.400,00</td></tr></tbody><tfoot><tr><td></td><td>Totais do mês</td><td class="n xin te">0,00</td><td class="n xout ts">0,00</td><td class="n tb">18.400,00</td></tr></tfoot></table></div><div class="lc-al">1 nota sem o seu CPF: peça a correção.</div></div></div></div>`},
 async run(x){const nf=x.qa('.nf'),tb=x.q('.lc-t tbody'),te=x.q('.te'),ts=x.q('.ts'),tbl=x.q('.tb');let bal=18400,en=0,sa=0;
  for(let i=0;i<5;i++){const [n,d,h,v]=this.N[i],c=nf[i];x.on(c,'act');await x.to(c,i<2?{side:'b',dy:-.03}:{side:'a'});await x.wait(260);
   if(i===4){x.off(c,'act');x.on(c,'fl');x.on(x.q('.lc-al'));await x.hop();await x.wait(700);break}
   const tr=document.createElement('tr');tr.className='nw';tr.innerHTML=`<td>${d}</td><td>${h}</td><td class="n xin">${v>0?brl(v):''}</td><td class="n xout">${v<0?brl(-v):''}</td><td class="n"></td>`;tb.appendChild(tr);
   bal+=v;v>0?en+=v:sa-=v;await x.count(tr.lastChild,bal,300);te.textContent=brl(en);ts.textContent=brl(sa);tbl.textContent=brl(bal);x.off(c,'act');x.on(c,'dn');await x.wait(200)}
  if(!x.fast){await x.cam(x.q('.lc-t tfoot'),1.35);await x.to(x.q('.lc-t h6'),{side:'b',dx:-.42});await x.wait(1000)}},
 out:()=>`${FILE('#22408C','XLS','Livro_Caixa_Novembro.xlsx','Planilha · 1 aba')}4 notas lançadas no livro caixa. Saldo do mês: R$ 20.430,00. A nota das peças veio sem o seu CPF: peça a correção.`}
};

/* ===== motor ===== */
const audio=new Audio();audio.preload='auto';
let run=0,state=null,ro=null;
class Cancel extends Error{}

function applyCam(st,tx,ty,z,instant){const w=st.world;st.cam={tx,ty,z};if(instant){w.style.transition='none'}w.style.transform=`translate(${tx}px,${ty}px) scale(${st.scale*z})`;if(instant){void w.offsetWidth;w.style.transition=''}}

function helpers(st,alive,fast){
  const {stage,world,A}=st;
  const chk=()=>{if(!alive())throw new Cancel()};
  const wait=ms=>{chk();return fast?Promise.resolve():new Promise(r=>setTimeout(r,RM?Math.min(ms,80):ms)).then(chk)};
  const wpos=el=>{const wr=world.getBoundingClientRect(),er=el.getBoundingClientRect(),k=(wr.width/DW)||1;return{x:(er.left-wr.left)/k,y:(er.top-wr.top)/k,w:er.width/k,h:er.height/k}};
  const size=()=>{const h=A.offsetHeight||stage.clientHeight*.42;return{w:A.offsetWidth>8?A.offsetWidth:h*.8,h}};
  let pos=null;
  const put=(x,y)=>{pos={x,y};A.style.transform=`translate(${x}px,${y}px)`};
  const raf=fn=>new Promise((res,rej)=>{const t0=performance.now();const f=n=>{if(!alive())return rej(new Cancel());fn(Math.max(0,n-t0))?res():requestAnimationFrame(f)};requestAnimationFrame(f)});
  const x={fast,wait,wpos,
    q:s=>world.querySelector(s),qa:s=>[...world.querySelectorAll(s)],
    on(el,c='on'){chk();el&&el.classList.add(c)},off(el,c='on'){el&&el.classList.remove(c)},
    async cam(t,z=1){chk();if(fast)return;const W=stage.clientWidth,H=stage.clientHeight,s=st.scale;let tx=0,ty=0;
      if(t){const p=Array.isArray(t)?{x:t[0],y:t[1],w:0,h:0}:wpos(t),cx=p.x+p.w/2,cy=p.y+p.h/2,WH=Math.max(DH,world.offsetHeight);
        tx=Math.min(0,Math.max(W-DW*s*z,W/2-cx*s*z));ty=Math.min(0,Math.max(H-WH*s*z,H/2-cy*s*z))}else z=1;
      const c=st.cam;if(c&&Math.abs(c.tx-tx)<1.5&&Math.abs(c.ty-ty)<1.5&&c.z===z)return;
      applyCam(st,tx,ty,z,false);await wait(660)},
    async to(el,o={}){chk();if(fast||!el)return;const W=stage.clientWidth,H=stage.clientHeight,{w,h}=size();
      const sr=stage.getBoundingClientRect(),er=el.getBoundingClientRect(),l=er.left-sr.left,t=er.top-sr.top,r=er.right-sr.left,b=er.bottom-sr.top;
      const side=o.side||((l+r)/2>W*.58?'l':'r');let ax,ay;
      if(side==='b'){ax=(l+r)/2-w/2;ay=b-h*.1}else if(side==='a'){ax=(l+r)/2-w/2;ay=t-h*.9}else{ax=side==='r'?r-w*.12:l-w*.88;ay=(t+b)/2-h*.3}
      ax+=(o.dx||0)*W;ay+=(o.dy||0)*H;
      ax=Math.max(-w*.1,Math.min(W-w*.9,ax));ay=Math.max(-h*.04,Math.min(H-h*.97,ay));
      if(pos&&Math.hypot(pos.x-ax,pos.y-ay)<8)return;
      A.classList.remove('mv','yay');void A.offsetWidth;A.classList.add('mv');put(ax,ay);await wait(500)},
    async hop(){chk();if(fast)return;A.classList.remove('mv','yay');void A.offsetWidth;A.classList.add('yay');await wait(360)},
    enter(){const W=stage.clientWidth,H=stage.clientHeight,{w,h}=size();A.style.transition='none';put(W-w*.96,H-h*.98);void A.offsetWidth;A.style.transition='';A.classList.add('on','pop');setTimeout(()=>A.classList.remove('pop'),560)},
    async type(el,t,ms=22,mir){chk();if(fast){el.textContent=t;if(mir)mir.textContent=t;return}
      el.classList.add('xact');try{await raf(e=>{const c=Math.min(t.length,Math.floor(e/(RM?1:ms))+1),v=t.slice(0,c);el.textContent=v;if(mir)mir.textContent=v;return c>=t.length})}finally{el.classList.remove('xact')}},
    async count(el,v,ms=380,o={}){chk();const fmt=n=>(o.pre||'')+brl(n);if(fast){el.textContent=fmt(v);return}
      await raf(e=>{const p=Math.min(1,e/(RM?1:ms));el.textContent=fmt(v*(1-Math.pow(1-p,3)));return p>=1})}
  };
  return x;
}

function reply(st,anim){const d=st.root.querySelector('.xp-dock');d.innerHTML=`<div class="xp-b${anim?' in':''}"><span class="xwho">${esc(st.n)}</span>${st.s.out()}<span class="xtm">agora</span></div>`}
function setGo(st,again){const g=st.root.querySelector('.xp-go span');if(g)g.textContent=again?'Ver de novo':`Ver o ${st.n} trabalhando`}
function prog(st,p,t){const wv=st.wv,tw=st.tw;wv.forEach((b,i)=>b.classList.toggle('on',i/wv.length<p));tw.forEach((w,i)=>w.classList.toggle('on',i/tw.length<p*1.08));if(st.du)st.du.textContent='0:0'+Math.min(9,Math.max(0,Math.floor(t)))}

/* estado parado: o arquivo já pronto, de verdade */
function poster(st,again){
  const id=++run,alive=()=>id===run;const {root,stage,world,s,A,big}=st;
  root.classList.remove('run','talk');A.classList.remove('on');big&&big.classList.remove('away');
  stage.classList.add('xinst');world.innerHTML=s.doc();applyCam(st,0,0,1,true);
  const x=helpers(st,alive,true);
  Promise.resolve().then(()=>s.run(x)).then(()=>{if(!alive())return;prog(st,1,s.d);reply(st,false);st.dh=root.querySelector('.xp-dock').offsetHeight;setGo(st,again);root.classList.add('done');const pg=root.querySelector('.xp-pg i');pg.style.transition='none';pg.style.width='0';
    requestAnimationFrame(()=>requestAnimationFrame(()=>{if(alive())stage.classList.remove('xinst')}))}).catch(e=>{if(!(e instanceof Cancel))console.error('[xp]',e)});
}

function halt(){run++;try{audio.pause()}catch(e){}}
function stop(){const st=state,was=st&&st.root.isConnected&&st.root.classList.contains('run');halt();if(was)poster(st,false)}

function mount(root,ag,big,auto){
  halt();if(ro){ro.disconnect();ro=null}
  const k=ag.k,s=S[k];if(!s){root.innerHTML='';state=null;return}
  root.className='xp';root.style.setProperty('--ac',ag.t);
  const words=s.f.split(' '),voice=!!s.a;
  const bars=Array.from({length:34},(_,i)=>`<i style="height:${6+Math.round(Math.abs(Math.sin(i*1.7+k.length)+Math.sin(i*.6))*9)}px"></i>`).join('');
  const url=AN[k]?CF+AN[k]+'.webp':`/img/${k}.webp`;
  root.innerHTML=`<div class="xp-req">${voice?`<div class="xp-row"><button class="xp-play" type="button" aria-label="Ouvir o pedido e ver o ${esc(ag.n)} trabalhando">${PLAY}</button><span class="xp-wv" aria-hidden="true">${bars}</span><span class="xp-du">0:0${Math.round(s.d)}</span></div>`:''}<p class="xp-tr"${voice?'':' style="margin-top:0"'}>${voice?'"':''}${words.map(w=>`<span>${esc(w)}</span>`).join(' ')}${voice?'"':''}</p><span class="xp-meta">${voice?'Pedido por áudio no WhatsApp':'Pedido por mensagem no WhatsApp'}</span></div>
<div class="xp-stage"><div class="xp-world" aria-hidden="true"></div><div class="xp-ag" aria-hidden="true"><img src="${url}" alt="" decoding="async"></div><div class="xp-pg" aria-hidden="true"><i></i></div></div>
<div class="xp-cta"><button class="xp-go" type="button"><i>${PLAY}</i><span></span></button></div>
<div class="xp-dock" aria-live="polite"></div>`;
  const stage=root.querySelector('.xp-stage');
  const st=state={root,big,s,k,n:ag.n,stage,world:root.querySelector('.xp-world'),A:root.querySelector('.xp-ag'),scale:1,cam:null,
    wv:[...root.querySelectorAll('.xp-wv i')],tw:[...root.querySelectorAll('.xp-tr span')],du:root.querySelector('.xp-du')};
  st.scale=(stage.clientWidth||DW)/DW;
  /* o personagem do topo também fica vivo */
  if(big&&AN[k]&&big.dataset.live!==k){const im=new Image();im.onload=()=>{if(big.isConnected){big.src=url;big.dataset.live=k}};im.src=url}
  ro=new ResizeObserver(()=>{const w=stage.clientWidth;if(!w)return;const ns=w/DW;if(Math.abs(ns-st.scale)<.002)return;st.scale=ns;if(!root.classList.contains('run'))applyCam(st,0,0,1,true)});ro.observe(stage);
  root.querySelector('.xp-go').addEventListener('click',()=>start());
  const pb=root.querySelector('.xp-play');pb&&pb.addEventListener('click',()=>start());
  if(auto){setGo(st,false);start()}else poster(st,false);
}

async function start(){
  const st=state;if(!st||!st.root.isConnected)return;const {root,s,stage,world,A,big}=st;
  if(root.classList.contains('run'))return;
  const id=++run,alive=()=>id===run&&root.isConnected;
  let pp=null;
  if(s.a){try{audio.src=CF+s.a+'.mp3';pp=audio.play()}catch(e){pp=null}}
  root.classList.remove('done');root.classList.add('run');
  try{window._lpPause&&window._lpPause()}catch(e){}
  A.classList.remove('on');big&&big.classList.remove('away');
  stage.classList.add('xinst');world.innerHTML=s.doc();applyCam(st,0,0,1,true);void world.offsetWidth;stage.classList.remove('xinst');
  prog(st,0,0);
  {const dk=root.querySelector('.xp-dock');if(!st.dh){reply(st,false);st.dh=dk.offsetHeight}dk.style.minHeight=st.dh+'px';dk.innerHTML=`<span class="xp-phd"><i></i><i></i><i></i>O arquivo chega aqui, no seu WhatsApp</span>`}
  /* deixa o próximo personagem pronto */
  {const ks=Object.keys(AN),nx=ks[(ks.indexOf(st.k)+1)%ks.length];if(!start.pre)start.pre={};if(!start.pre[nx]){start.pre[nx]=new Image();start.pre[nx].src=CF+AN[nx]+'.webp'}}
  const pg=root.querySelector('.xp-pg i');pg.style.transition='none';pg.style.width='0';
  {const r=stage.getBoundingClientRect();if(r.top<70||r.bottom>innerHeight-10){const y=scrollY+r.top-Math.max(90,(innerHeight-r.height)/2-40);scrollTo({top:y,behavior:RM?'auto':'smooth'})}}
  const x=helpers(st,alive,false);
  try{
    /* 1. o pedido */
    root.classList.add('talk');let played=false;
    if(pp){try{await Promise.race([pp,new Promise((_,j)=>setTimeout(j,2500))]);played=true}catch(e){try{audio.pause()}catch(_){}}}
    if(!alive())throw new Cancel();
    const talk=new Promise(res=>{const t0=performance.now(),d0=s.d;const f=()=>{if(!alive())return res();const el=(performance.now()-t0)/1000;let p,t;
      if(played){const d=isFinite(audio.duration)&&audio.duration>0?audio.duration:d0;t=audio.currentTime;p=t/d;if(audio.ended||p>=.995||el>d+4)p=1}else{t=el*(RM?6:1);p=t/d0}
      if(p>=1){prog(st,1,d0);res()}else{prog(st,p,t);requestAnimationFrame(f)}};f()});
    talk.then(()=>root.classList.remove('talk'));
    /* 2. o ajudante já começa a trabalhar junto com o áudio */
    await x.wait(450);
    big&&big.classList.add('away');x.enter();
    void pg.offsetWidth;pg.style.transition=`width ${s.t||9}s linear`;pg.style.width='94%';
    await x.wait(560);
    await s.run(x);
    await x.cam(null);
    pg.style.transition='width .3s';pg.style.width='100%';
    await x.hop();await talk;if(!alive())throw new Cancel();await x.wait(260);
    /* 3. a entrega */
    A.classList.remove('on');big&&big.classList.remove('away');
    reply(st,true);setGo(st,true);
    root.classList.remove('run');root.classList.add('done');
    const pick=document.getElementById('pick');if(pick){pick.classList.remove('nudge');void pick.offsetWidth;pick.classList.add('nudge')}
  }catch(e){
    if(!(e instanceof Cancel))console.error('[xp]',e);
    if(id===run&&root.isConnected)poster(st,false);
  }
}

window.GXP={mount,stop,start,S};
})();
