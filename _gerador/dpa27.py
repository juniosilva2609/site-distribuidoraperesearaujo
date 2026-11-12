# -*- coding: utf-8 -*-
"""Modelos de 2027 (feed, carrossel, story e reel) sobre o dpa.py. Identidade: grafite + vermelho, Montserrat/Anton."""
import json, subprocess, os
import dpa
from dpa import tela, cta, story, render, ARROBA

CSS = open(os.path.join(dpa.AQUI, "dpa27.css")).read()

def chips_html(itens, anim=False, d0=.5, passo=.32, v=()):
    if anim:
        return '<div class="chips">' + "".join(f'<span class="chip{" v" if i in v else ""}" style="--d:{d0+k*passo:.2f}s">{i}</span>' for k, i in enumerate(itens)) + '</div>'
    return '<div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:34px">' + "".join(
        f'<span style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:40px;padding:14px 26px;font-size:30px;font-weight:700">{i}</span>' for i in itens) + '</div>'

def chk(itens, d0=.5, passo=1.0):
    return "".join(f'<div class="chk esq" style="--d:{d0+k*passo:.2f}s"><i></i><span>{i}</span></div>' for k, i in enumerate(itens))

def logo_cta(titulo, sub, botao="Envie seu edital no WhatsApp"):
    return (f'<div class="c"><img class="zoom" src="logo-full.png" style="width:800px;display:block;margin:0 auto 70px">'
            f'<h1 class="an" style="--d:.4s;font-size:92px">{titulo}</h1><p class="an" style="--d:.9s;margin-top:36px">{sub}</p>'
            f'<div class="an" style="--d:1.3s;margin-top:60px"><span class="btn" style="font-size:42px">{botao}</span></div></div>')

def reel(out, cenas, audio, inicio):
    t, html = 0, '<div class="fundo"></div><div class="grade"></div><div class="brilho"></div><img class="gl" src="mark.png"><div class="luz"></div><div class="prog"></div>'
    html += '<div class="marca"><img src="mark.png">PERES &amp; ARAÚJO</div>'
    for i, (d, c) in enumerate(cenas):
        html += dpa.cena(t, d, c, ult=i == len(cenas) - 1); t += d
    html += f'<div class="arroba">{ARROBA}</div>'
    spec = os.path.join(dpa.AQUI, f"reel_{os.getpid()}.json")
    json.dump({"out": out, "dur": round(t, 2), "html": html, "css": CSS, "audio": audio, "inicio": inicio, "crf": 17}, open(spec, "w"))
    subprocess.run(["node", os.path.join(dpa.AQUI, "reel27.js"), spec], check=True, cwd=dpa.AQUI)
    os.remove(spec)

# ---------- peças estáticas
def f_dica(k, titulo, corpo, fonte="", n="", arr=False):
    return tela(f'<div class="k">{k}</div><h2>{titulo}</h2><div class="linha"></div><p>{corpo}</p>' + (f'<p class="fonte">{fonte}</p>' if fonte else ""), n, arr=arr)

def f_capa(k, titulo, sub, n, total):
    return tela(f'<div class="k">{k}</div><h1>{titulo}</h1><div class="linha"></div><p>{sub}</p>', f"{n}/{total}", arr=True)

def f_lista(k, titulo, itens, n="", arr=False, simb=None):
    its = "".join(f'<div class="it"><i>{(simb or str(i))}</i><span>{t}</span></div>' for i, t in enumerate(itens, 1))
    return tela(f'<div class="k">{k}</div><h2>{titulo}</h2>{its}', n, arr=arr)

def f_produto(k, titulo, corpo, itens, chamada="Envie o item do seu edital pelo WhatsApp da bio"):
    return tela(f'<div class="k">{k}</div><h1>{titulo}</h1><div class="linha"></div><p>{corpo}</p>{chips_html(itens)}'
                f'<p style="margin-top:44px;font-size:32px;font-weight:700;color:#fff">→ {chamada}</p>')

def f_kit(k, titulo, itens, sub):
    cards = "".join(f'<div class="kit"><em>{e}</em><b>{t}</b></div>' for e, t in itens)
    st = ('<style>.kits{display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;margin-top:34px}'
          '.kit{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:24px 12px;text-align:center}'
          '.kit em{display:block;font-style:normal;font-size:70px;line-height:1.1}.kit b{display:block;font-size:26px;font-weight:700;margin-top:10px;color:#fff}</style>')
    return tela(f'{st}<div class="k">{k}</div><h2 style="font-size:66px">{titulo}</h2><div class="kits">{cards}</div><p style="margin-top:30px;font-size:32px;font-weight:700;color:#fff">{sub}</p>')

def f_numero(k, num, titulo, corpo):
    return tela(f'<div class="k">{k}</div><div class="num" style="font-size:260px">{num}</div><h2 style="margin-top:20px">{titulo}</h2><div class="linha"></div><p>{corpo}</p>')

def s_story(k, titulo, corpo, botao="", topo_img=""):
    b = f'<div style="text-align:center;margin-top:70px"><span class="btn">{botao}</span></div>' if botao else ""
    return story(f'{topo_img}<div class="k" style="text-align:center">{k}</div><h1 style="text-align:center;font-size:100px">{titulo}</h1><p style="text-align:center;margin-top:46px">{corpo}</p>{b}')
