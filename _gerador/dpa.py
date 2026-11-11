# -*- coding: utf-8 -*-
"""Peças do Instagram da DPA em HTML -> JPEG/MP4 (render.js / reel.js)."""
import json, subprocess, os
AQUI = os.path.dirname(os.path.abspath(__file__))
ARROBA = "@distribuidoraperesearaujo"

def topo(n=""):
    return f'<div class="topo"><img src="mark.png">PERES &amp; ARAÚJO<span class="n">{n}</span></div>'

def pe(arr=False):
    return f'<div class="pe"><span class="pill">{ARROBA}</span>{"<span class=arr>arraste →</span>" if arr else ""}</div>'

def tela(meio, n="", arr=False, claro=False, extra="", cls=""):
    return (f'<div class="t {"claro" if claro else ""} {cls}"><img class="globo" src="mark.png">{topo(n)}'
            f'<div class="meio">{meio}</div>{extra}{pe(arr)}</div>')

def cta(titulo, corpo, botao="Envie seu edital no WhatsApp", n=""):
    return (f'<div class="t"><img class="globo" src="mark.png"><div class="topo"><span class="n">{n}</span></div>'
            f'<div class="meio c"><img class="logo" src="logo-full.png" style="margin-bottom:60px">'
            f'<h2 style="text-align:center">{titulo}</h2><p style="text-align:center;margin:34px 0 56px">{corpo}</p>'
            f'<span class="btn">{botao}</span></div>'
            f'<p style="text-align:center;font-size:30px;font-weight:600;color:#fff;position:relative;z-index:2">WhatsApp na bio • distribuidoraperesearaujo.com.br</p></div>')

def story(meio, cls=""):
    return (f'<div class="t st {cls}" style="padding:150px 90px 250px"><img class="globo" src="mark.png">{topo()}'
            f'<div class="meio">{meio}</div><p style="text-align:center;font-size:34px;font-weight:600;color:#c4c7cf;position:relative;z-index:2">{ARROBA}</p></div>')

CSS_STORY = ".st h1{font-size:112px}.st p{font-size:48px}.st .k{font-size:34px}"

def render(pecas):
    """pecas: [(arquivo, html, 'feed'|'story')]"""
    spec = [{"out": a, "w": 1080, "h": 1350 if t == "feed" else 1920, "html": h, "css": CSS_STORY} for a, h, t in pecas]
    json.dump(spec, open(os.path.join(AQUI, "spec.json"), "w"))
    subprocess.run(["node", os.path.join(AQUI, "render.js"), os.path.join(AQUI, "spec.json")], check=True, cwd=AQUI)

def cena(inicio, dur, conteudo, ult=False):
    return f'<div class="cena {"ult" if ult else ""}" style="--s:{inicio}s;--dur:{dur}s"><div class="r">{conteudo}</div></div>'

def reel(out, cenas, audio, inicio=0, css=""):
    """cenas: [(duracao, html)] -- html usa classes an/zoom/esq/barra com style="--d:.3s"."""
    t, html = 0, '<div class="fundo"></div><div class="brilho"></div><img class="gl" src="mark.png"><div class="prog"></div>'
    html += '<div class="marca"><img src="mark.png">PERES &amp; ARAÚJO</div>'
    for i, (d, c) in enumerate(cenas):
        html += cena(t, d, c, ult=i == len(cenas) - 1)
        t += d
    html += f'<div class="arroba">{ARROBA}</div>'
    json.dump({"out": out, "dur": t, "html": html, "css": css, "audio": audio, "inicio": inicio},
              open(os.path.join(AQUI, "reel.json"), "w"))
    subprocess.run(["node", os.path.join(AQUI, "reel.js"), os.path.join(AQUI, "reel.json")], check=True, cwd=AQUI)
