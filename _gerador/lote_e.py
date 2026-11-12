from dpa import *
GATO = '''<svg class="gato" viewBox="0 0 200 260"><g fill="#060607">
<path d="M58 40 L62 2 L88 30 Z"/><path d="M142 40 L138 2 L112 30 Z"/>
<circle cx="100" cy="62" r="44"/>
<path d="M60 100 C30 150 32 230 60 252 L140 252 C168 230 170 150 140 100 Z"/>
<path d="M140 240 C190 236 196 196 172 176 C190 204 176 226 140 226 Z"/></g>
<g class="olhos" fill="#ffcf3a"><ellipse cx="82" cy="60" rx="8" ry="11"/><ellipse cx="118" cy="60" rx="8" ry="11"/></g></svg>'''
CSS = """
.lua{position:absolute;left:50%;top:50%;width:760px;height:760px;margin:-560px 0 0 -380px;border-radius:50%;
 background:radial-gradient(circle at 40% 38%,#ff4a4f,#d7141a 55%,#8e0b10);box-shadow:0 0 160px 40px rgba(215,20,26,.45);
 animation:zoom 1s cubic-bezier(.2,1,.3,1) calc(var(--s)) both paused}
.treze{position:relative;font-family:Anton;font-size:520px;line-height:.9;color:#fff;text-align:center;letter-spacing:-.02em;
 text-shadow:0 20px 60px rgba(0,0,0,.5);animation:pisca 3.2s steps(1) calc(var(--s) + .6s) both paused}
@keyframes pisca{0%{opacity:1}8%{opacity:.25}10%{opacity:1}12%{opacity:.4}14%{opacity:1}100%{opacity:1}}
.gato{position:absolute;width:300px;left:50%;margin-left:150px;top:830px;animation:sobe .8s ease calc(var(--s) + .9s) both paused}
.olhos{transform-origin:100px 60px;animation:pisc 3.2s linear calc(var(--s) + 1.6s) both paused}
@keyframes pisc{0%,40%,48%,100%{transform:scaleY(1)}44%{transform:scaleY(.08)}}
.lista .it{font-size:54px;font-weight:700;color:#fff;margin-top:44px}.lista .it i{width:76px;height:76px;font-size:40px}
.fim h2{font-size:92px;text-align:center}.fim p{text-align:center}
"""
reel("out/2026-11-13_reel_sexta_feira_13.mp4", [
 (3.4, '<div class="lua"></div><div class="k an c" style="text-align:center;font-size:44px;color:#fff;--d:.2s;position:relative">Sexta-feira</div>'
       '<div class="treze zoom" style="--d:.35s">13</div>' + GATO),
 (3.0, '<div class="k an">Calma, setor de compras</div><h2 class="an" style="--d:.25s">Quem compra para o governo não tem medo de <b>gato preto</b>.</h2>'),
 (5.6, '<div class="k an">Medo de verdade é</div><div class="lista">'
       '<div class="it esq" style="--d:.3s"><i>1</i>Pregão deserto</div>'
       '<div class="it esq" style="--d:1.2s"><i>2</i>Empenho vencendo sem entrega</div>'
       '<div class="it esq" style="--d:2.1s"><i>3</i>Fornecedor que some depois da homologação</div>'
       '<div class="it esq" style="--d:3.0s"><i>4</i>Dezembro chegando com saldo parado</div></div>'),
 (3.2, '<h1 class="an">Superstição,<br>a gente respeita.</h1><h1 class="an" style="--d:1.1s;margin-top:40px">Prazo,<br>a gente <mark>cumpre</mark>.</h1>'),
 (3.6, '<div class="fim c"><img class="logo zoom" src="logo-full.png" style="width:720px;margin-bottom:70px">'
       '<h2 class="an" style="--d:.3s">Fornecedor <b>sem susto</b>.</h2>'
       '<p class="an" style="--d:.8s;margin-top:44px">Qual é o seu maior medo?<br><b>Comenta o número</b> ↓</p></div>'),
], "musica/Sneaky_Snitch.mp3", inicio=0, css=CSS)
