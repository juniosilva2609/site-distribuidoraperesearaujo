# -*- coding: utf-8 -*-
"""Lote G (12/11/2026): 8 reels de vendas/atualidades para os dias vazios. Música: Kevin MacLeod (CC BY 4.0).
Dados da DPA: site oficial (fundação 08/01/2015, 5+ estados MG/RJ/BA/SE/PB, 40+ linhas, segmentos)."""
import json, subprocess, os, sys
import dpa
CSS = """
.grade{position:absolute;inset:-10%;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:90px 90px;animation:grade 24s linear 0s both paused}
@keyframes grade{from{transform:translate(0,0)}to{transform:translate(-90px,-180px)}}
.luz{position:absolute;top:-20%;left:-60%;width:50%;height:140%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.07),transparent);transform:skewX(-18deg);animation:luz 6s ease-in-out 0s infinite paused}
@keyframes luz{from{left:-60%}to{left:130%}}
.chips{display:flex;flex-wrap:wrap;gap:20px;margin-top:40px}
.chip{font-weight:800;font-size:46px;padding:20px 34px;border-radius:60px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);color:#fff;animation:zoom .55s cubic-bezier(.2,1.5,.3,1) calc(var(--s) + var(--d,0s)) both paused}
.chip.v{background:#d7141a;border-color:#d7141a;box-shadow:0 0 50px rgba(215,20,26,.55)}
.cartao{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-left:12px solid #d7141a;border-radius:26px;padding:38px 44px;margin-top:30px}
.cartao h3{font-size:56px;font-weight:800;line-height:1.12}.cartao p{font-size:38px;margin-top:12px}
.cartao.cinza{border-left-color:#5c606c;opacity:.9}
.chk{display:flex;gap:28px;align-items:center;margin-top:40px;font-size:50px;font-weight:700;line-height:1.2}
.chk i{flex:none;width:78px;height:78px;border-radius:20px;border:4px solid rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center;font-style:normal;font-size:50px;color:#fff;position:relative}
.chk i::after{content:"✓";position:absolute;inset:-4px;border-radius:20px;background:#d7141a;display:flex;align-items:center;justify-content:center;animation:zoom .4s cubic-bezier(.2,1.6,.3,1) calc(var(--s) + var(--d,0s) + .45s) both paused}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:44px}
.tile{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:30px;padding:40px 30px;text-align:center;animation:zoom .6s cubic-bezier(.2,1.4,.3,1) calc(var(--s) + var(--d,0s)) both paused}
.tile em{display:block;font-style:normal;font-size:120px;line-height:1.1}.tile b{display:block;font-size:40px;font-weight:800;margin-top:14px;color:#fff}
.tl{position:relative;margin-top:44px;padding-left:96px}
.tl .fio{position:absolute;left:30px;top:10px;bottom:10px;width:8px;border-radius:4px;background:linear-gradient(#d7141a,#ff6a6f);transform-origin:top;animation:cresce 5s linear calc(var(--s) + .4s) both paused}
@keyframes cresce{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.no{position:relative;margin-bottom:50px;animation:sobe .6s cubic-bezier(.2,.8,.2,1) calc(var(--s) + var(--d,0s)) both paused}
.no::before{content:"";position:absolute;left:-88px;top:10px;width:52px;height:52px;border-radius:50%;background:#111216;border:8px solid #d7141a;box-shadow:0 0 34px rgba(215,20,26,.8)}
.no b{font-size:54px;font-weight:800;color:#fff;display:block;line-height:1.15}.no span{font-size:38px;color:#c4c7cf;display:block;margin-top:8px;line-height:1.3}
.big{font-family:Anton;font-size:360px;line-height:.95;color:#d7141a;text-shadow:0 0 80px rgba(215,20,26,.45)}
.sol{position:absolute;left:50%;top:330px;width:620px;height:620px;margin-left:-310px;border-radius:50%;background:radial-gradient(circle,#ffd166 0%,#ff8a3d 45%,rgba(215,20,26,0) 72%);animation:zoom 1.2s ease calc(var(--s)) both paused;opacity:.85}
.c{text-align:center}.c .chips{justify-content:center}
"""
def logo_cta(titulo, sub, botao="Envie seu edital no WhatsApp"):
    return (f'<div class="c"><img class="zoom" src="logo-full.png" style="width:800px;display:block;margin:0 auto 70px">'
            f'<h1 class="an" style="--d:.4s;font-size:92px">{titulo}</h1><p class="an" style="--d:.9s;margin-top:36px">{sub}</p>'
            f'<div class="an" style="--d:1.3s;margin-top:60px"><span class="btn" style="font-size:42px">{botao}</span></div></div>')
def reel(out, cenas, audio, inicio):
    t, html = 0, '<div class="fundo"></div><div class="grade"></div><div class="brilho"></div><img class="gl" src="mark.png"><div class="luz"></div><div class="prog"></div>'
    html += '<div class="marca"><img src="mark.png">PERES &amp; ARAÚJO</div>'
    for i, (d, c) in enumerate(cenas):
        html += dpa.cena(t, d, c, ult=i == len(cenas) - 1); t += d
    html += f'<div class="arroba">{dpa.ARROBA}</div>'
    json.dump({"out": out, "dur": round(t, 2), "html": html, "css": CSS, "audio": audio, "inicio": inicio}, open(os.path.join(dpa.AQUI, "reel.json"), "w"))
    subprocess.run(["node", os.path.join(dpa.AQUI, "reel.js"), os.path.join(dpa.AQUI, "reel.json")], check=True, cwd=dpa.AQUI)
O = "out/g/"; os.makedirs(os.path.join(dpa.AQUI, O), exist_ok=True)
def chips(itens, d0=.5, passo=.32, v=()):
    return '<div class="chips">' + "".join(f'<span class="chip{" v" if i in v else ""}" style="--d:{d0+k*passo:.2f}s">{i}</span>' for k, i in enumerate(itens)) + '</div>'
def chk(itens, d0=.5, passo=1.0):
    return "".join(f'<div class="chk esq" style="--d:{d0+k*passo:.2f}s"><i></i><span>{i}</span></div>' for k, i in enumerate(itens))
R = {
"2026-11-22_reel_catalogo_um_cnpj": ([
 (2.8, '<div class="k an">Setor de compras,</div><h1 class="an" style="--d:.25s">Quantos fornecedores <mark>você gerencia</mark> por processo?</h1>'),
 (5.4, '<h2 class="an" style="font-size:88px">Na DPA são <b>40+ linhas</b> no mesmo CNPJ</h2>' + chips(["Informática", "Climatização", "Eletrodomésticos", "Ferramentas", "Áudio e vídeo", "Papelaria", "Material elétrico", "Mobiliário"], .7, .38)),
 (3.6, '<div class="c"><div class="big zoom">1</div><h1 class="an" style="--d:.5s;font-size:96px">CNPJ. Uma proposta.<br><mark>Uma NF-e.</mark></h1></div>'),
 (3.4, '<div class="k an">Desde 2015</div><h2 class="an" style="--d:.2s;font-size:92px">Atendendo órgãos públicos em <b>5+ estados</b></h2>' + chips(["MG", "RJ", "BA", "SE", "PB"], .9, .25, v=("MG",))),
 (3.6, logo_cta("Um fornecedor, <mark>vários itens</mark>", "Envie o edital inteiro. A gente cota tudo que atende.")),
], "musica/Voxel_Revolution.mp3", 39, "Voxel Revolution"),
"2026-12-13_reel_dezembro_expectativa_realidade": ([
 (2.8, '<div class="k an">Dezembro no setor de compras</div><h1 class="an" style="--d:.25s;font-size:150px">Expectativa <b>x</b> realidade</h1>'),
 (3.0, '<div class="k an">Expectativa</div><div class="cartao cinza esq" style="--d:.3s"><h3>Clima de fim de ano 🎄</h3><p>Tudo resolvido, mesa vazia, café quentinho.</p></div>'),
 (5.0, '<div class="k an">Realidade</div>' + chk(["Empenho para emitir", "Nota para atestar", "Entrega para conferir", "Prazo para cumprir"], .4, .95)),
 (3.2, '<h1 class="an" style="font-size:118px">A parte da <mark>entrega</mark>, deixa com a gente.</h1>'),
 (3.6, logo_cta("Dezembro <mark>sem susto</mark>", "Envie o item. Proposta no padrão do seu processo.")),
], "musica/Electrodoodle.mp3", 0, "Electrodoodle"),
"2026-12-20_reel_verao_climatizacao": ([
 (3.0, '<div class="sol"></div><div class="c" style="margin-top:520px"><div class="k an" style="--d:.4s">Amanhã, 21 de dezembro</div><h1 class="an" style="--d:.6s;font-size:150px">Começa o <mark>verão</mark></h1></div>'),
 (3.2, '<div class="c"><div class="zoom" style="font-size:300px;line-height:1">🌡️</div><h2 class="an" style="--d:.4s;font-size:88px;margin-top:30px">E a sala de atendimento, <b>está pronta</b>?</h2></div>'),
 (4.6, '<div class="k an">Climatização DPA</div><h2 class="an" style="--d:.2s;font-size:96px">Split e portátil</h2>' + chips(["9.000 BTUs", "12.000 BTUs", "18.000 BTUs", "24.000+ BTUs"], .7, .45, v=("24.000+ BTUs",))),
 (3.0, '<h1 class="an" style="font-size:112px">Para salas, postos de trabalho e <mark>atendimento ao público</mark>.</h1>'),
 (3.6, logo_cta("Clima bom, <mark>serviço melhor</mark>", "Envie o item do seu edital. A DPA cota.")),
], "musica/Funkorama.mp3", 28, "Funkorama"),
"2026-12-29_reel_metas_2027": ([
 (2.6, '<div class="k an">Metas 2027 do setor de compras</div><h1 class="an" style="--d:.25s;font-size:150px">Anota <mark>aí</mark> ✍️</h1>'),
 (5.6, chk(["Planejar o 1º trimestre", "Pesquisar preço cedo", "Comprar com calma, não em dezembro", "Menos fornecedores para gerenciar", "Fornecedor que entrega no prazo"], .3, .95)),
 (3.2, '<h1 class="an" style="font-size:124px">As duas últimas, a DPA <mark>resolve</mark>.</h1>'),
 (3.6, logo_cta("2027 começa com a <mark>cotação pronta</mark>", "Mande a lista. A gente monta a proposta.")),
], "musica/Rocket_Power.mp3", 5, "Rocket Power"),
"2027-01-05_reel_volta_as_aulas": ([
 (2.8, '<div class="k an">Fevereiro chega rápido</div><h1 class="an" style="--d:.25s">Escola pronta para a <mark>volta às aulas</mark>?</h1>'),
 (5.0, '<div class="tiles"><div class="tile" style="--d:.3s"><em>💻</em><b>Notebooks e computadores</b></div><div class="tile" style="--d:.8s"><em>📽️</em><b>Projetores e Smart TVs</b></div>'
       '<div class="tile" style="--d:1.3s"><em>❄️</em><b>Climatização</b></div><div class="tile" style="--d:1.8s"><em>🍽️</em><b>Eletro para a cozinha</b></div></div>'),
 (3.2, '<h1 class="an" style="font-size:116px">Tudo no <mark>mesmo CNPJ</mark>, com NF-e própria.</h1>'),
 (3.6, logo_cta("Sala de aula <mark>equipada</mark>", "Envie o edital ou a lista de itens.")),
], "musica/Pump.mp3", 17, "Pump"),
"2027-01-12_reel_12_anos_em_numeros": ([
 (3.2, '<div class="c"><img class="zoom" src="logo-12anos.webp" style="width:860px;display:block;margin:0 auto 50px"><h1 class="an" style="--d:.6s;font-size:120px">Obrigado!</h1></div>'),
 (2.8, '<div class="c"><div class="big zoom">2015</div><h2 class="an" style="--d:.4s;font-size:84px">8 de janeiro: <b>nasce a DPA</b></h2></div>'),
 (2.8, '<div class="c"><div class="big zoom">5+</div><h2 class="an" style="--d:.4s;font-size:84px">estados atendidos</h2>' + chips(["MG", "RJ", "BA", "SE", "PB"], .8, .2) + '</div>'),
 (2.8, '<div class="c"><div class="big zoom">40+</div><h2 class="an" style="--d:.4s;font-size:84px">linhas de produtos no <b>mesmo CNPJ</b></h2></div>'),
 (2.8, '<div class="c"><div class="big zoom">12</div><h2 class="an" style="--d:.4s;font-size:84px">anos fornecendo para o <b>setor público</b></h2></div>'),
 (3.6, '<div class="c"><h1 class="an" style="font-size:130px">Que venham os <mark>próximos 12</mark>.</h1><p class="an" style="--d:.7s;margin-top:44px">A cada órgão, pregoeiro, fiscal e parceiro: obrigado.</p></div>'),
], "musica/Neon_Laser_Horizon.mp3", 6, "Neon Laser Horizon"),
"2027-01-19_reel_do_edital_a_nota": ([
 (2.8, '<div class="k an">Como a DPA atende</div><h1 class="an" style="--d:.25s">Do edital à <mark>nota fiscal</mark>, sem surpresa</h1>'),
 (7.0, '<div class="tl"><div class="fio"></div>'
       '<div class="no" style="--d:.5s"><b>1. Você envia</b><span>Link do edital, item ou termo de referência</span></div>'
       '<div class="no" style="--d:1.9s"><b>2. A DPA propõe</b><span>Proposta no padrão do processo, com a documentação</span></div>'
       '<div class="no" style="--d:3.3s"><b>3. Empenho ou AF</b><span>Recebido o pedido, a entrega é programada</span></div>'
       '<div class="no" style="--d:4.7s;margin-bottom:0"><b>4. Entrega + NF-e</b><span>Nota fiscal eletrônica própria, emitida na venda</span></div></div>'),
 (3.0, '<h1 class="an" style="font-size:118px">Pregão, dispensa ou ata: <mark>mesma rotina</mark>.</h1>'),
 (3.6, logo_cta("Desde <mark>2015</mark>", "Comece pelo passo 1: mande o edital.")),
], "musica/Werq.mp3", 130, "Werq"),
"2027-01-26_reel_pedido_perfeito": ([
 (2.8, '<div class="k an">Dica de quem cota todo dia</div><h1 class="an" style="--d:.25s">Quer proposta <mark>rápida</mark>? Mande isto:</h1>'),
 (6.0, chk(["Link do edital ou nº do processo", "Item e especificação", "Quantidade", "Local de entrega", "Prazo exigido"], .3, 1.0)),
 (3.0, '<h1 class="an" style="font-size:118px">Com isso, a proposta sai <mark>no padrão</mark> do seu processo.</h1>'),
 (3.6, logo_cta("Mande <mark>agora</mark>", "WhatsApp (31) 9 9718-6304", "Diga: vim pelo Instagram")),
], "musica/Blippy_Trance.mp3", 87, "Blippy Trance"),
}
so = sys.argv[1:] or list(R)
for nome in so:
    cenas, audio, ini, _ = R[nome]
    reel(O + nome + ".mp4", cenas, audio, ini)
json.dump({k: v[3] for k, v in R.items()}, open(os.path.join(dpa.AQUI, O, "musicas.json"), "w"), ensure_ascii=False)
