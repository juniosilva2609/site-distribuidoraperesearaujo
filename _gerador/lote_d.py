# -*- coding: utf-8 -*-
"""Reel especial: reforma tributária nas compras públicas (13/11/2026). Fatos: EC 132/2023 (ADCT 125-129), LC 214/2025 arts. 472 e 473."""
from dpa import *
CSS = """
.grade{position:absolute;inset:-10%;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:90px 90px;animation:grade 24s linear 0s both paused}
@keyframes grade{from{transform:translate(0,0)}to{transform:translate(-90px,-180px)}}
.luz{position:absolute;top:-20%;left:-60%;width:50%;height:140%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.07),transparent);transform:skewX(-18deg);animation:luz 6s ease-in-out 0s infinite paused}
@keyframes luz{from{left:-60%}to{left:130%}}
.chips{display:flex;flex-wrap:wrap;gap:22px;margin-top:34px}
.chip{font-family:Anton;font-size:96px;line-height:1;padding:22px 38px 26px;border-radius:22px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.16);color:#fff}
.sai{animation:sai 1s cubic-bezier(.5,0,.8,.4) calc(var(--s) + var(--d,0s)) both paused}
@keyframes sai{0%{opacity:1;transform:none}35%{opacity:1;transform:rotate(-4deg) scale(1.04);color:#d7141a;text-decoration:line-through}100%{opacity:.16;transform:translateY(46px) rotate(5deg) scale(.9);color:#8a8e99;text-decoration:line-through}}
.entra{background:#d7141a;border-color:#d7141a;box-shadow:0 0 70px rgba(215,20,26,.65);animation:zoom .7s cubic-bezier(.2,1.5,.3,1) calc(var(--s) + var(--d,0s)) both paused}
.entra small{display:block;font-family:Montserrat;font-weight:600;font-size:28px;margin-top:10px;letter-spacing:.02em}
.tl{position:relative;margin-top:44px;padding-left:96px}
.tl .fio{position:absolute;left:30px;top:10px;bottom:10px;width:8px;border-radius:4px;background:linear-gradient(#d7141a,#ff6a6f);transform-origin:top;animation:cresce 4.6s linear calc(var(--s) + .4s) both paused}
@keyframes cresce{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.no{position:relative;margin-bottom:54px;animation:sobe .6s cubic-bezier(.2,.8,.2,1) calc(var(--s) + var(--d,0s)) both paused}
.no::before{content:"";position:absolute;left:-88px;top:14px;width:52px;height:52px;border-radius:50%;background:#111216;border:8px solid #d7141a;box-shadow:0 0 34px rgba(215,20,26,.8)}
.no b{font-family:Anton;font-size:104px;line-height:1;color:#fff;font-weight:400;display:block}
.no span{font-size:40px;line-height:1.25;color:#c4c7cf;font-weight:500;display:block;margin-top:8px}
.no em{font-style:normal;color:#ff5a60;font-weight:700}
.cartao{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-left:12px solid #d7141a;border-radius:26px;padding:40px 44px;margin-top:34px}
.cartao h3{font-size:58px;font-weight:800;line-height:1.12}.cartao p{font-size:36px;margin-top:14px}
.cartao small{display:block;font-size:28px;color:#8a8e99;margin-top:14px;font-weight:600}
.r .fonte{font-size:30px}
"""
cenas = [
 (3.2, '<div class="k an">Reforma tributária</div><h1 class="an" style="--d:.2s;font-size:124px">O jeito de <mark>tributar</mark> a compra pública vai <b>mudar</b></h1><p class="an" style="--d:.9s;margin-top:40px">Entenda em 25 segundos.</p>'),
 (4.8, '<div class="k an">Saem</div><div class="chips"><span class="chip sai" style="--d:.9s">PIS</span><span class="chip sai" style="--d:1.1s">COFINS</span><span class="chip sai" style="--d:1.3s">ICMS</span><span class="chip sai" style="--d:1.5s">ISS</span></div>'
       '<div class="k an" style="--d:2.2s;margin-top:80px">Entram</div><div class="chips"><span class="chip entra" style="--d:2.5s">CBS<small>federal</small></span><span class="chip entra" style="--d:2.8s">IBS<small>Estados e Municípios</small></span></div>'
       '<p class="fonte an" style="--d:3.2s;margin-top:40px">Emenda Constitucional nº 132/2023</p>'),
 (6.4, '<div class="k an">A linha do tempo</div><div class="tl"><div class="fio"></div>'
       '<div class="no" style="--d:.5s"><b>2026</b><span>Ano de teste: <em>0,9%</em> de CBS e <em>0,1%</em> de IBS</span></div>'
       '<div class="no" style="--d:1.7s"><b>2027</b><span>A <em>CBS</em> entra em vigor. PIS e Cofins são extintos</span></div>'
       '<div class="no" style="--d:2.9s"><b>2029–2032</b><span>ICMS e ISS caem <em>10% ao ano</em></span></div>'
       '<div class="no" style="--d:4.1s;margin-bottom:0"><b>2033</b><span>ICMS e ISS são <em>extintos</em></span></div></div>'
       '<p class="fonte an" style="--d:4.8s;margin-top:40px">EC nº 132/2023, ADCT arts. 125 a 129</p>'),
 (5.6, '<div class="k an">E na compra pública?</div><h2 class="an" style="--d:.2s;font-size:92px">Tem <mark>regra própria</mark></h2>'
       '<div class="cartao esq" style="--d:.9s"><h3>Alíquota reduzida</h3><p>IBS e CBS com redutor nas aquisições de órgãos públicos, a partir de 2027.</p><small>LC nº 214/2025, art. 472</small></div>'
       '<div class="cartao esq" style="--d:2.2s"><h3>O imposto fica com quem compra</h3><p>Arrecadação destinada integralmente ao ente contratante.</p><small>LC nº 214/2025, art. 473</small></div>'),
 (4.4, '<img class="zoom" src="logo-full.png" style="width:820px;display:block;margin:0 auto 70px"><h1 class="an" style="--d:.5s;font-size:96px;text-align:center">Siga a <mark>série</mark> no perfil</h1><p class="an" style="--d:1s;margin-top:40px;text-align:center">Cada regra explicada, com a fonte.<br>Salve e envie ao setor de compras.</p>'),
]
# fundo com grade e luz
import dpa
_orig = dpa.reel
def reel_rico(out, cenas, audio, inicio):
    import json, subprocess, os
    t, html = 0, '<div class="fundo"></div><div class="grade"></div><div class="brilho"></div><img class="gl" src="mark.png"><div class="luz"></div><div class="prog"></div>'
    html += '<div class="marca"><img src="mark.png">PERES &amp; ARAÚJO</div>'
    for i, (d, c) in enumerate(cenas):
        html += dpa.cena(t, d, c, ult=i == len(cenas) - 1); t += d
    html += f'<div class="arroba">{dpa.ARROBA}</div>'
    json.dump({"out": out, "dur": round(t, 2), "html": html, "css": CSS, "audio": audio, "inicio": inicio}, open(os.path.join(dpa.AQUI, "reel.json"), "w"))
    subprocess.run(["node", os.path.join(dpa.AQUI, "reel.js"), os.path.join(dpa.AQUI, "reel.json")], check=True, cwd=dpa.AQUI)
reel_rico("out/d/2026-11-13_reel_reforma_tributaria_compras_publicas.mp4", cenas, "musica/Newer_Wave.mp3", 52)
