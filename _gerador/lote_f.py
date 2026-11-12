# -*- coding: utf-8 -*-
"""Lote F (12/11/2026): dias vazios de 22/11/2026 a 29/01/2027 -- vendas, atualidades e utilidade.
Fontes: site oficial da DPA (linhas, fundação, estados, documentos); Lei 14.133/2021 arts. 6º XLI, 12 VII e §1º,
75 I e II, 84, 86 §§4º, 5º e 8º, 182; Decreto 12.807/2025 (valores 2026); Decreto 11.462/2023 art. 32."""
from dpa import *
import random
random.seed(11)
O = "out/f/"
def luzes(n=46, h=1350):
    s = ""
    for _ in range(n):
        x, y, r = random.randint(0, 1080), random.randint(0, h), random.randint(6, 26)
        cor = random.choice(["215,20,26", "255,255,255", "255,196,90"])
        s += f'<i style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;border-radius:50%;background:rgba({cor},{random.uniform(.18,.7):.2f});filter:blur({random.choice([0,1,3,6])}px)"></i>'
    return s
def festa(h):
    return h.replace('<img class="globo" src="mark.png">', luzes() + '<img class="globo" src="mark.png">', 1)
def chips(*itens):
    return '<div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:34px">' + "".join(
        f'<span style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:40px;padding:14px 26px;font-size:30px;font-weight:700">{i}</span>' for i in itens) + '</div>'
def chamada(t="Envie o item do seu edital pelo WhatsApp da bio"):
    return f'<p style="margin-top:44px;font-size:32px;font-weight:700;color:#fff">→ {t}</p>'
def st(arq, k, titulo, corpo, botao="", extra=""):
    b = f'<div style="text-align:center;margin-top:70px"><span class="btn">{botao}</span></div>' if botao else ""
    return (O + arq + ".jpg", story(f'{extra}<div class="k" style="text-align:center">{k}</div><h1 style="text-align:center;font-size:100px">{titulo}</h1><p style="text-align:center;margin-top:46px">{corpo}</p>{b}'), "story")
def carrossel(nome, telas):
    return [(f"{O}{nome}_{i}.jpg", h, "feed") for i, h in enumerate(telas, 1)]

pecas = [
 (O + "2026-11-29_post_climatizacao_verao.jpg", tela(
   '<div class="k">O verão começa em 21 de dezembro</div><h1>Seu atendimento <mark>aguenta o calor</mark>?</h1><div class="linha"></div>'
   '<p>Ar-condicionado <b>split e portátil</b>, de <b>9 mil a mais de 24 mil BTUs</b>, para salas, postos de trabalho e atendimento ao público.</p>'
   + chips("9.000 BTUs", "12.000 BTUs", "18.000 BTUs", "24.000+ BTUs") + chamada()), "feed"),
 (O + "2026-12-23_post_lista_papai_noel.jpg", festa(tela(
   '<div class="k">Querido Papai Noel,</div><h2 style="font-size:66px">O setor de compras <b>se comportou</b> em 2026 e só pede:</h2>'
   '<div class="it"><i>1</i><span>Pregão sem recurso</span></div><div class="it"><i>2</i><span>Fornecedor que entrega no prazo</span></div>'
   '<div class="it"><i>3</i><span>Nota fiscal certa de primeira</span></div><div class="it"><i>4</i><span>Saldo sobrando no orçamento</span></div>'
   '<p style="margin-top:44px;font-size:40px">Os itens <b>2 e 3</b> a DPA já entrega.</p>')), "feed"),
 (O + "2026-12-30_post_cotacao_pronta_2027.jpg", tela(
   '<div class="k">Primeira compra de 2027</div><h1>Deixe a <mark>cotação pronta</mark> antes de janeiro</h1><div class="linha"></div>'
   '<p>Mande a lista agora e comece o ano com a proposta no padrão do seu processo.</p>'
   '<div class="it"><i>✓</i><span>Mais de 40 linhas no mesmo CNPJ</span></div><div class="it"><i>✓</i><span>Documentação sempre regular</span></div>'
   '<div class="it"><i>✓</i><span>NF-e própria, emitida na venda</span></div>'), "feed"),
 (O + "2027-01-04_post_orcamento_novo.jpg", tela(
   '<div class="k">2027 começou</div><h1>Orçamento novo, <mark>compra planejada</mark></h1><div class="linha"></div>'
   '<p>Quem cota em janeiro compra com calma e recebe antes da correria do fim do ano.</p>'
   + chips("Informática", "Climatização", "Eletrodomésticos", "Ferramentas", "Áudio e vídeo", "Papelaria") + chamada()), "feed"),
 (O + "2027-01-06_post_eletro_refeitorio.jpg", tela(
   '<div class="k">Cozinhas institucionais e refeitórios</div><h1>Eletro para o <mark>dia a dia</mark> do órgão</h1><div class="linha"></div>'
   '<p>Do refeitório da escola à copa da secretaria, no mesmo fornecedor.</p>'
   + chips("Geladeiras", "Freezers", "Micro-ondas", "Liquidificadores", "Cafeteiras", "Purificadores", "Bebedouros") + chamada()), "feed"),
 (O + "2027-01-14_post_audio_video.jpg", tela(
   '<div class="k">Treinamentos, eventos e comunicação</div><h1>Áudio e vídeo para <mark>sala cheia</mark></h1><div class="linha"></div>'
   '<p>Equipamentos audiovisuais para auditórios, salas de treinamento e comunicação institucional.</p>'
   + chips("Smart TVs", "Projetores", "Câmeras", "Caixas de som", "Rádios comunicadores") + chamada()), "feed"),
 (O + "2027-01-21_post_ferramentas.jpg", tela(
   '<div class="k">Manutenção predial, obras e campo</div><h1>Ferramenta boa <mark>não para</mark> o serviço</h1><div class="linha"></div>'
   '<p>Para as equipes de manutenção do prédio, das obras e dos serviços de campo.</p>'
   + chips("Esmerilhadeiras", "Furadeiras", "Martelos demolidores", "Roçadeiras", "Máquinas de solda", "Bombas") + chamada()), "feed"),
 (O + "2027-01-28_post_climatizacao_split.jpg", tela(
   '<div class="k">Janeiro quente</div><h1>Sala climatizada, <mark>atendimento melhor</mark></h1><div class="linha"></div>'
   '<p>Split e portátil de diversas capacidades, da sala pequena ao atendimento ao público.</p>'
   + chips("Split", "Portátil", "9K a 24K+ BTUs") + chamada("Mande a metragem e o edital: a DPA indica e cota")), "feed"),
]
pecas += carrossel("2026-12-06_carrossel_dispensa_2026", [
 tela('<div class="k">Valores de 2026</div><h1>Dispensa de licitação: <mark>até quanto</mark> pode?</h1><div class="linha"></div><p>Os limites por valor do art. 75 da Lei 14.133/2021, em vigor desde 1º de janeiro de 2026.</p>', "1/5", arr=True),
 tela('<div class="k">Compras e outros serviços</div><div class="num" style="font-size:150px;line-height:1.05">R$ 65.492,11</div><div class="linha"></div><p>Limite para a dispensa por valor em <b>compras e demais serviços</b>.</p><p class="fonte">Lei 14.133/2021, art. 75, II · valor atualizado pelo Decreto nº 12.807/2025</p>', "2/5", arr=True),
 tela('<div class="k">Obras, engenharia e manutenção de veículos</div><div class="num" style="font-size:150px;line-height:1.05">R$ 130.984,20</div><div class="linha"></div><p>Limite para <b>obras, serviços de engenharia</b> e <b>manutenção de veículos automotores</b>.</p><p class="fonte">Lei 14.133/2021, art. 75, I · valor atualizado pelo Decreto nº 12.807/2025</p>', "3/5", arr=True),
 tela('<div class="k">Atenção em janeiro</div><h2>Os valores <b>mudam todo ano</b></h2><div class="linha"></div><p>A lei manda atualizar os valores em <b>1º de janeiro</b>, pelo IPCA-E. Antes da primeira dispensa de 2027, confira o decreto novo.</p><p class="fonte">Lei 14.133/2021, art. 182</p>', "4/5", arr=True),
 cta("Dispensa aberta? A DPA <b>cota rápido</b>", "Envie o item e a quantidade. Proposta no padrão do seu processo.", n="5/5"),
])
pecas += carrossel("2026-12-28_carrossel_plano_contratacoes_2027", [
 tela('<div class="k">Planejamento 2027</div><h1>O ano começa no <mark>plano de contratações</mark></h1><div class="linha"></div><p>O que é o PCA e por que ele faz as compras de 2027 andarem mais rápido.</p>', "1/5", arr=True),
 tela('<div class="k">O que diz a lei</div><h2>As compras do ano <b>em um só plano</b></h2><div class="linha"></div><p>Feito a partir dos documentos de formalização de demanda, o PCA serve para <b>racionalizar as contratações</b>, alinhar ao planejamento estratégico e subsidiar as leis orçamentárias.</p><p class="fonte">Lei 14.133/2021, art. 12, VII</p>', "2/5", arr=True),
 tela('<div class="k">Transparência</div><h2>O plano é <b>público</b></h2><div class="linha"></div><p>O plano de contratações anual deve ser divulgado e mantido à disposição do público em sítio eletrônico oficial.</p><p class="fonte">Lei 14.133/2021, art. 12, § 1º</p>', "3/5", arr=True),
 tela('<div class="k">Na prática</div><h2>3 dicas para o <b>1º trimestre</b></h2><div class="it"><i>1</i><span>Agrupe itens parecidos no mesmo processo.</span></div><div class="it"><i>2</i><span>Pesquise preços cedo: painel de preços e contratações similares (art. 23).</span></div><div class="it"><i>3</i><span>Veja as atas de registro de preços vigentes.</span></div>', "4/5", arr=True),
 cta("Planejou? A DPA <b>cota com você</b>", "Mande a lista: informática, climatização, eletro, ferramentas e muito mais, no mesmo CNPJ.", n="5/5"),
])
pecas += carrossel("2027-01-13_carrossel_modalidades", [
 tela('<div class="k">Como a DPA atende</div><h1>Pregão, dispensa ou ata? <mark>Todas.</mark></h1><div class="linha"></div><p>As principais formas de compra pública, em uma tela cada.</p>', "1/5", arr=True),
 tela('<div class="k">Pregão eletrônico</div><h2>O caminho dos <b>bens e serviços comuns</b></h2><div class="linha"></div><p>Modalidade obrigatória para aquisição de bens e serviços comuns. Disputa por lances, com o menor preço ou maior desconto.</p><p class="fonte">Lei 14.133/2021, art. 6º, XLI</p>', "2/5", arr=True),
 tela('<div class="k">Dispensa de licitação</div><h2>Rápida, <b>com limite</b></h2><div class="linha"></div><p>Por valor, até <b>R$ 65.492,11</b> em compras e serviços comuns em 2026, valor atualizado todo 1º de janeiro.</p><p class="fonte">Lei 14.133/2021, arts. 75, II, e 182 · Decreto nº 12.807/2025</p>', "3/5", arr=True),
 tela('<div class="k">Ata de registro de preços</div><h2>Registra hoje, <b>compra quando precisar</b></h2><div class="linha"></div><p>A ata vale <b>1 ano</b>, prorrogável por igual período se o preço continuar vantajoso. E outros órgãos podem aderir (a "carona").</p><p class="fonte">Lei 14.133/2021, arts. 84 e 86</p>', "4/5", arr=True),
 cta("Qualquer modalidade, <b>mesma DPA</b>", "Documentação regular junto com cada proposta, desde 2015.", n="5/5"),
])
pecas += carrossel("2027-01-20_carrossel_adesao_ata_limites", [
 tela('<div class="k">Carona na ata</div><h1>Adesão à ata: <mark>até onde</mark> dá para ir?</h1><div class="linha"></div><p>Os dois limites que todo órgão não participante precisa conferir antes de aderir.</p>', "1/5", arr=True),
 tela('<div class="k">Limite por órgão</div><div class="num" style="font-size:240px">50%</div><div class="linha"></div><p>Cada órgão que adere pode contratar até <b>metade dos quantitativos</b> de cada item registrado na ata.</p><p class="fonte">Lei 14.133/2021, art. 86, § 4º · Decreto nº 11.462/2023, art. 32, I</p>', "2/5", arr=True),
 tela('<div class="k">Limite de todas as adesões</div><div class="num" style="font-size:240px">2x</div><div class="linha"></div><p>Somadas, as adesões não podem passar do <b>dobro do quantitativo</b> de cada item registrado.</p><p class="fonte">Lei 14.133/2021, art. 86, § 5º · Decreto nº 11.462/2023, art. 32, II</p>', "3/5", arr=True),
 tela('<div class="k">Atenção, órgão federal</div><h2>Ata de Estado ou Município <b>não serve</b></h2><div class="linha"></div><p>Órgãos e entidades da Administração Pública federal não podem aderir a ata gerenciada por órgão estadual, distrital ou municipal.</p><p class="fonte">Lei 14.133/2021, art. 86, § 8º</p>', "4/5", arr=True),
 cta("Itens fora da ata? <b>A DPA cota</b>", "Envie o que falta no seu processo. Proposta no padrão do seu órgão.", n="5/5"),
])
pecas += carrossel("2027-01-27_carrossel_documentacao_em_dia", [
 tela('<div class="k">Habilitação sem susto</div><h1>Documentação <mark>em dia</mark>, junto com a proposta</h1><div class="linha"></div><p>O que a DPA mantém regular e envia com cada proposta, sem você precisar pedir.</p>', "1/4", arr=True),
 tela('<div class="k">Certidões</div><h2>Regularidade <b>fiscal e trabalhista</b></h2><div class="it"><i>✓</i><span>Certidão Negativa Federal</span></div><div class="it"><i>✓</i><span>Certidão Negativa Estadual (MG)</span></div><div class="it"><i>✓</i><span>Certidão Negativa Municipal</span></div><div class="it"><i>✓</i><span>FGTS</span></div><div class="it"><i>✓</i><span>Certidão Trabalhista (CNDT)</span></div>', "2/4", arr=True),
 tela('<div class="k">Cadastro</div><h2>Dados da empresa <b>sempre atualizados</b></h2><div class="it"><i>✓</i><span>Cartão CNPJ</span></div><div class="it"><i>✓</i><span>Contrato social consolidado</span></div><div class="it"><i>✓</i><span>Inscrição Estadual</span></div><p style="margin-top:44px">CNPJ 21.641.059/0001-39 · Ibirité/MG · desde 2015</p>', "3/4", arr=True),
 cta("Fornecedor <b>regular</b> é fornecedor que entrega", "Envie o edital. A proposta vai com a documentação.", n="4/4"),
])
pecas += [
 st("2026-12-26_story_entre_natal_e_ano_novo", "Entre o Natal e o Ano Novo", "O setor de compras está…", "( ) descansando<br>( ) fechando o exercício<br><b>(x) os dois ao mesmo tempo</b>", "Responda aqui 😄"),
 st("2026-12-27_story_2026_em_uma_palavra", "Retrospectiva", "2026 em <mark>uma palavra</mark>", "Como foi o ano no seu setor de compras? Mande a sua palavra por mensagem.", "Responder"),
 st("2027-01-09_story_obrigado_12_anos", "8 de janeiro de 2015 → 2027", "<mark>12 anos.</mark> Obrigado!", "A cada órgão, pregoeiro, fiscal e parceiro que fez parte da nossa história.", "", '<img src="logo-12anos.webp" style="width:560px;display:block;margin:0 auto 70px">'),
 st("2027-01-15_story_edital_whatsapp", "Edital aberto?", "Mande e <mark>receba a proposta</mark>", "Link do edital, item ou termo de referência.<br><b>WhatsApp (31) 9 9718-6304</b>", "Diga: vim pelo Instagram"),
 st("2027-01-22_story_ata_vigencia", "Você sabia?", "A ata vale <mark>1 ano</mark>", "E pode ser prorrogada por igual período, se o preço continuar vantajoso.<br><span style=\"font-size:30px;color:#8a8e99\">Lei 14.133/2021, art. 84</span>", "Siga para mais dicas"),
 st("2027-01-29_story_volta_as_aulas", "Fevereiro chegando", "Escola pronta para a <mark>volta às aulas</mark>?", "Notebooks, projetores, Smart TVs, climatização e eletro para a cozinha, no mesmo CNPJ.", "Envie seu edital"),
]
render(pecas)
print(len(pecas), "peças")
