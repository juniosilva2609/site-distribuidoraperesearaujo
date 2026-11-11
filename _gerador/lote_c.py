# -*- coding: utf-8 -*-
"""Lote C: datas, encerramento (dezembro) e conteúdo leve."""
from dpa import *
import random
random.seed(7)
def luzes(n=46, h=1350):
    s = ""
    for _ in range(n):
        x, y, r = random.randint(0, 1080), random.randint(0, h), random.randint(6, 26)
        cor = random.choice(["215,20,26", "255,255,255", "255,196,90"])
        s += f'<i style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;border-radius:50%;background:rgba({cor},{random.uniform(.18,.7):.2f});filter:blur({random.choice([0,1,3,6])}px)"></i>'
    return s
def festa(meio, h=1350, st=False):
    base = story(meio) if st else tela(meio)
    return base.replace('<img class="globo" src="mark.png">', luzes(60 if st else 46, 1920 if st else 1350) + '<img class="globo" src="mark.png">', 1)
def st(arq, k, titulo, corpo, botao=""):
    b = f'<div style="text-align:center;margin-top:70px"><span class="btn">{botao}</span></div>' if botao else ""
    return (f"out/c/{arq}.jpg", story(f'<div class="k" style="text-align:center">{k}</div><h1 style="text-align:center;font-size:100px">{titulo}</h1><p style="text-align:center;margin-top:46px">{corpo}</p>{b}'), "story")
F4320 = "Fonte: Lei nº 4.320/1964, art. 36."
pecas = [
 ("out/c/2026-12-01_post_agenda_dezembro_compras_publicas.jpg", tela('<div class="k">Agenda de dezembro</div><h2 style="font-size:66px">Datas que o setor de compras <b>não pode perder</b></h2><div class="card"><h3>4/12</h3><p>Limite de empenho federal (despesas primárias discricionárias)</p></div><div class="card"><h3>25/12</h3><p>Natal (feriado nacional)</p></div><div class="card"><h3>31/12</h3><p>Fim do exercício financeiro de 2026</p></div><div class="fonte">Fontes: Decreto nº 12.846/2026, art. 16; Lei nº 4.320/1964, art. 34. Estados e Municípios têm prazos próprios: confira o decreto do seu ente.</div>'), "feed"),
 ("out/c/2026-12-09_post_dia_contra_corrupcao.jpg", tela('<div class="k">9 de dezembro</div><h1 style="font-size:86px">Dia Internacional contra a <mark>Corrupção</mark></h1><div class="linha"></div><p>Compra pública bem feita é a que qualquer pessoa pode conferir: edital claro, proposta documentada, nota fiscal e entrega comprovada.</p><p style="margin-top:24px"><b>Transparência é o nosso jeito de trabalhar.</b></p>'), "feed"),
]
T = 5
rp = [
 tela('<div class="k">Em 1 minuto</div><h1>O que são <mark>restos a pagar</mark>?</h1><div class="linha"></div><p>O termo que mais aparece em dezembro, explicado de forma simples.</p>', f"1/{T}", arr=True),
 tela('<div class="k">A definição</div><h2>Empenhou, mas <b>não pagou</b> até 31/12</h2><div class="linha"></div><p>“Consideram-se Restos a Pagar as despesas <b>empenhadas mas não pagas até o dia 31 de dezembro</b>.”</p><div class="fonte">'+F4320+'</div>', f"2/{T}", claro=True),
 tela('<h2 style="font-size:62px">Existem <b>dois tipos</b></h2><div class="card"><h3>Processados</h3><p>A mercadoria ou o serviço já foi entregue e conferido (despesa liquidada). Falta só o pagamento.</p></div><div class="card"><h3>Não processados</h3><p>O empenho existe, mas a entrega ainda não foi conferida (despesa não liquidada).</p></div><div class="fonte">'+F4320+'</div>', f"3/{T}"),
 tela('<div class="k">Por que importa</div><h2>Entrega no prazo <b>protege</b> o empenho</h2><div class="linha"></div><p>Quando o fornecedor entrega e o órgão liquida dentro do exercício, o processo fecha sem pendência para o ano seguinte.</p><p style="margin-top:24px">Cada ente define em decreto os prazos e as regras de inscrição.</p>', f"4/{T}", claro=True),
 cta("Precisa receber ainda em <b>2026</b>?", "Envie o edital, o item ou o termo de referência. A DPA monta a proposta com você.", n=f"5/{T}"),
]
pecas += [(f"out/c/2026-12-16_carrossel_restos_a_pagar_{i}.jpg", h, "feed") for i, h in enumerate(rp, 1)]
T = 5
ck = [
 tela('<div class="k">Última semana útil</div><h1>Checklist para <mark>fechar o ano</mark> sem pendência</h1><div class="linha"></div><p>Cinco conferências rápidas para o setor de compras.</p>', f"1/{T}", arr=True),
 tela('<h2>Antes de <b>empenhar</b></h2><div class="it"><i>1</i><span>Saldo orçamentário conferido na dotação certa.</span></div><div class="it"><i>2</i><span>Ata de registro de preços dentro da vigência.</span></div><div class="it"><i>3</i><span>Documentação do fornecedor em dia.</span></div>', f"2/{T}", claro=True),
 tela('<h2>Depois de <b>empenhar</b></h2><div class="it"><i>4</i><span>Nota de empenho enviada ao fornecedor com local e contato de entrega.</span></div><div class="it"><i>5</i><span>Recebimento conferido e atestado assim que a mercadoria chegar.</span></div>', f"3/{T}"),
 tela('<div class="k">Lembrete</div><h2>O prazo é o do <mark>seu ente</mark></h2><div class="linha"></div><p>União, Estados e Municípios publicam as próprias datas de encerramento. Confira o decreto ou a portaria que vale para o seu órgão.</p>', f"4/{T}", claro=True),
 cta("Conte com a DPA para <b>fechar o ano</b>", "Envie o edital, o item ou o termo de referência. A DPA monta a proposta com você.", n=f"5/{T}"),
]
pecas += [(f"out/c/2026-12-21_carrossel_checklist_fechar_o_ano_{i}.jpg", h, "feed") for i, h in enumerate(ck, 1)]
pecas += [
 ("out/c/2026-12-24_post_feliz_natal.jpg", festa('<div class="k">Distribuidora Peres &amp; Araújo</div><h1 style="font-size:150px">Feliz <b>Natal</b></h1><div class="linha"></div><p>A todos os servidores, pregoeiros, fiscais e equipes de compras que fazem o serviço público acontecer: <b>obrigado pela confiança em 2026.</b></p>'), "feed"),
 ("out/c/2026-12-25_story_feliz_natal.jpg", festa('<h1 style="text-align:center;font-size:170px">Feliz <b>Natal</b></h1><p style="text-align:center;margin-top:50px">Paz, saúde e boas festas para você e sua família.</p>', st=True), "story"),
 ("out/c/2026-12-31_post_obrigado_2026.jpg", festa('<div class="k">31 de dezembro</div><h1 style="font-size:120px">Obrigado, <mark>2026</mark></h1><div class="linha"></div><p>Mais um ano ao lado de quem compra para o setor público. Que <b>2027</b> venha com bons processos, entregas no prazo e muito trabalho bem feito.</p>'), "feed"),
 ("out/c/2027-01-01_story_feliz_2027.jpg", festa('<div class="num" style="text-align:center;font-size:440px">2027</div><h1 style="text-align:center;font-size:110px">Feliz <b>Ano Novo</b></h1><p style="text-align:center;margin-top:44px">Orçamento novo, plano de contratações novo. Vamos juntos.</p>', st=True), "story"),
 st("2026-11-27_story_ata_registro_precos", "Você sabia?", "Preço de ata <mark>não muda</mark> na Black Friday", "Na ata de registro de preços, o valor fica definido em licitação durante a vigência."),
 st("2026-12-03_story_amanha_limite_federal", "Amanhã • 4/12", "Limite de <mark>empenho</mark> federal", "Despesas primárias discricionárias. Decreto nº 12.846/2026, art. 16."),
 st("2026-12-08_story_pergunta_decreto", "Pergunta rápida", "Seu órgão já tem a <mark>data</mark> de encerramento?", "Responda este story com a cidade ou o órgão. A gente ajuda a planejar a entrega.", "Responder"),
 st("2026-12-11_story_saldo", "Dezembro", "Ainda tem <mark>saldo</mark> para empenhar?", "Envie o edital, o item ou o termo de referência pelo WhatsApp da bio.", "Enviar edital"),
 st("2026-12-15_story_reforma_serie", "Série no perfil", "Reforma tributária nas <mark>compras públicas</mark>", "4 posts com a fonte de cada regra. Toque no perfil e salve."),
 st("2026-12-17_story_restos_a_pagar", "Novo post no perfil", "Restos a pagar em <mark>1 minuto</mark>", "Processados e não processados: a diferença que todo setor de compras precisa saber."),
 st("2026-12-22_story_ultima_semana", "Última semana útil", "Vamos <mark>fechar o ano</mark> juntos?", "Checklist no perfil. Dúvida no processo? Chame no WhatsApp da bio.", "Falar com a DPA"),
 st("2026-12-31_story_ate_2027", "31 de dezembro", "Até <mark>2027</mark>", "Obrigado a cada órgão que confiou na DPA neste ano."),
]
render(pecas)
reel("out/c/2026-11-28_reel_3_passos_nao_perder_saldo.mp4", [
 (2.6, '<div class="k an">Fim de ano</div><h1 class="an" style="--d:.25s"><mark>3 passos</mark> para não perder o saldo do orçamento</h1>'),
 (2.8, '<div class="num zoom">1</div><h2 class="an" style="--d:.4s">Levante o <b>saldo</b> que ainda pode virar empenho</h2>'),
 (2.8, '<div class="num zoom">2</div><h2 class="an" style="--d:.4s">Confira a <b>ata</b> vigente e peça a cotação</h2>'),
 (2.8, '<div class="num zoom">3</div><h2 class="an" style="--d:.4s">Emita o <b>empenho</b> antes do prazo do seu ente</h2>'),
 (3.2, '<h1 class="an" style="font-size:104px">Sem empenho, <mark>não há</mark> compra</h1><p class="an" style="--d:.5s;margin-top:36px;font-size:38px">Lei nº 4.320/1964, art. 60</p><p class="an" style="--d:.9s;margin-top:40px">Envie seu edital para a DPA.</p>'),
], "musica/Funkorama.mp3", inicio=12)
reel("out/c/2026-12-12_reel_sinais_de_dezembro.mp4", [
 (2.6, '<div class="k an">Quem é do setor de compras entende</div><h1 class="an" style="--d:.25s"><mark>3 sinais</mark> de que dezembro chegou</h1>'),
 (2.7, '<div class="num zoom">1</div><h2 class="an" style="--d:.4s">A palavra do mês é <b>“saldo”</b></h2>'),
 (2.7, '<div class="num zoom">2</div><h2 class="an" style="--d:.4s">Todo prazo virou <b>“até sexta”</b></h2>'),
 (2.7, '<div class="num zoom">3</div><h2 class="an" style="--d:.4s">O calendário só tem uma data: <b>31/12</b></h2>'),
 (3.3, '<h1 class="an" style="font-size:104px">A gente ajuda a <mark>fechar o ano</mark></h1><p class="an" style="--d:.5s;margin-top:40px">Marque quem está nessa correria.</p>'),
], "musica/Too_Cool.mp3", inicio=8)
reel("out/c/2026-12-19_reel_2027_tres_mudancas.mp4", [
 (2.6, '<div class="k an">Reforma tributária</div><h1 class="an" style="--d:.25s"><mark>2027</mark> vem aí: 3 mudanças nas compras públicas</h1>'),
 (3.0, '<div class="num zoom">1</div><h2 class="an" style="--d:.4s">A <b>CBS</b> entra em vigor e PIS/Cofins são extintos</h2><p class="an" style="--d:.8s;margin-top:20px;font-size:36px">EC nº 132/2023, ADCT art. 126</p>'),
 (3.0, '<div class="num zoom">2</div><h2 class="an" style="--d:.4s">Compra pública com <b>alíquota reduzida</b></h2><p class="an" style="--d:.8s;margin-top:20px;font-size:36px">LC nº 214/2025, art. 472</p>'),
 (3.0, '<div class="num zoom">3</div><h2 class="an" style="--d:.4s">O <b>IBS</b> da compra fica com o ente que compra</h2><p class="an" style="--d:.8s;margin-top:20px;font-size:36px">LC nº 214/2025, arts. 372 e 473</p>'),
 (3.2, '<h1 class="an" style="font-size:104px">Salve para o <mark>planejamento</mark> de 2027</h1><p class="an" style="--d:.5s;margin-top:40px">Série completa no perfil da DPA.</p>'),
], "musica/Werq.mp3", inicio=62)
reel("out/c/2026-12-24_reel_feliz_natal.mp4", [
 (3.0, '<div class="k an">Distribuidora Peres &amp; Araújo</div><h1 class="an" style="--d:.3s;font-size:170px">Feliz <b>Natal</b></h1>'),
 (3.6, '<h2 class="an">A quem faz o serviço público acontecer:</h2><p class="an" style="--d:.7s;margin-top:36px">servidores, pregoeiros, fiscais e equipes de compras.</p>'),
 (3.6, '<h1 class="an" style="font-size:110px">Obrigado pela <mark>confiança</mark> em 2026</h1><p class="an" style="--d:.6s;margin-top:40px">Boas festas!</p>'),
], "musica/Wholesome.mp3", inicio=30)
