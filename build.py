#!/usr/bin/env python3
"""Gera o site estático da Distribuidora Peres & Araújo.

Uso:
    python3 build.py            valida novidades/novidades.json e gera todas as páginas
    python3 build.py --check    só valida (não grava nada)

Variável opcional DPA_HOJE=AAAA-MM-DD simula outra data (testes do período de 12 anos).

Fontes:   _src/pages/*.html (conteúdo das páginas) e novidades/novidades.json (notícias).
Geradas:  index.html, sobre/, segmentos/, como-atendemos/, contato/, novidades/ (+ feed.xml),
          404.html, sitemap.xml, páginas antigas *.html (redirecionamento) e a og.jpg do período.
Não edite as páginas geradas à mão: edite _src/ ou o JSON e rode o build.
A página /links/ é mantida à parte (links/index.html) e não é gerada aqui.
"""
import datetime as dt
import html
import json
import os
import re
import shutil
import sys
from urllib.parse import quote, urlparse

RAIZ = os.path.dirname(os.path.abspath(__file__))
SITE = "https://distribuidoraperesearaujo.com.br"
IG_URL = "https://www.instagram.com/distribuidoraperesearaujo"
MSG_WA = ("Olá, tudo bem? Acessei o site da Distribuidora Peres & Araújo e gostaria de receber "
          "mais informações sobre produtos e condições de fornecimento. Desde já, agradeço.")
SOCIOS = [("Leonardo", "5531997186304", "(31) 99718-6304"), ("Júnio", "5531998902018", "(31) 99890-2018")]
CATEGORIAS = {"Licitações": "licitacoes", "Reforma Tributária": "reforma", "DPA": "dpa"}
FUNDACAO = dt.date(2015, 1, 8)
FESTA_INI, FESTA_FIM = dt.date(2027, 1, 8), dt.date(2027, 1, 31)
DOMINIOS_OFICIAIS = ("planalto.gov.br", "gov.br", "portal.tcu.gov.br", "tcu.gov.br", "tce.mg.gov.br", "almg.gov.br",
                     "mg.gov.br", "fazenda.mg.gov.br", "planejamento.mg.gov.br", "camara.leg.br", "senado.leg.br",
                     "in.gov.br", "iof.mg.gov.br", "jornalminasgerais.mg.gov.br")
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]
MESES_RSS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def hoje_brt():
    if os.environ.get("DPA_HOJE"):
        return dt.date.fromisoformat(os.environ["DPA_HOJE"])
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=3)).date()


HOJE = hoje_brt()
FESTA = FESTA_INI <= HOJE <= FESTA_FIM
ANOS = HOJE.year - FUNDACAO.year - (1 if (HOJE.month, HOJE.day) < (FUNDACAO.month, FUNDACAO.day) else 0)
e = html.escape


def wa_link(numero):
    return "https://wa.me/%s?text=%s" % (numero, quote(MSG_WA, safe="-_.!~*'()"))


def data_br(d):
    return d.strftime("%d/%m/%Y")


def data_extenso(d):
    return "%d de %s de %d" % (d.day, MESES[d.month - 1], d.year)


# ---------------------------------------------------------------- ícones
IG_GLYPH = re.search(r'\sd="([^"]+)"', open(os.path.join(RAIZ, "assets/img/instagram-glyph-branco.svg")).read()).group(1)


def ig_glyph(cls="ig-glyph"):
    return ('<svg class="%s" viewBox="0 0 1000 1000" aria-hidden="true" focusable="false">'
            '<path fill="#fff" d="%s"/></svg>' % (cls, IG_GLYPH))


WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11.5a8.5 8.5 0 0 1-12.6 7.4L3.5 20l1.2-3.7A8.5 8.5 0 1 1 20 11.5Z"/>'
           '<path d="M9 8.6c.2-.4.5-.4.8-.4h.4c.2 0 .4.1.5.4l.6 1.4c.1.2 0 .5-.1.7l-.5.6c.6 1.1 1.4 1.9 2.5 2.5l.6-.5c.2-.2.5-.2.7-.1l1.4.6c.3.1.4.3.4.5v.4c0 .3-.1.6-.4.8-.5.4-1.2.6-1.9.4A8.4 8.4 0 0 1 8.6 10.5c-.2-.7 0-1.4.4-1.9Z"/></svg>')


def wa_lista(titulo="Escolha com quem falar"):
    itens = "".join(
        '<a href="%s" target="_blank" rel="noopener"><span class="av">%s</span><span><strong>%s</strong>'
        '<small>Sócio-fundador · %s</small></span></a>' % (e(wa_link(n)), WA_ICON, nome, tel)
        for nome, n, tel in SOCIOS)
    return '<div class="wa-lista"><div class="tit">%s</div>%s</div>' % (titulo, itens)


def wa_botao(classes, rotulo):
    return ('<details class="wa-escolha wa-btn"><summary class="%s">%s <span class="seta" aria-hidden="true"></span>'
            '</summary>%s</details>' % (classes, rotulo, wa_lista()))


# ---------------------------------------------------------------- dados
def carregar_novidades():
    caminho = os.path.join(RAIZ, "novidades/novidades.json")
    itens = json.load(open(caminho, encoding="utf-8"))
    erros, ids = [], set()
    for i, n in enumerate(itens):
        ref = "registro %d (%s)" % (i + 1, n.get("titulo", "?"))
        for campo in ("id", "data", "categoria", "titulo", "resumo", "fonte", "url"):
            if not str(n.get(campo, "")).strip():
                erros.append("%s: campo obrigatório '%s' vazio" % (ref, campo))
        try:
            n["_data"] = dt.date.fromisoformat(n.get("data", ""))
        except ValueError:
            erros.append("%s: data inválida (use AAAA-MM-DD)" % ref)
        if n.get("categoria") not in CATEGORIAS:
            erros.append("%s: categoria deve ser uma de %s" % (ref, ", ".join(CATEGORIAS)))
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n.get("id", "")):
            erros.append("%s: id deve ter só letras minúsculas, números e hífens" % ref)
        if n.get("id") in ids:
            erros.append("%s: id repetido" % ref)
        ids.add(n.get("id"))
        u = urlparse(n.get("url", ""))
        host = (u.hostname or "").lower()
        oficial = any(host == d or host.endswith("." + d) for d in DOMINIOS_OFICIAIS)
        if n.get("categoria") == "DPA":
            oficial = oficial or host in ("www.instagram.com", "instagram.com", "distribuidoraperesearaujo.com.br")
        if u.scheme != "https" or not oficial:
            erros.append("%s: url precisa ser https e de fonte oficial permitida (%s)" % (ref, host or "vazia"))
        frases = len(re.findall(r"[.!?](\s|$)", n.get("resumo", "")))
        if not 2 <= frases <= 4:
            erros.append("%s: resumo deve ter de 2 a 4 frases (tem %d)" % (ref, frases))
    if erros:
        sys.exit("ERRO em novidades.json:\n  - " + "\n  - ".join(erros))
    itens.sort(key=lambda n: (n["_data"], n["id"]), reverse=True)
    return itens


NOVIDADES = carregar_novidades()
PUBLICADAS = [n for n in NOVIDADES if n["_data"] <= HOJE]
ULTIMA = PUBLICADAS[0]["_data"] if PUBLICADAS else HOJE


def card_novidade(n, nivel="h3"):
    cat = CATEGORIAS[n["categoria"]]
    tag = ' <span class="tag">%s</span>' % e(n["tag"]) if n.get("tag") else ""
    futuro = n["_data"] > HOJE
    return ('<article class="news-card revelar" id="%s" data-cat="%s" data-publicar="%s"%s>'
            '<div class="news-meta"><time datetime="%s">%s</time><span class="badge cat-%s">%s</span></div>'
            '<%s>%s</%s><p>%s</p><p class="news-fonte">Fonte: %s%s</p>'
            '<a class="btn btn-primario" href="%s" target="_blank" rel="noopener">%s<span class="sr-only"> (abre em nova aba)</span></a>'
            '</article>' % (
                n["id"], cat, n["data"], " hidden" if futuro else "", n["data"], data_br(n["_data"]), cat,
                e(n["categoria"]), nivel, e(n["titulo"]), nivel, e(n["resumo"]), e(n["fonte"]), tag, e(n["url"]),
                e(n.get("botao") or "Ler na fonte oficial ↗")))


# ---------------------------------------------------------------- blocos
NAV = [("Quem somos", "/sobre/"), ("Segmentos", "/segmentos/"), ("Como atendemos", "/como-atendemos/"),
       ("Órgãos atendidos", "/#orgaos"), ("Novidades", "/novidades/"), ("Contato", "/contato/")]

ORGAOS = ["PMMG", "Polícia Civil MG", "DER-MG", "EPAMIG", "IEF-MG", "TCE-MG", "FHEMIG", "SEJUSP-MG", "Prefeituras",
          "Câmaras", "Universidades", "Autarquias"]

PASSOS = [
    ("Edital e cotação", "Você nos envia o edital, o item ou o termo de referência, e fazemos a cotação."),
    ("Proposta", "Elaboramos a proposta com especificação técnica, marca e valor compatíveis com o edital."),
    ("Empenho / AF", "Recebemos o empenho ou a autorização de fornecimento e confirmamos prazo e garantia."),
    ("Entrega", "Entregamos no endereço indicado, dentro do prazo do empenho."),
    ("Nota fiscal e acompanhamento", "NF-e própria emitida na hora e acompanhamento até o recebimento, com garantia conforme o edital."),
]

MOSAICO = [
    ("post-1", "Post: 11 anos entregando o que o edital pede"),
    ("post-2", "Post: o que a DPA fornece para o setor público"),
    ("post-3", "Post: do edital à entrega em 4 passos"),
    ("post-4", "Post: quem já contou com a DPA — órgãos atendidos"),
    ("post-5", "Post: 3 motivos para ter a DPA como fornecedor"),
    ("post-6", "Post: por que ter a DPA como seu fornecedor?"),
]


def header(caminho):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == caminho else "", t) for t, h in NAV)
    return """<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="container">
    <a href="/" class="marca" aria-label="Distribuidora Peres &amp; Araújo — página inicial">
      <img class="logo-std" src="/assets/img/logo.webp" width="359" height="120" alt="Distribuidora Peres &amp; Araújo">
      <img class="logo-12" src="/assets/img/12anos/logo-12anos.webp" width="349" height="120" alt="Distribuidora Peres &amp; Araújo — 12 anos" loading="lazy">
    </a>
    <button class="hamb" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <nav class="menu" id="menu" aria-label="Menu principal">
      %s
      <a class="ig-link" href="%s" target="_blank" rel="noopener" aria-label="Instagram @distribuidoraperesearaujo">%s<span class="sr-only sr-txt">Instagram</span></a>
      <details class="wa-escolha wa-header"><summary>Fale no WhatsApp <span class="seta" aria-hidden="true"></span></summary>%s</details>
    </nav>
  </div>
</header>""" % (links, IG_URL, ig_glyph(), wa_lista())


def footer():
    nav = "".join('<a href="%s">%s</a>' % (h, t) for t, h in NAV)
    socios = "".join('<a href="%s" target="_blank" rel="noopener">%s · %s</a>' % (e(wa_link(n)), nome, tel)
                     for nome, n, tel in SOCIOS)
    return """<footer class="site-footer escuro">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-marca"><img src="/assets/img/logo.webp" width="359" height="120" alt="Distribuidora Peres &amp; Araújo" loading="lazy"></div>
        <p class="footer-dados"><strong>Distribuidora Peres &amp; Araújo Ltda</strong><br>CNPJ 21.641.059/0001-39<br>Ibirité/MG · Fornecedora do setor público desde 2015</p>
      </div>
      <div><h2>Navegação</h2>%s</div>
      <div><h2>Fale com a gente</h2>%s<a href="mailto:distribuidora.peres@hotmail.com">distribuidora.peres@hotmail.com</a></div>
      <div><h2>Siga a DPA</h2><a class="footer-ig" href="%s" target="_blank" rel="noopener">%s @distribuidoraperesearaujo</a><a href="/links/">Links oficiais</a><a href="/novidades/feed.xml">Feed RSS das novidades</a></div>
    </div>
    <div class="footer-linha">
      <span>© <span data-ano>%d</span> Distribuidora Peres &amp; Araújo Ltda · CNPJ 21.641.059/0001-39</span>
      <span>Última atualização: <time datetime="%s">%s</time></span>
    </div>
  </div>
</footer>
<details class="wa-escolha wa-flutuante"><summary aria-label="Fale no WhatsApp">%s</summary>%s</details>""" % (
        nav, socios, IG_URL, ig_glyph(), HOJE.year, ULTIMA.isoformat(), data_br(ULTIMA), WA_ICON, wa_lista())


def jsonld_org():
    d = {
        "@context": "https://schema.org",
        "@type": ["Organization", "LocalBusiness"],
        "@id": SITE + "/#empresa",
        "name": "Distribuidora Peres & Araújo",
        "alternateName": "DPA",
        "legalName": "Distribuidora Peres & Araújo Ltda",
        "taxID": "21.641.059/0001-39",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo.png",
        "image": SITE + "/assets/img/og.jpg",
        "foundingDate": "2015-01-08",
        "description": "Fornecedora de órgãos públicos via licitações desde 2015: informática e tecnologia, climatização, eletrodomésticos, ferramentas e equipamentos, eletroeletrônicos.",
        "email": "distribuidora.peres@hotmail.com",
        "telephone": "+55-31-99718-6304",
        "address": {"@type": "PostalAddress", "streetAddress": "Rua Antônio Germano, 688 — Palmares, 2ª Seção",
                    "addressLocality": "Ibirité", "addressRegion": "MG", "postalCode": "32430-090", "addressCountry": "BR"},
        "areaServed": [{"@type": "State", "name": "Minas Gerais"}, {"@type": "Country", "name": "Brasil"}],
        "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "name": nome, "telephone": "+" + n,
                          "availableLanguage": "pt-BR"} for nome, n, _ in SOCIOS],
        "sameAs": [IG_URL],
    }
    return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False)


def timeline():
    itens = "".join('<li class="revelar"><span class="n">%d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i, t, p)
                    for i, (t, p) in enumerate(PASSOS, 1))
    return '<ol class="timeline">%s</ol>' % itens


def orgaos():
    ul = "<ul%%s>%s</ul>" % "".join("<li>%s</li>" % o for o in ORGAOS)
    return (ul % "") + (ul % ' aria-hidden="true"')


def mosaico():
    return "".join(
        '<a href="%s" target="_blank" rel="noopener"><picture><source srcset="/assets/img/instagram/%s.avif" type="image/avif">'
        '<img src="/assets/img/instagram/%s.webp" width="480" height="600" alt="%s" loading="lazy" decoding="async"></picture></a>'
        % (IG_URL, f, f, e(alt)) for f, alt in MOSAICO)


def segmentos_home():
    s = open(os.path.join(RAIZ, "_src/pages/segmentos.html"), encoding="utf-8").read()
    itens = re.findall(r'<div class="icone">(<svg.*?</svg>)</div>\s*<div>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>', s, re.S)
    return "".join('<a class="card revelar" href="/segmentos/"><div class="icone">%s</div><h3>%s</h3><p>%s</p></a>'
                   % (svg.replace("<svg ", '<svg aria-hidden="true" '), h, p) for svg, h, p in itens)


def aviso_novidade():
    if not PUBLICADAS:
        return ""
    n = PUBLICADAS[0]
    rotulo = "Novidades desta semana" if (HOJE - n["_data"]).days <= 7 else "Última novidade"
    return ('<a class="aviso-novidade entrada" href="/novidades/#%s"><b>%s</b><span>%s</span><i aria-hidden="true">→</i></a>'
            % (n["id"], rotulo, e(n["titulo"])))


def substituir(corpo):
    corpo = corpo.replace("<span data-anos>{{ANOS}}</span>", "<span data-anos>%d</span>" % ANOS)
    corpo = corpo.replace("{{ANOS}}", "<span data-anos>%d</span>" % ANOS)
    corpo = re.sub(r"\{\{WA_BTN:([^|}]+)(?:\|([^}]+))?\}\}", lambda m: wa_botao(m.group(1), m.group(2) or "Falar no WhatsApp"), corpo)
    corpo = re.sub(r"\{\{WA:(\d+)\}\}", lambda m: e(wa_link(m.group(1))), corpo)
    blocos = {"TIMELINE": timeline, "ORGAOS": orgaos, "MOSAICO": mosaico, "SEGMENTOS_HOME": segmentos_home,
              "AVISO_NOVIDADE": aviso_novidade, "IG_GLYPH": ig_glyph,
              "NEWS_HOME": lambda: "".join(card_novidade(n) for n in PUBLICADAS[:3]) or '<p class="vazio">Em breve.</p>'}
    for k, f in blocos.items():
        if "{{%s}}" % k in corpo:
            corpo = corpo.replace("{{%s}}" % k, f())
    corpo = corpo.replace("{{ANOS}}", str(ANOS))
    falta = re.findall(r"\{\{[^}]+\}\}", corpo)
    if falta:
        sys.exit("ERRO: marcador sem valor: %s" % falta)
    return corpo


def pagina(caminho, titulo, desc, corpo, extra_head=""):
    og = SITE + "/assets/img/og.jpg"
    return """<!DOCTYPE html>
<html lang="pt-BR"%s>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="theme-color" content="#0B0C0E">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Distribuidora Peres &amp; Araújo">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Distribuidora Peres &amp; Araújo — Fornecedora do setor público desde 2015">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%s">
<meta name="twitter:description" content="%s">
<meta name="twitter:image" content="%s">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/assets/img/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/favicon-180.png">
<link rel="alternate" type="application/rss+xml" title="Novidades DPA" href="/novidades/feed.xml">
<link rel="preload" href="/assets/fonts/anton-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v=%s">
<script>document.documentElement.classList.add('js')</script>
<script src="/assets/js/site.js?v=%s" defer></script>
%s
</head>
<body>
%s
<main id="conteudo">
%s
</main>
%s
</body>
</html>
""" % (' class="festa12"' if FESTA else "", e(titulo), e(desc), SITE + caminho, e(titulo), e(desc), SITE + caminho, og,
       e(titulo), e(desc), og, VERSAO, VERSAO, extra_head, header(caminho), corpo.strip(), footer())


def ler_fonte(nome):
    s = open(os.path.join(RAIZ, "_src/pages", nome + ".html"), encoding="utf-8").read()
    m = re.match(r"<!--(.*?)-->\n", s, re.S)
    return json.loads(m.group(1)), s[m.end():]


def gravar(rel, conteudo):
    destino = os.path.join(RAIZ, rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)


def hero_pagina(migalha, titulo, sub):
    return ('<section class="hero-pagina escuro brilho"><div class="container"><div class="migalha"><a href="/">Início</a> / %s</div>'
            '<h1>%s</h1><p class="sub">%s</p></div></section>' % (migalha, titulo, sub))


def pagina_novidades():
    filtros = '<button type="button" data-cat="todas" aria-pressed="true">Todas</button>' + "".join(
        '<button type="button" data-cat="%s" aria-pressed="false">%s</button>' % (v, k) for k, v in CATEGORIAS.items())
    cards = "".join(card_novidade(n, "h2") for n in NOVIDADES if n["_data"] <= HOJE + dt.timedelta(days=45))
    corpo = hero_pagina("Novidades", "Novidades <em>DPA</em>",
                        "Licitações, reforma tributária e notícias da DPA, em resumos simples e sempre com o link da fonte oficial.")
    corpo += ('<section class="secao-cinza"><div class="container"><div class="filtros" role="group" aria-label="Filtrar por categoria">%s</div>'
              '<div class="news-grid">%s</div>'
              '<p class="aviso-fontes">Resumos informativos. Consulte sempre a fonte oficial.<br>'
              '<a href="/novidades/feed.xml">Assine o feed RSS</a> · Última atualização em %s.</p></div></section>'
              % (filtros, cards, data_extenso(ULTIMA)))
    css = "<style>.news-card h2{font-family:var(--sans);text-transform:none;font-size:18px;line-height:1.3;margin:0 0 10px;font-weight:700;letter-spacing:0}</style>"
    return pagina("/novidades/", "Novidades — Licitações e Reforma Tributária | DPA",
                  "Resumos semanais sobre licitações (Lei 14.133/2021, PNCP), reforma tributária (CBS e IBS) e notícias da Distribuidora Peres & Araújo, com link para a fonte oficial.",
                  corpo, css)


def feed():
    def rfc822(d):
        return "%s, %02d %s %d 09:00:00 -0300" % (["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][d.weekday()], d.day,
                                                  MESES_RSS[d.month - 1], d.year)
    itens = "".join("""
  <item>
    <title>%s</title>
    <link>%s/novidades/#%s</link>
    <guid isPermaLink="false">dpa-novidade-%s</guid>
    <pubDate>%s</pubDate>
    <category>%s</category>
    <description>%s</description>
  </item>""" % (e(n["titulo"]), SITE, n["id"], n["id"], rfc822(n["_data"]), e(n["categoria"]),
                e("%s Fonte: %s — %s" % (n["resumo"], n["fonte"], n["url"]))) for n in PUBLICADAS[:30])
    return """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Novidades — Distribuidora Peres &amp; Araújo</title>
  <link>%s/novidades/</link>
  <atom:link href="%s/novidades/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Licitações, reforma tributária e notícias da DPA, com link para a fonte oficial.</description>
  <language>pt-BR</language>
  <lastBuildDate>%s</lastBuildDate>%s
</channel>
</rss>
""" % (SITE, SITE, rfc822(ULTIMA), itens)


def redirecionar(destino):
    return """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Distribuidora Peres &amp; Araújo</title>
<link rel="canonical" href="%s%s"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=%s">
<script>location.replace("%s"+location.hash)</script></head>
<body><p>Esta página mudou de endereço: <a href="%s">%s%s</a></p></body></html>
""" % (SITE, destino, destino, destino, destino, SITE, destino)


def sitemap(paginas):
    urls = "".join("\n  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (SITE, p, lm, pr)
                   for p, lm, pr in paginas)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s\n</urlset>\n' % urls


def og_do_periodo():
    origem = "assets/img/12anos/og-12anos.jpg" if FESTA else "assets/img/og-padrao.jpg"
    for destino in ("assets/img/og.jpg", "links/og.jpg"):
        a, b = os.path.join(RAIZ, origem), os.path.join(RAIZ, destino)
        if not os.path.exists(b) or open(a, "rb").read() != open(b, "rb").read():
            shutil.copyfile(a, b)


VERSAO = "1"


def main():
    global VERSAO
    if "--check" in sys.argv:
        print("novidades.json OK: %d registros (%d publicados até %s)" % (len(NOVIDADES), len(PUBLICADAS), data_br(HOJE)))
        return
    import hashlib
    VERSAO = hashlib.sha1(open(os.path.join(RAIZ, "assets/css/site.css"), "rb").read()
                          + open(os.path.join(RAIZ, "assets/js/site.js"), "rb").read()).hexdigest()[:8]

    meta, corpo = ler_fonte("index")
    gravar("index.html", pagina("/", meta["title"], meta["desc"], substituir(corpo), jsonld_org()))

    internas = {
        "sobre": ("/sobre/", "Quem somos", "Mais de uma década fornecendo para o <em>setor público</em>"),
        "segmentos": ("/segmentos/", "Segmentos", None),
        "como-atendemos": ("/como-atendemos/", "Como atendemos", None),
        "contato": ("/contato/", "Contato", None),
    }
    for nome, (caminho, _, _) in internas.items():
        meta, corpo = ler_fonte(nome)
        corpo = re.sub(r'<section class="hero-pagina">', '<section class="hero-pagina escuro brilho">', corpo, count=1)
        gravar(nome + "/index.html", pagina(caminho, meta["title"], meta["desc"], substituir(corpo)))

    gravar("novidades/index.html", pagina_novidades())
    gravar("novidades/feed.xml", feed())

    gravar("404.html", pagina("/404.html", "Página não encontrada — Distribuidora Peres & Araújo",
                              "A página procurada não existe.",
                              hero_pagina("404", "Página não <em>encontrada</em>",
                                          "O endereço pode ter mudado. Use o menu acima ou volte para a página inicial.")
                              + '<section class="secao-clara"><div class="container centro"><a class="btn btn-primario" href="/">Ir para o início</a></div></section>',
                              '<meta name="robots" content="noindex">'))

    for antigo, novo in (("sobre.html", "/sobre/"), ("segmentos.html", "/segmentos/"),
                         ("licitacoes.html", "/como-atendemos/"), ("contato.html", "/contato/")):
        gravar(antigo, redirecionar(novo))

    lm = ULTIMA.isoformat()
    gravar("sitemap.xml", sitemap([("/", lm, "1.0"), ("/sobre/", lm, "0.8"), ("/segmentos/", lm, "0.8"),
                                   ("/como-atendemos/", lm, "0.9"), ("/contato/", lm, "0.7"),
                                   ("/novidades/", lm, "0.9"), ("/links/", lm, "0.6")]))
    og_do_periodo()
    print("Site gerado para %s (%d anos%s). Novidades publicadas: %d. Última: %s." % (
        data_br(HOJE), ANOS, ", período 12 anos" if FESTA else "", len(PUBLICADAS),
        PUBLICADAS[0]["titulo"] if PUBLICADAS else "-"))


if __name__ == "__main__":
    main()
