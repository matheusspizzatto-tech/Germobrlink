# Frase acima dos exemplos de cada página: a Germo entrega pronto, não só responde.
PRONTO = {
 "graos": "Não é só a cotação. Chega o custo por hectare, a janela de colheita e as propostas lado a lado.",
 "pecuaria-leite": "Você fala os litros no áudio. Volta a planilha da ordenha somada e o custo real do litro.",
 "pecuaria-corte": "Você manda a pesagem. Volta o ganho por lote, o custo da arroba e a proposta pronta para o frigorífico.",
 "cafe": "Não é só dica de manejo. Chega o custo por saca, a apresentação para o comprador e o post da safra.",
 "hortifruti": "Você manda os pedidos por áudio. Volta a colheita da semana organizada e a proposta pronta para o mercado.",
 "fruticultura": "Não é só a cotação da caixa. Chega o custo, a margem e a proposta pronta para o atacado.",
 "avicultura-suinocultura": "Não é só explicar o contrato. Nós conferimos o acerto do lote com você, número por número.",
 "cana": "Não é só explicar o Consecana. Nós conferimos o pagamento da usina com o seu ATR.",
 "madeira": "Não é só o preço da tora. Chega o inventário do talhão, as propostas por sortimento e o contrato de corte organizado.",
 "mel": "Você fala o que colheu. Volta a produção por florada, o preço certo do pote e o post para vender.",
 "agroindustria": "Não é só a receita. Chega o custo de cada produto, os pedidos do dia e a apresentação para o distribuidor.",
 "tecnicos": "Você grava o áudio no carro. O relatório chega antes de você voltar para casa.",
 "estudantes": "Não é só resumo. Chega o relatório de estágio organizado e os slides da banca.",
 "creators": "Não é só ideia de post. Chega o roteiro pronto para gravar, a legenda e a proposta para a marca.",
 "vender-producao": "Não é só a cotação. Chega a contraproposta pronta para mandar.",
 "imposto-papelada": "Não é só explicar o imposto. Nós mostramos quanto saiu da sua nota e por quê.",
 "contratos": "Não é só explicar a lei. Nós mostramos o que falta no seu contrato.",
 "controle-custos": "Não é só falar de custo. Chega o custo real por hectare, com juros e taxas, e onde dá para economizar.",
 "credito-rural": "Não é só explicar as linhas. Chega a simulação das parcelas e a lista de documentos para levar ao banco.",
 "equipe": "Você fala quem trabalhou. Volta a folha da semana somada e o combinado por escrito.",
 "instagram": "Não é só dica de rede social. Chega o post com legenda, o roteiro do reels e a bio que vende.",
 "clima-safra": "Não é só a previsão. Chega a janela certa para plantar, pulverizar e colher na sua propriedade.",
 "cobranca": "Você fala quem está devendo. Volta a lista organizada e a mensagem de cobrança pronta para mandar.",
 "licencas-ambientais": "Não é só explicar a lei. Chega a lista do que pedir e o prazo de cada documento.",
 "planilha": "Você fala os números. A planilha volta pronta para baixar.",
 "clima": "Você não precisa perguntar. O aviso chega antes da chuva, da geada e da janela certa.",
 "campo": "Você grava o áudio no fim da visita. Volta o relatório em PDF com as suas fotos.",
 "agronomo": "Não é só a resposta. Chega o que fazer agora e quando chamar o técnico.",
 "vendas": "Não é só a cotação. Chega a proposta e a contraproposta prontas para mandar.",
 "viral": "Não é só ideia. Chega o roteiro com gancho, cortes e legenda prontos para gravar.",
 "vitrine": "Não é só dica. Chega o post com imagem, legenda e a bio do perfil.",
 "apresenta": "Você manda os números. Voltam os slides prontos para a reunião.",
 "juridico": "Não é só explicar a lei. Nós mostramos o que falta no seu contrato e o que perguntar antes de assinar.",
 "contabil": "Você manda as notas. Volta o livro caixa organizado e o pacote pronto para o contador.",
}

FAQ_DIF = ("Qual a diferença da Germo para outras IAs do agro?",
 "As outras IAs respondem as suas dúvidas, e isso é ótimo. Os ajudantes da Germo vão além: você pede e recebe o trabalho pronto, seja a planilha, o relatório em PDF, o contrato revisado ou a proposta para o comprador. Você só confere e usa.")


def selo(k, mk, t=""):
    tl = t.lower()
    if 'mk tb' in mk and ("explicad" in tl or tl.startswith(("quando", "qual", "o que", "prazos", "linhas"))): return "Resumo pronto no seu WhatsApp"
    if 'mk tb' in mk or 'mk ct2' in mk: return "Planilha pronta para baixar"
    if 'mk docm ctr' in mk: return "Análise pronta em PDF"
    if 'mk docm' in mk: return "PDF pronto para enviar"
    if 'mk sld' in mk: return "Slides prontos para apresentar"
    if 'mk igp' in mk: return "Post pronto para publicar"
    if 'mk reel' in mk: return "Roteiro pronto para gravar"
    if 'mk dias' in mk: return "Aviso direto no seu WhatsApp"
    if k in ("vendas", "campo", "juridico", "contabil"): return "Mensagem pronta para mandar"
    return "Chega pronto no seu WhatsApp"
