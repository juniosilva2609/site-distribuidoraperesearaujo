# -*- coding: utf-8 -*-
"""Lote B: reforma tributária (EC 132/2023, LC 214/2025, Decreto 12.955/2026) -- fatos conferidos em 11/11/2026."""
from dpa import *
def car(prefixo, telas):
    return [(f"out/b/{prefixo}_{i}.jpg", h, "feed") for i, h in enumerate(telas, 1)]
def novo(data, titulo, sub):
    return (f"out/b/{data}_story_novo_post.jpg", story(f'<div class="k" style="text-align:center">Novo post no perfil</div><h1 style="text-align:center;font-size:100px">{titulo}</h1><p style="text-align:center;margin-top:50px">{sub}</p>'), "story")
LT = '''<div style="margin-top:18px">%s</div>'''
def linha(ano, txt, cor="#d7141a"):
    return f'<div style="display:flex;gap:30px;align-items:center;margin-top:26px"><div style="font-family:Anton;font-size:84px;color:{cor};width:250px;flex:none;line-height:1">{ano}</div><div style="font-size:35px;line-height:1.3;font-weight:500">{txt}</div></div>'
pecas = []
# ---- B1: visão geral (16/11)
T = 7
pecas += car("2026-11-16_carrossel_reforma_tributaria_o_que_muda", [
 tela('<div class="k">Reforma tributária</div><h1>O que muda para quem <mark>compra</mark> e <b>vende</b> ao setor público</h1><div class="linha"></div><p>Sem juridiquês e com a fonte de cada informação. Salve para consultar.</p>', f"1/{T}", arr=True),
 tela('<div class="k">O básico</div><h2>Saem quatro tributos, entram <b>dois</b></h2><div class="card"><h3>CBS</h3><p>federal: substitui PIS e Cofins</p></div><div class="card"><h3>IBS</h3><p>de Estados e Municípios: substitui ICMS e ISS</p></div><p style="margin-top:28px;font-size:34px">O IPI tem as alíquotas reduzidas a zero, exceto para produtos da Zona Franca de Manaus.</p><div class="fonte">Fonte: Emenda Constitucional nº 132/2023 (ADCT, arts. 126 e 129).</div>', f"2/{T}", claro=True),
 tela('<div class="k">Linha do tempo</div><h2 style="font-size:60px">A mudança é <b>gradual</b></h2>'+linha("2026","Ano de teste: CBS de 0,9% e IBS de 0,1%.")+linha("2027","CBS passa a valer. PIS e Cofins são extintos.")+linha("2029-32","ICMS e ISS caem 10% a cada ano e o IBS sobe.")+linha("2033","ICMS e ISS são extintos.")+'<div class="fonte">Fonte: EC nº 132/2023 (ADCT, arts. 125 a 129).</div>', f"3/{T}"),
 tela('<div class="k">2026: ano de teste</div><div class="num" style="font-size:230px">0,9% + 0,1%</div><h2 style="font-size:58px">CBS e IBS já aparecem na <b>nota fiscal</b></h2><p style="margin-top:26px;font-size:35px">Quem cumpre as obrigações acessórias fica <b>dispensado do recolhimento</b> neste ano. As alíquotas de teste não se aplicam ao Simples Nacional.</p><div class="fonte">Fonte: Lei Complementar nº 214/2025, arts. 343, 346 e 348.</div>', f"4/{T}", claro=True),
 tela('<div class="k">Compras públicas</div><h2>O setor público tem <mark>regra própria</mark></h2><div class="linha"></div><p>A lei traz um capítulo só para as <b>compras governamentais</b>: alíquotas reduzidas e imposto destinado ao ente que compra.</p><p style="margin-top:26px">Vamos explicar cada regra nos próximos posts.</p><div class="fonte">Fonte: Lei Complementar nº 214/2025, arts. 472 e 473.</div>', f"5/{T}"),
 tela('<h2>O que isso muda no <b>dia a dia</b></h2><div class="it"><i>1</i><span>Formação de preço nos editais a partir de 2027.</span></div><div class="it"><i>2</i><span>Nota fiscal com CBS e IBS destacados.</span></div><div class="it"><i>3</i><span>Contratos antigos podem pedir reequilíbrio.</span></div><div class="it"><i>4</i><span>Fornecedor preparado evita atraso no seu processo.</span></div>', f"6/{T}", claro=True),
 cta("Dúvida sobre o seu <b>edital</b>?", "Envie o edital, o item ou o termo de referência. A DPA monta a proposta com você.", n=f"7/{T}"),
])
pecas.append(novo("2026-11-16", "Reforma tributária e <mark>compras</mark> <b>públicas</b>", "O que muda para quem compra e para quem vende ao setor público."))
# ---- B2: CBS e o redutor (30/11)
T = 6
pecas += car("2026-11-30_carrossel_cbs_compras_publicas_2027", [
 tela('<div class="k">Reforma tributária • parte 2</div><h1>Em 2027 a <mark>CBS</mark> chega às <b>compras públicas</b></h1><div class="linha"></div><p>E vem com um redutor de alíquota. Entenda em 5 telas.</p>', f"1/{T}", arr=True),
 tela('<div class="k">A regra</div><h2>Compra de órgão público tem <b>alíquota reduzida</b></h2><div class="linha"></div><p>“Nas aquisições de bens e serviços por pessoa jurídica de direito público interno, as alíquotas do IBS e da CBS serão <b>reduzidas, de modo uniforme</b>, na proporção do redutor fixado.”</p><div class="fonte">Fonte: Lei Complementar nº 214/2025, art. 472 (redação da LC nº 227/2026).</div>', f"2/{T}", claro=True),
 tela('<div class="k">Atenção</div><h2>O redutor <mark>não vale</mark> para tudo</h2><p style="margin-top:30px">Ficam fora do redutor:</p><div class="it"><i>1</i><span>compras presenciais com dispensa de licitação;</span></div><div class="it"><i>2</i><span>operações com alíquotas nacionalmente uniformes;</span></div><div class="it"><i>3</i><span>aquisições de fornecedores do Simples Nacional ou MEI.</span></div><div class="fonte">Fonte: LC nº 214/2025, art. 472, parágrafo único.</div>', f"3/{T}"),
 tela('<div class="k">Para quem faz edital</div><h2>O preço de referência precisa <b>considerar o redutor</b></h2><div class="linha"></div><p>“Para fins da formação de preços nos editais de licitação, nas aquisições de bens e serviços, deverá ser considerada a aplicação do redutor.”</p><div class="fonte">Fonte: Decreto nº 12.955/2026 (Regulamento da CBS), art. 442, § 2º.</div>', f"4/{T}", claro=True),
 tela('<div class="k">E os números de 2027?</div><h2 style="font-size:62px">Ainda <mark>não estão</mark> fixados</h2><p style="margin-top:30px">O TCU <b>propôs</b> ao Senado:</p><div class="card"><h3>11,3%</h3><p>alíquota da CBS em 2027</p></div><div class="card"><h3>44,16%</h3><p>redutor nas compras públicas</p></div><p style="margin-top:26px;font-size:33px">São propostas. Quem fixa é o Senado, por resolução. Avisamos quando sair.</p><div class="fonte">Fonte: Agência Senado, 28/10/2026 e 10/11/2026.</div>', f"5/{T}"),
 cta("Seu edital de 2027 já considera a <b>CBS</b>?", "Fale com a DPA: acompanhamos a regra para formar preço certo com você.", n=f"6/{T}"),
])
pecas.append(novo("2026-11-30", "CBS nas <mark>compras</mark> públicas em <b>2027</b>", "Redutor de alíquota, exceções e formação de preço no edital."))
# ---- B3: IBS destinado a quem compra (07/12)
T = 6
pecas += car("2026-12-07_carrossel_ibs_fica_com_quem_compra", [
 tela('<div class="k">Reforma tributária • parte 3</div><h1>O imposto da compra pública fica com <mark>quem compra</mark></h1><div class="linha"></div><p>É a regra da destinação integral. Veja como funciona.</p>', f"1/{T}", arr=True),
 tela('<div class="k">A regra</div><h2>Arrecadação <b>100%</b> para o ente contratante</h2><div class="linha"></div><p>O IBS e a CBS sobre as compras da administração direta, autarquias e fundações públicas serão <b>“integralmente destinados ao ente federativo contratante”</b>.</p><div class="fonte">Fonte: Lei Complementar nº 214/2025, art. 473.</div>', f"2/{T}", claro=True),
 tela('<div class="k">Na prática</div><h2 style="font-size:60px">Como a lei faz isso</h2><div class="card"><h3>Compra do Estado</h3><p>CBS e IBS municipal vão a zero; o IBS estadual recebe a soma.</p></div><div class="card"><h3>Compra do Município</h3><p>CBS e IBS estadual vão a zero; o IBS municipal recebe a soma.</p></div><div class="card"><h3>Compra da União</h3><p>IBS vai a zero; a CBS recebe a soma.</p></div><div class="fonte">Fonte: LC nº 214/2025, art. 473, § 1º.</div>', f"3/{T}"),
 tela('<div class="k">Quando começa</div><h2 style="font-size:60px">Entra em <b>etapas</b></h2>'+linha("2026","Não se aplica (ano de teste).","#d7141a")+linha("2027","Vale integralmente para o IBS.")+linha("2029-32","CBS entra aos poucos nas compras de Estados e Municípios: de 10% a 40%.")+linha("2033","Vale integralmente também para a CBS.")+'<div class="fonte">Fonte: LC nº 214/2025, art. 372.</div>', f"4/{T}", claro=True),
 tela('<div class="k">Detalhe importante</div><h2>O imposto nasce no <mark>pagamento</mark></h2><div class="linha"></div><p>Nas compras públicas sujeitas a essa regra, o fato gerador ocorre <b>“no momento em que se realiza o pagamento”</b>, e não na emissão da nota.</p><div class="fonte">Fonte: LC nº 214/2025, art. 10, § 2º.</div>', f"5/{T}"),
 cta("Quer entender o impacto no seu <b>processo</b>?", "Envie o edital, o item ou o termo de referência. A DPA monta a proposta com você.", n=f"6/{T}"),
])
pecas.append(novo("2026-12-07", "O imposto fica com <mark>quem compra</mark>", "IBS e CBS nas compras públicas: a regra da destinação integral."))
# ---- B4: reequilíbrio (14/12)
T = 6
pecas += car("2026-12-14_carrossel_reequilibrio_contratos_reforma", [
 tela('<div class="k">Reforma tributária • parte 4</div><h1>Contrato antigo, <mark>imposto novo</mark>. E agora?</h1><div class="linha"></div><p>A lei prevê o reequilíbrio econômico-financeiro. Veja as regras.</p>', f"1/{T}", arr=True),
 tela('<div class="k">Quem tem direito</div><h2>Contratos firmados <b>antes</b> da lei</h2><div class="linha"></div><p>Vale para contratos administrativos anteriores à Lei Complementar nº 214/2025 e para os assinados depois, mas com <b>proposta apresentada antes</b> da vigência da lei.</p><div class="fonte">Fonte: LC nº 214/2025, art. 373.</div>', f"2/{T}", claro=True),
 tela('<div class="k">O que diz a lei</div><h2 style="font-size:62px">Equilíbrio <b>restabelecido</b></h2><div class="linha"></div><p>Os contratos “serão ajustados para assegurar o restabelecimento do equilíbrio econômico-financeiro em razão da alteração da carga tributária efetiva”, quando o desequilíbrio <b>for comprovado</b>.</p><p style="margin-top:24px;font-size:34px">Vale para os dois lados: se a carga cair, a Administração revisa de ofício.</p><div class="fonte">Fonte: LC nº 214/2025, arts. 374 e 375.</div>', f"3/{T}"),
 tela('<h2>Como a contratada <b>pede</b></h2><div class="it"><i>1</i><span>Em procedimento administrativo específico.</span></div><div class="it"><i>2</i><span>Durante a vigência do contrato e antes de eventual prorrogação.</span></div><div class="it"><i>3</i><span>Com cálculo que comprove o desequilíbrio.</span></div><div class="it"><i>4</i><span>A cada alteração tributária ou de uma vez para todo o período.</span></div><div class="fonte">Fonte: LC nº 214/2025, art. 376.</div>', f"4/{T}", claro=True),
 tela('<div class="k">Prazo de resposta</div><div class="num" style="font-size:300px">90 dias</div><h2 style="font-size:58px">para a Administração <b>decidir</b></h2><p style="margin-top:26px;font-size:36px">Contados do protocolo e prorrogáveis uma única vez por igual período.</p><div class="fonte">Fonte: LC nº 214/2025, art. 376, § 1º.</div>', f"5/{T}"),
 cta("Fornecedor que acompanha a regra <b>evita surpresa</b>", "A DPA atende órgãos públicos desde 2015. Envie seu edital.", n=f"6/{T}"),
])
pecas.append(novo("2026-12-14", "Contrato antigo, <mark>imposto novo</mark>", "Reequilíbrio de contratos administrativos na reforma tributária."))
# ---- B5: NF-e (10/12)
pecas.append(("out/b/2026-12-10_post_nfe_cbs_ibs.jpg", tela('<div class="k">Você sabia?</div><h1 style="font-size:84px">A nota fiscal já vem com <mark>CBS</mark> e <b>IBS</b></h1><div class="linha"></div><p>Desde <b>3 de agosto de 2026</b> a NF-e traz os campos dos novos tributos. Para empresas do Simples Nacional, a exigência começa em <b>1º de janeiro de 2027</b>.</p><div class="fonte">Fonte: Ato Conjunto RFB/CGIBS nº 4, de 30/07/2026, art. 1º.</div>'), "feed"))
render(pecas)
# ---- Reels
reel("out/b/2026-11-21_reel_reforma_tributaria_linha_do_tempo.mp4", [
 (2.6, '<div class="k an">Reforma tributária</div><h1 class="an" style="--d:.25s">A linha do tempo em <mark>15 segundos</mark></h1>'),
 (2.6, '<div class="num zoom" style="font-size:400px">2026</div><h2 class="an" style="--d:.4s">Ano de <b>teste</b></h2><p class="an" style="--d:.7s;margin-top:20px">CBS 0,9% + IBS 0,1%</p>'),
 (2.6, '<div class="num zoom" style="font-size:400px">2027</div><h2 class="an" style="--d:.4s">A <b>CBS</b> entra em vigor</h2><p class="an" style="--d:.7s;margin-top:20px">PIS e Cofins são extintos</p>'),
 (2.6, '<div class="num zoom" style="font-size:300px">2029-32</div><h2 class="an" style="--d:.4s">ICMS e ISS <b>caem</b> 10% ao ano</h2><p class="an" style="--d:.7s;margin-top:20px">O IBS sobe na mesma medida</p>'),
 (2.4, '<div class="num zoom" style="font-size:400px">2033</div><h2 class="an" style="--d:.4s">ICMS e ISS são <b>extintos</b></h2><p class="an" style="--d:.7s;margin-top:20px;font-size:36px">EC nº 132/2023, ADCT arts. 125 a 129</p>'),
 (3.2, '<h1 class="an" style="font-size:100px">Compra pública tem <mark>regra própria</mark></h1><p class="an" style="--d:.5s;margin-top:40px">Siga a DPA: explicamos cada etapa.</p>'),
], "musica/Upbeat_Forever.mp3", inicio=14)
reel("out/b/2026-12-05_reel_imposto_fica_com_quem_compra.mp4", [
 (2.8, '<div class="k an">Reforma tributária</div><h1 class="an" style="--d:.25s">Para onde vai o <mark>imposto</mark> da compra pública?</h1>'),
 (3.0, '<div class="num zoom" style="font-size:420px">100%</div><h2 class="an" style="--d:.45s">para o ente que <b>compra</b></h2><p class="an" style="--d:.8s;margin-top:22px;font-size:36px">LC nº 214/2025, art. 473</p>'),
 (3.2, '<h2 class="esq">O <b>Estado</b> comprou?</h2><p class="an" style="--d:.4s;margin-top:26px">O IBS fica com o Estado.</p><h2 class="esq" style="--d:1.1s;margin-top:70px">O <b>Município</b> comprou?</h2><p class="an" style="--d:1.5s;margin-top:26px">O IBS fica com o Município.</p>'),
 (2.6, '<div class="num zoom" style="font-size:400px">2027</div><h2 class="an" style="--d:.4s">é quando a regra começa para o <b>IBS</b></h2><p class="an" style="--d:.8s;margin-top:22px;font-size:36px">LC nº 214/2025, art. 372</p>'),
 (3.0, '<h1 class="an" style="font-size:104px">Salve e mande para o <mark>setor de compras</mark></h1><p class="an" style="--d:.5s;margin-top:40px">Mais no perfil da DPA.</p>'),
], "musica/Protofunk.mp3", inicio=10)
