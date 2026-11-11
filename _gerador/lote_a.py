# -*- coding: utf-8 -*-
"""Lote A: encerramento do exercício 2026 (fatos conferidos em 11/11/2026)."""
from dpa import *
F1 = "Fonte: Lei nº 4.320/1964, arts. 34, 35, 36 e 60."
F2 = "Fonte: Decreto federal nº 12.846, de 12/02/2026, art. 16."
F3 = "Fonte: Decreto estadual (MG) nº 49.118, de 03/11/2025."
T = 7
c = [
 tela('<div class="k">Encerramento do exercício 2026</div><h1>O orçamento do seu órgão tem <mark>data</mark> para <b>acabar</b></h1><div class="linha"></div><p>O que o setor de compras precisa saber antes de dezembro. Salve este post.</p>', f"1/{T}", arr=True),
 tela('<div class="num">31/12</div><h2>O ano do orçamento é o <b>ano civil</b></h2><p style="margin-top:30px">O exercício financeiro coincide com o ano civil. E pertencem ao exercício as despesas <b>nele legalmente empenhadas</b>.</p><div class="fonte">'+F1+'</div>', f"2/{T}", claro=True),
 tela('<div class="k">Regra de ouro</div><h2>Sem empenho, <mark>não há</mark> compra</h2><div class="linha"></div><p>A lei é direta: <b>“É vedada a realização de despesa sem prévio empenho.”</b></p><p style="margin-top:26px">Saldo que não foi empenhado dentro do exercício não vira entrega no ano seguinte.</p><div class="fonte">Lei nº 4.320/1964, art. 60.</div>', f"3/{T}"),
 tela('<div class="k">Governo Federal</div><div class="num" style="font-size:260px">4 DEZ</div><h2 style="font-size:60px">é o limite de empenho das despesas <b>primárias discricionárias</b></h2><p style="margin-top:26px;font-size:35px">Para as demais despesas, o limite é 31/12/2026. O Ministério do Planejamento pode autorizar prazo posterior.</p><div class="fonte">'+F2+'</div>', f"4/{T}", claro=True),
 tela('<div class="k">Minas Gerais</div><h2>E no <b>Estado</b>?</h2><div class="linha"></div><p>Todo ano um decreto fixa os prazos. Em <b>2025</b>, foi assim:</p><div class="card"><h3>31/12/2025</h3><p>limite para emissão de empenhos</p></div><div class="card"><h3>29/12/2025</h3><p>limite para ordens de pagamento no Siafi-MG</p></div><p style="margin-top:28px;font-size:34px">O decreto de 2026 nós estamos acompanhando e avisamos aqui assim que sair.</p><div class="fonte">'+F3+'</div>', f"5/{T}"),
 tela('<h2>O que fazer <b>agora</b></h2><div class="it"><i>1</i><span>Levante o saldo orçamentário que ainda pode virar empenho.</span></div><div class="it"><i>2</i><span>Confira as atas de registro de preços vigentes e os itens pendentes.</span></div><div class="it"><i>3</i><span>Peça a cotação e a documentação do fornecedor com antecedência.</span></div><div class="it"><i>4</i><span>Emita o empenho antes do prazo do seu ente e combine a entrega.</span></div>', f"6/{T}", claro=True),
 cta("Seu órgão tem saldo para <b>empenhar</b>?", "Envie o edital, o item ou o termo de referência. A DPA monta a proposta com você.", n=f"7/{T}"),
]
pecas = [(f"out/a/2026-11-23_carrossel_encerramento_exercicio_{i}.jpg", h, "feed") for i, h in enumerate(c, 1)]
pecas += [
 ("out/a/2026-11-23_story_novo_post_encerramento.jpg", story('<div class="k" style="text-align:center">Novo post no perfil</div><h1 style="text-align:center">O orçamento tem <mark>data</mark> para <b>acabar</b></h1><p style="text-align:center;margin-top:50px">Guia do encerramento do exercício 2026 para o setor de compras.</p>'), "story"),
 ("out/a/2026-12-02_story_faltam_2_dias.jpg", story('<div class="k" style="text-align:center">Governo Federal</div><div class="num" style="text-align:center;font-size:520px">2</div><h1 style="text-align:center;font-size:92px">dias para o <mark>limite</mark> de empenho</h1><p style="text-align:center;margin-top:44px">4/12/2026: despesas primárias discricionárias.<br>Decreto nº 12.846/2026, art. 16.</p>'), "story"),
 ("out/a/2026-12-04_post_e_hoje_empenho_federal.jpg", tela('<div class="k">É hoje • 4 de dezembro</div><h1>Último dia de <mark>empenho</mark> no Governo <b>Federal</b></h1><div class="linha"></div><p>Vale para as despesas primárias discricionárias. Para as demais, o limite é 31/12.</p><div class="fonte">'+F2+'</div>'), "feed"),
 ("out/a/2026-11-27_post_black_friday_setor_publico.jpg", tela('<div class="k">Black Friday</div><h1>No setor público não existe <mark>promoção</mark>.<br>Existe <b>preço registrado</b>.</h1><div class="linha"></div><p>Na ata de registro de preços, preço e condições já saem definidos em licitação e valem durante toda a vigência da ata.</p>'), "feed"),
]
render(pecas)
reel("out/a/2026-11-14_reel_orcamento_tem_data.mp4", [
 (2.6, '<div class="k an">Setor de compras</div><h1 class="an" style="--d:.25s">O orçamento de <b>2026</b> tem <mark>data</mark> para acabar</h1>'),
 (2.8, '<div class="num zoom" style="font-size:380px">31/12</div><h2 class="an" style="--d:.45s">O exercício financeiro é o <b>ano civil</b></h2><p class="an" style="--d:.8s;margin-top:24px;font-size:36px">Lei nº 4.320/1964, art. 34</p>'),
 (3.0, '<h1 class="an" style="font-size:104px">Sem <mark>empenho</mark>, não há <b>compra</b></h1><p class="an" style="--d:.5s;margin-top:40px">“É vedada a realização de despesa sem prévio empenho.”</p><p class="an" style="--d:.9s;margin-top:20px;font-size:36px">Lei nº 4.320/1964, art. 60</p>'),
 (3.2, '<div class="k an">Governo Federal</div><div class="num zoom" style="--d:.2s;font-size:340px">4 DEZ</div><h2 class="an" style="--d:.6s;font-size:66px">limite de empenho das despesas <b>discricionárias</b></h2><p class="an" style="--d:1s;margin-top:24px;font-size:36px">Decreto nº 12.846/2026, art. 16</p>'),
 (3.4, '<h1 class="an">Tem saldo?<br><b>Empenhe</b> a tempo.</h1><div class="barra" style="--d:.5s;width:92px;height:8px;background:#d7141a;margin:44px 0"></div><p class="an" style="--d:.7s">Envie seu edital para a DPA.<br>WhatsApp na bio.</p>'),
], "musica/Werq.mp3", inicio=31)
