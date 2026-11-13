/* Germo: guarda a origem do link (creator, campanha) e monta o link de indicação. */
(function(){
  try{var q=new URLSearchParams(location.search);var o=q.get('origem')||q.get('utm_source');if(o){localStorage.setItem('germo_origem',o);localStorage.setItem('germo_origem_em',String(Date.now()))}}catch(e){}
  window.germoOrigem=function(){
    try{var q=new URLSearchParams(location.search);var o=q.get('origem')||q.get('utm_source');if(o)return o;
      var s=localStorage.getItem('germo_origem'),t=+localStorage.getItem('germo_origem_em')||0;
      if(s&&Date.now()-t<1000*60*60*24*30)return s}catch(e){}
    return ''};
  window.germoIndicar=function(){
    var u=location.origin+location.pathname+'?origem=indicacao';
    var t='Olha isso: a Germo vai colocar 10 ajudantes do agro no WhatsApp. Planilha, contrato, previsão do tempo e muito mais, tudo pronto. Entra na lista de espera antes do lançamento: '+u;
    return 'https://wa.me/?text='+encodeURIComponent(t)};
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-indicar]');if(a){a.href=window.germoIndicar()}},true);
})();
