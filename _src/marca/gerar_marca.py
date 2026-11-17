#!/usr/bin/env python3
"""Gera o kit de imagens da marca DPA (Perfil da Empresa no Google e capas de destaques do Instagram).

Saída em assets/img/marca/. Requer Playwright + Chrome (só para gerar; o site não depende disto).
Uso: python3 _src/marca/gerar_marca.py
"""
import pathlib
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[2]
OUT = RAIZ / "assets/img/marca"
F = (RAIZ / "assets/fonts").as_uri()
IMG = (RAIZ / "assets/img").as_uri()

ICON = {
 "laptop": '<rect x="3.5" y="4.5" width="17" height="11.5" rx="1.6"/><path d="M1.5 19.5h21"/><path d="M10 19.5l.6-1.4h2.8l.6 1.4"/>',
 "snow": '<path d="M12 2v20M3.3 7l17.4 10M3.3 17L20.7 7"/><path d="M9.5 3.8L12 6l2.5-2.2M9.5 20.2L12 18l2.5 2.2M3.6 10.4l3.2-1.1-.6-3.3M20.4 13.6l-3.2 1.1.6 3.3M3.6 13.6l3.2 1.1-.6 3.3M20.4 10.4l-3.2-1.1.6-3.3"/>',
 "fridge": '<rect x="5.5" y="2" width="13" height="20" rx="2"/><path d="M5.5 10h13M8.5 5.2v2.3M8.5 12.8v3.6"/>',
 "tool": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.4-3.4a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
 "tv": '<rect x="2" y="7" width="20" height="13.5" rx="2"/><path d="M16.5 2.5L12 7 7.5 2.5"/>',
 "landmark": '<path d="M3 21.5h18M5 18.5h14M6 18.5v-7M10 18.5v-7M14 18.5v-7M18 18.5v-7M12 2.5l8.5 5.5h-17z"/>',
 "chat": '<path d="M20.5 14.5a2 2 0 0 1-2 2H8l-4.5 4V5a2 2 0 0 1 2-2h13a2 2 0 0 1 2 2z"/><path d="M8 8.5h8M8 12h5"/>',
 "news": '<rect x="3" y="3.5" width="18" height="17" rx="2"/><path d="M7 8h10M7 12h4.5M7 16h4.5M14 12h3v4h-3z"/>',
 "grid": '<rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/>',
 "check": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M8.5 14l2.5 2.5 4.5-5"/>',
}

def ic(nome, tam, cor="#fff", sw=1.4):
    return ('<svg viewBox="0 0 24 24" width="%d" height="%d" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (tam, tam, cor, sw, ICON[nome]))

GLOBO = ('<svg class="globo" viewBox="0 0 200 200"><g fill="none" stroke="#fff" stroke-width=".35">'
         '<circle cx="100" cy="100" r="98"/><ellipse cx="100" cy="100" rx="98" ry="40"/><ellipse cx="100" cy="100" rx="98" ry="72"/>'
         '<ellipse cx="100" cy="100" rx="40" ry="98"/><ellipse cx="100" cy="100" rx="72" ry="98"/>'
         '<line x1="2" y1="100" x2="198" y2="100"/><line x1="100" y1="2" x2="100" y2="198"/></g></svg>')

BASE_CSS = """
@font-face{font-family:Anton;src:url(%(F)s/anton-latin.woff2) format('woff2')}
@font-face{font-family:Montserrat;src:url(%(F)s/montserrat-latin.woff2) format('woff2');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{font-family:Montserrat,sans-serif;color:#F4F5F7;background:#0B0C0E;position:relative;-webkit-font-smoothing:antialiased}
.fundo{position:absolute;inset:0;background:
  radial-gradient(60%% 70%% at 78%% 30%%,rgba(215,20,26,.38),rgba(142,11,16,.12) 45%%,transparent 70%%),
  radial-gradient(50%% 60%% at 10%% 100%%,rgba(142,11,16,.22),transparent 70%%),
  linear-gradient(160deg,#121318,#0B0C0E 55%%,#08090B)}
.grao{position:absolute;inset:0;opacity:0;background-image:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 4px)}
.globo{position:absolute;opacity:.10}
.faixas{position:absolute;top:0;right:0;width:%(FX)dpx;height:%(FX)dpx;background:linear-gradient(225deg,transparent 0 24%%,#D7141A 24%% 29.5%%,transparent 29.5%% 33.5%%,#2A2D34 33.5%% 39%%,transparent 39%%)}
.eyebrow{font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#FF5A5F}
.disp{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:1.02;letter-spacing:.01em}
.linha{display:block;width:90px;height:6px;background:#D7141A;border-radius:3px}
.muted{color:#A3A8B3}
.rod{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:space-between;border-top:1px solid rgba(255,255,255,.10);background:rgba(0,0,0,.25)}
"""

def pagina(w, h, corpo, extra="", fx=None):
    fx = fx or int(min(w, h) * .32)
    css = BASE_CSS % dict(F=F, W=w, H=h, FX=fx, FW=max(10, fx // 16), FT1=int(fx * .28), FT2=int(fx * .40))
    return '<!DOCTYPE html><html><head><meta charset="utf-8"><style>%s%s</style></head><body><div class="fundo"></div><div class="grao"></div>%s</body></html>' % (css, extra, corpo)

FAIXAS = '<div class="faixas"></div>'

# ---------- Google: capa 16:9 ----------
def capa():
    W, H = 2048, 1152
    segs = [("laptop", "Informática"), ("snow", "Climatização"), ("fridge", "Eletrodomésticos"),
            ("tool", "Ferramentas"), ("tv", "Eletroeletrônicos")]
    chips = "".join('<div class="chip">%s<span>%s</span></div>' % (ic(i, 36, "#FF5A5F", 1.6), t) for i, t in segs)
    extra = """
    .globo{width:1500px;height:1500px;right:-380px;top:-180px}
    .wrap{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 160px}
    .logo{width:1000px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.6))}
    .eyebrow{font-size:30px;margin:34px 0 0}
    .chips{display:flex;gap:16px;margin-top:50px;flex-wrap:nowrap}
    .chip{display:flex;align-items:center;gap:12px;padding:16px 24px;border:1.5px solid rgba(255,255,255,.14);border-radius:999px;background:rgba(255,255,255,.04);font-size:25px;font-weight:600;color:#E8E9EC;white-space:nowrap}
    .base{margin-top:42px;font-size:25px;color:#A3A8B3;letter-spacing:.02em}
    .base b{color:#fff;font-weight:600}
    """
    corpo = GLOBO + FAIXAS + """<div class="wrap">
      <img class="logo" src="%s/logo-full.png">
      <div class="eyebrow">Fornecedora do setor público desde 2015</div>
      <div class="chips">%s</div>
      <div class="base">Prefeituras · Polícias · Autarquias · Universidades &nbsp;—&nbsp; <b>Minas Gerais e outros estados</b></div>
    </div>""" % (IMG, chips)
    return "google/capa.jpg", W, H, pagina(W, H, corpo, extra, fx=420)

# ---------- Google: logotipo 1:1 ----------
def logotipo():
    W = H = 1080
    extra = """
    .fundo{background:radial-gradient(55% 55% at 50% 52%,rgba(215,20,26,.30),rgba(142,11,16,.10) 55%,transparent 75%),linear-gradient(160deg,#16171C,#0B0C0E)}
    .globo{width:1000px;height:1000px;left:40px;top:40px;opacity:.07}
    .m{position:absolute;left:50%;top:50%;width:700px;transform:translate(-50%,-50%);filter:drop-shadow(0 30px 40px rgba(0,0,0,.65))}
    """
    corpo = GLOBO + '<img class="m" src="%s/mark.png">' % IMG
    return "google/logotipo.png", W, H, pagina(W, H, corpo, extra)

# ---------- Google: fotos 4:3 ----------
SEGMENTOS = [
    ("seg-informatica", "laptop", "Informática<br>&amp; Tecnologia",
     "Notebooks, computadores, monitores, impressoras, HDs, componentes e suprimentos."),
    ("seg-eletrodomesticos", "fridge", "Eletrodomésticos<br>&amp; Refrigeração",
     "Geladeiras, freezers, micro-ondas, cafeteiras, purificadores e bebedouros."),
    ("seg-climatizacao", "snow", "Climatização",
     "Ar-condicionado split e portátil de diversas capacidades, de 9 mil a 24 mil BTUs ou mais."),
    ("seg-ferramentas", "tool", "Ferramentas<br>&amp; Equipamentos",
     "Esmerilhadeiras, furadeiras, martelos demolidores, roçadeiras, máquinas de solda e bombas."),
    ("seg-audio-video", "tv", "Áudio, Vídeo<br>&amp; Eletrônicos",
     "Smart TVs, projetores, câmeras, caixas de som e rádios comunicadores."),
]

FOTO_CSS = """
.globo{width:1300px;height:1300px;right:-420px;top:-200px}
.cab{position:absolute;left:84px;top:70px;height:74px}
.rod{height:96px;padding:0 84px;font-size:21px;white-space:nowrap;font-weight:600;color:#C9CCD3}
.rod b{color:#fff}
.rod .dot{width:7px;height:7px;border-radius:50%;background:#D7141A;display:inline-block;margin:0 14px 3px}
"""

def foto_segmento(slug, icone, titulo, texto, n):
    W, H = 1200, 1200
    extra = FOTO_CSS + """
    .ico{position:absolute;left:84px;top:230px;width:300px;height:300px;border-radius:50%;display:grid;place-items:center;
         background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.08),rgba(255,255,255,.02));border:1.5px solid rgba(255,90,95,.45);
         box-shadow:0 0 0 18px rgba(215,20,26,.06),0 40px 80px -30px rgba(0,0,0,.8)}
    .txt{position:absolute;left:84px;top:600px;width:1030px}
    .eyebrow{font-size:21px;margin-bottom:22px}
    h1{font-size:104px;margin-bottom:28px}
    p{font-size:30px;line-height:1.45;color:#B9BDC6;margin-top:28px;max-width:960px}
    """
    corpo = GLOBO + FAIXAS + """<img class="cab" src="%s/logo.png">
    <div class="ico">%s</div>
    <div class="txt"><div class="eyebrow">Linha de fornecimento · %02d</div><h1 class="disp">%s</h1><span class="linha"></span><p>%s</p></div>
    <div class="rod"><span>Fornecimento para <b>órgãos públicos</b> desde 2015</span><span>distribuidoraperesearaujo.com.br</span></div>""" % (
        IMG, ic(icone, 150, "#fff", 1.25), n, titulo, texto)
    return "google/foto-%s.jpg" % slug, W, H, pagina(W, H, corpo, extra, fx=300)

PASSOS = [("Edital e cotação", "Recebemos o edital, item ou TR"), ("Proposta", "Especificação, marca e valor"),
          ("Empenho / AF", "Prazo e garantia confirmados"), ("Entrega", "No endereço, dentro do prazo"),
          ("NF-e e suporte", "Acompanhamento até o recebimento")]

def foto_processo():
    W, H = 1200, 1200
    itens = "".join('<li><span class="n">%d</span><div><b>%s</b><small>%s</small></div></li>' % (i, t, s)
                    for i, (t, s) in enumerate(PASSOS, 1))
    extra = FOTO_CSS + """
    .txt{position:absolute;left:84px;top:200px;right:84px}
    .eyebrow{font-size:21px;margin-bottom:20px}
    h1{font-size:96px}
    ol{list-style:none;position:absolute;left:84px;right:84px;top:430px;display:grid;gap:44px}
    ol:before{content:"";position:absolute;left:39px;top:40px;bottom:40px;width:2px;background:linear-gradient(180deg,#D7141A,rgba(215,20,26,.25))}
    li{position:relative;display:flex;align-items:center;gap:30px}
    .n{display:grid;place-items:center;width:84px;height:84px;flex:0 0 84px;border-radius:50%;background:#15171B;border:2px solid #D7141A;font-family:Anton;font-size:38px;color:#fff;position:relative;z-index:1}
    li b{display:block;font-size:35px;margin:0 0 4px;color:#fff;line-height:1.2}
    li small{display:block;font-size:26px;color:#A3A8B3;line-height:1.4}
    """
    corpo = GLOBO + FAIXAS + """<img class="cab" src="%s/logo.png">
    <div class="txt"><div class="eyebrow">Como atendemos</div><h1 class="disp">Do edital à entrega</h1></div>
    <ol>%s</ol>
    <div class="rod"><span>Pregão · Dispensa · Registro de Preços · <b>Adesão a ARP</b></span><span>distribuidoraperesearaujo.com.br</span></div>""" % (IMG, itens)
    return "google/foto-como-atendemos.jpg", W, H, pagina(W, H, corpo, extra, fx=300)

ORGAOS = ["PMMG", "Polícia Civil MG", "DER-MG", "EPAMIG", "IEF-MG", "TCE-MG", "FHEMIG", "SEJUSP-MG",
          "Prefeituras", "Câmaras", "Universidades", "Autarquias"]

def foto_orgaos():
    W, H = 1200, 1200
    tags = "".join("<span>%s</span>" % o for o in ORGAOS)
    extra = FOTO_CSS + """
    .txt{position:absolute;left:84px;top:206px;right:84px}
    .eyebrow{font-size:21px;margin-bottom:20px}
    h1{font-size:96px;margin-bottom:14px}
    .sub{font-size:25px;color:#B9BDC6}
    .tags{position:absolute;left:84px;right:84px;top:470px;display:flex;flex-wrap:wrap;gap:20px}
    .tags span{padding:24px 34px;border-radius:14px;border:1.5px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);font-size:33px;font-weight:600;color:#ECEDF0}
    .num{position:absolute;right:92px;top:200px;text-align:right}
    .num b{font-family:Anton;font-size:120px;line-height:1;color:#fff;display:block}
    .num small{font-size:19px;letter-spacing:.16em;text-transform:uppercase;color:#FF5A5F;font-weight:700}
    """
    corpo = GLOBO + FAIXAS + """<img class="cab" src="%s/logo.png">
    <div class="txt"><div class="eyebrow">Quem já confia na DPA</div><h1 class="disp">Órgãos atendidos</h1><div class="sub">Minas Gerais, Rio de Janeiro, Bahia, Sergipe e Paraíba</div></div>
    <div class="tags">%s</div>
    <div class="rod"><span>Documentação sempre regular · <b>certidões em dia</b></span><span>distribuidoraperesearaujo.com.br</span></div>""" % (IMG, tags)
    return "google/foto-orgaos-atendidos.jpg", W, H, pagina(W, H, corpo, extra, fx=300)

# ---------- Instagram: capas de destaques 9:16 ----------
DESTAQUES = [("quem-somos", "mark"), ("segmentos", "grid"), ("como-atendemos", "check"),
             ("orgaos", "landmark"), ("novidades", "news"), ("contato", "chat")]

def destaque(slug, icone):
    W, H = 1080, 1920
    extra = """
    .fundo{background:radial-gradient(40% 24% at 50% 50%,rgba(215,20,26,.32),rgba(142,11,16,.10) 60%,transparent 80%),linear-gradient(170deg,#15161B,#0B0C0E)}
    .anel{position:absolute;left:50%;top:50%;width:620px;height:620px;transform:translate(-50%,-50%);border-radius:50%;
          border:3px solid rgba(255,90,95,.55);box-shadow:inset 0 0 0 22px rgba(255,255,255,.025);display:grid;place-items:center}
    .anel img{width:420px}
    """
    miolo = ('<img src="%s/mark.png">' % IMG) if icone == "mark" else ic(icone, 300, "#fff", 1.15)
    corpo = '<div class="anel">%s</div>' % miolo
    return "instagram-destaques/%s.png" % slug, W, H, pagina(W, H, corpo, extra)

def main():
    jobs = [capa(), logotipo()] + [foto_segmento(*s, n=i) for i, s in enumerate(SEGMENTOS, 1)] + \
           [foto_processo(), foto_orgaos()] + [destaque(*d) for d in DESTAQUES]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        for nome, w, h, html in jobs:
            dest = OUT / nome
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = OUT / "_tmp.html"
            tmp.write_text(html, encoding="utf-8")
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(tmp.as_uri()); pg.wait_for_timeout(400)
            if nome.endswith(".jpg"):
                pg.screenshot(path=str(dest), type="jpeg", quality=92)
            else:
                pg.screenshot(path=str(dest))
            pg.close(); tmp.unlink()
            print("ok", nome, w, h)
        b.close()

if __name__ == "__main__":
    main()
