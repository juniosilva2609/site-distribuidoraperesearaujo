# -*- coding: utf-8 -*-
"""Esteira de conteúdo 2027 da DPA: postagem em todo dia útil (fev-dez), story diário e 2 reels por semana.
  python3 plano_2027.py plano             -> out/2027/calendario_2027.csv (ano inteiro)
  python3 plano_2027.py render 2027-02    -> artes, reels e legendas do mês (out/2027/AAAA-MM/ + legendas_AAAA-MM.json)
Cadência: SEG carrossel "Segunda do Edital" 11:30 · TER reel de vendas 11:30 · QUA post de produto/segmento 11:30
· QUI reel de engajamento 18:30 · SEX post de conversão 11:30 · story todo dia útil (13:00; quinta 19:00)."""
import sys, os, re, json, csv, itertools, datetime as D
from multiprocessing import Pool
AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI); os.chdir(AQUI)
import dpa27 as M
import banco_2027 as B
TR = json.load(open("musica/trilhas.json"))
VENDAS = ["Voxel_Revolution", "Neon_Laser_Horizon", "Rocket_Power", "Funkorama", "Digital_Lemonade", "Hyperfun", "Galactic_Rap", "Funky_Chunk",
          "Disco_Medusae", "Upbeat_Forever", "Too_Cool", "Off_to_Osaka", "Newer_Wave", "Protofunk", "Itty_Bitty_8_Bit", "Werq", "Blippy_Trance", "Pump"]
LEVE = ["Monkeys_Spinning_Monkeys", "Investigations", "Fluffing_a_Duck", "Sneaky_Snitch", "Easy_Lemon", "Run_Amok", "Local_Forecast_-_Elevator",
        "Spy_Glass", "Brightly_Fancy", "Electrodoodle", "Bossa_Antigua", "Cheery_Monday"]
NOME_MUS = lambda f: f.replace("_-_", " - ").replace("_", " ")
WPP = '📲 Edital aberto? Chame no WhatsApp da bio e diga "Vim pelo Instagram".'
HT = ["#licitacao #pregaoeletronico #comprasPublicas #setorPublico #gestaoPublica #lei14133 #MinasGerais",
      "#licitacoes #pregoeiro #compraspublicas #servidorpublico #administracaopublica #fornecedor #prefeitura",
      "#pregao #empenho #ataderegistrodeprecos #setorpublico #gestaopublica #camaramunicipal #MinasGerais"]
plain = lambda h: re.sub(r"<[^>]+>", "", h).replace("&amp;", "&")
FIM = D.date(2027, 12, 31)

# ---------- datas especiais (fev-jul produzidas; ago-dez no plano, produzidas na época com conferência)
ESPECIAL = {
 "2027-02-08": ("story_so", "carnaval", "Carnaval", "Bom <mark>Carnaval</mark>!", "Descanse, aproveite com segurança. Na quarta, a gente volta com tudo."),
 "2027-02-09": ("nada",),
 "2027-03-26": ("story_so", "pascoa", "Sexta-feira Santa", "Feliz <mark>Páscoa</mark>!", "Que seja um tempo de renovação para você e sua família."),
 "2027-04-21": ("story_so", "tiradentes", "21 de abril", "Feriado de <mark>Tiradentes</mark>", "Bom descanso! Amanhã seguimos com os seus pedidos."),
 "2027-05-27": ("story_so", "corpus_christi", "Corpus Christi", "Bom <mark>feriado</mark>!", "Amanhã a DPA segue com você."),
}
ESP_FEED = {  # data -> (tipo, dados)
 "2027-03-08": ("carrossel", dict(slug="dia_da_mulher", k="8 de março", t="Elas fazem a compra pública <mark>acontecer</mark>", sub="Dia Internacional da Mulher.",
   telas=[("dica", "Na sessão", "Pregoeiras", "Conduzem a disputa com técnica e firmeza.", ""), ("dica", "No planejamento", "Gestoras e servidoras", "Do termo de referência ao empenho.", ""), ("dica", "Na entrega", "Fiscais", "Conferem, atestam e garantem o interesse público.", "")],
   ct="Feliz Dia da <b>Mulher</b>", cs="Nossa homenagem a todas que fazem o setor público acontecer.", leg="Pregoeiras, gestoras, servidoras e fiscais: elas fazem a compra pública acontecer. Feliz Dia Internacional da Mulher! 💐"), "08:00"),
 "2027-03-22": ("produto", dict(slug="dia_mundial_da_agua", k="22 de março · Dia Mundial da Água", t="Água boa <mark>no órgão</mark>", c="Bebedouros e purificadores para escolas, unidades de saúde e repartições.", itens=["Bebedouros", "Purificadores", "Geladeiras", "Freezers"]), "11:30"),
 "2027-04-01": ("reel_lei", None, "11:30"),
 "2027-04-07": ("kit", dict(seg="saude", k="7 de abril · Dia Mundial da Saúde"), "11:30"),
 "2027-04-23": ("kit", dict(seg="cultura", k="23 de abril · Dia Mundial do Livro"), "11:30"),
 "2027-04-28": ("kit", dict(seg="escola", k="28 de abril · Dia da Educação"), "11:30"),
 "2027-05-07": ("dica", dict(slug="dia_das_maes", k="Domingo é Dia das Mães", t="Para as mães que <mark>também servem</mark> ao público", c="Servidoras, gestoras e fornecedoras: nossa homenagem a quem cuida em dobro. Feliz Dia das Mães! 💐"), "11:30"),
 "2027-05-12": ("kit", dict(seg="saude", k="12 de maio · Dia Internacional da Enfermagem"), "11:30"),
 "2027-06-30": ("dica", dict(slug="fim_do_semestre", k="30 de junho", t="Metade do ano: <mark>planeje o 2º semestre</mark>", c="Revise o plano de contratações, veja os saldos e cote cedo o que vai comprar até dezembro."), "11:30"),
 "2027-07-16": ("dica", dict(slug="dia_do_comerciante", k="16 de julho · Dia do Comerciante", t="Comércio que <mark>serve o público</mark>", c="Desde 2015 a DPA atende o setor público com documentação em dia e entrega no prazo."), "11:30"),
}
PLANO_FUTURO = {  # pautas de ago-dez que dependem de dado da época (a rotina mensal confere e produz)
 "2027-08-06": "Dia dos Pais (domingo 08/08): homenagem aos pais servidores (post).",
 "2027-09-07": "Independência: post institucional 10:00.", "2027-09-09": "Dia do Administrador: post.",
 "2027-09-24": "Aniversário do Júnio (26/09, domingo): post pessoal só com foto e frase dele (pedir até 12/09).",
 "2027-10-12": "N. Sra. Aparecida e Dia das Crianças: só story.", "2027-10-15": "Dia do Professor: kit escola + homenagem.",
 "2027-10-28": "DIA DO SERVIDOR PÚBLICO: reel especial de homenagem (o post mais forte do ano).",
 "2027-11-15": "Proclamação da República: post 10:00.", "2027-11-26": "Black Friday: 'aqui o preço é o do edital' (se couber).",
 "2027-11": "Encerramento do exercício 2027: pesquisar decretos federal e de MG e preparar a série de dezembro.",
 "2027-12-24": "Natal (post + reel).", "2027-12-31": "Retrospectiva e agradecimento (sem números inventados).",
 "2027-03-08b": "Aniversário do Leo (08/03): post pessoal 18:30 só com foto e frase dele (pedir ao Júnio até 20/02).",
 "2027-12": "Reforma tributária: CBS/IBS 2028 (conferir alíquotas fixadas pelo Senado antes de publicar).",
}

def dias():
    d = D.date(2027, 2, 1)
    while d <= FIM:
        if d.weekday() < 5: yield d
        d += D.timedelta(1)

def ciclo(seq): return itertools.cycle(seq)
TER = [("linha", l, 0) for l in B.LINHAS] + [("seg", s, 0) for s in B.SEGMENTOS] + [("linha", l, 1) for l in B.LINHAS] + [("linha", l, 2) for l in B.LINHAS]
QUA = [("kit", s) for s in B.SEGMENTOS] + [("produto", l) for l in B.LINHAS]

def agenda():
    """Lista de dicts: data, hora, tipo (carrossel/reel/post/story), slug, dados, papel."""
    mi = [q for q in B.QUI if q["tipo"] == "mito"]; qz = [q for q in B.QUI if q["tipo"] == "quiz"]; ls = [q for q in B.QUI if q["tipo"] == "lista"]
    QUI = [x for trio in itertools.zip_longest(mi, ls, qz) for x in trio if x]
    c_seg, c_ter, c_qua, c_qui, c_sex = ciclo(B.SEG), ciclo(TER), ciclo(QUA), ciclo(QUI), ciclo(B.SEX)
    c_v, c_l = ciclo(VENDAS), ciclo(LEVE)
    out = []
    for d in dias():
        iso = d.isoformat(); wd = d.weekday()
        if iso in ESPECIAL:
            e = ESPECIAL[iso]
            if e[0] == "story_so": out.append(dict(data=iso, hora="10:00", tipo="story", slug=e[1], papel="data", dados=dict(k=e[2], t=e[3], c=e[4], b="")))
            continue
        if iso in ESP_FEED:
            tp, dados, hora = ESP_FEED[iso]
            if tp == "reel_lei":
                out.append(dict(data=iso, hora=hora, tipo="reel", slug="lei_14133_faz_6_anos", papel="especial", dados=None, mus=next(c_v)))
            elif tp == "kit":
                s = next(x for x in B.SEGMENTOS if x["slug"] == dados["seg"])
                out.append(dict(data=iso, hora=hora, tipo="post", slug=f"kit_{s['slug']}_{d.strftime('%m%d')}", papel="especial", dados=dict(seg=s, k=dados["k"]), kind="kit"))
            else:
                out.append(dict(data=iso, hora=hora, tipo="carrossel" if tp == "carrossel" else "post", slug=dados["slug"], papel="especial", dados=dados, kind=tp))
        else:
            if wd == 0: it = next(c_seg); out.append(dict(data=iso, hora="11:30", tipo="carrossel", slug=it["slug"], papel="seg", dados=it, kind="carrossel"))
            if wd == 1: it = next(c_ter); out.append(dict(data=iso, hora="11:30", tipo="reel", slug=f"{it[0]}_{it[1]['slug']}" + (f"_{it[2]+1}" if it[0] == "linha" else ""), papel="ter", dados=it, mus=next(c_v)))
            if wd == 2:
                it = next(c_qua); hora = "14:00" if iso == "2027-02-10" else "11:30"
                out.append(dict(data=iso, hora=hora, tipo="post", slug=f"{it[0]}_{it[1]['slug']}", papel="qua", dados=dict(seg=it[1], k=it[1]["k"]) if it[0] == "kit" else it[1], kind=it[0]))
            if wd == 3: it = next(c_qui); out.append(dict(data=iso, hora="18:30", tipo="reel", slug=f"{it['tipo']}_{it['slug']}", papel="qui", dados=it, mus=next(c_l)))
            if wd == 4: it = next(c_sex); out.append(dict(data=iso, hora="11:30", tipo="post", slug=it["slug"], papel="sex", dados=it, kind=it["tipo"]))
        f = out[-1]; tit = titulo_curto(f)
        quinta = f["papel"] == "qui"
        hs = "19:00" if quinta else ("14:30" if f["hora"] == "14:00" else "13:00")
        out.append(dict(data=iso, hora=hs, tipo="story", slug=f"novo_{f['slug']}"[:60], papel="story",
                        dados=dict(k="Novo reel 🎬" if f["tipo"] == "reel" else "Novo no feed", t=tit, c="Você acerta? Assista e comente." if quinta and f["dados"] and f["dados"].get("tipo") == "quiz" else "Toque no perfil e confira.", b="Ver agora")))
    return out

def titulo_curto(f):
    d = f["dados"]
    if f["slug"] == "lei_14133_faz_6_anos": return "Lei 14.133 faz <mark>6 anos</mark>"
    if f["papel"] == "ter":
        return d[1]["hooks"][d[2]] if d[0] == "linha" else d[1]["hook"]
    if f.get("kind") == "kit": return f"Kit <mark>{d['seg']['nome']}</mark>"
    if f.get("kind") == "numero": return f"<mark>{d['n']}</mark> {d['t']}"
    if f["papel"] == "qui":
        return {"mito": "Mito ou <mark>verdade</mark>?", "quiz": "Quiz da <mark>quinta</mark>"}.get(d["tipo"], d.get("k", ""))
    return d.get("t", "")

# ---------- reels
def r_vendas(item, mus):
    tp, x = item[0], item[1]
    if tp == "linha":
        hook = x["hooks"][item[2]]; benef = B.BENEF[(item[2] + len(x["slug"])) % len(B.BENEF)]
        cenas = [(2.8, f'<div class="k an">{x["k"]}</div><h1 class="an" style="--d:.25s">{hook}</h1>'),
                 (5.0, f'<div class="c"><div class="zoom" style="font-size:200px;line-height:1">{x["emo"]}</div><h2 class="an" style="--d:.3s;font-size:84px;margin-top:20px">{x["nome"]}</h2>' + M.chips_html(x["itens"], True, .8, .38) + '</div>'),
                 (3.2, f'<h1 class="an" style="font-size:116px">{benef}</h1>'),
                 (3.6, M.logo_cta("Mande o item <mark>do edital</mark>", "A DPA cota no padrão do seu processo."))]
    else:
        tiles = "".join(f'<div class="tile" style="--d:{.3+k*.4:.1f}s"><em>{e}</em><b>{t}</b></div>' for k, (e, t) in enumerate(x["tiles"]))
        cenas = [(2.8, f'<div class="k an">{x["k"]}</div><h1 class="an" style="--d:.25s">{x["hook"]}</h1>'),
                 (5.6, f'<div class="k an">Kit {x["nome"]}</div><div class="tiles" style="grid-template-columns:1fr 1fr 1fr">{tiles}</div>'),
                 (3.0, '<h1 class="an" style="font-size:116px">Tudo no <mark>mesmo CNPJ</mark>, com NF-e própria.</h1>'),
                 (3.6, M.logo_cta(f"Kit {x['nome']}: <mark>a DPA cota</mark>", "Mande a lista de itens ou o edital."))]
    return cenas

def r_qui(x):
    if x["tipo"] == "mito":
        selo = "VERDADE" if x["v"] else "MITO"
        return [(2.4, '<div class="c"><div class="k an">Quinta do mito ou verdade</div><h1 class="an" style="--d:.2s;font-size:150px">Mito ou <mark>verdade</mark>?</h1></div>'),
                (3.4, f'<h1 class="an" style="font-size:104px">“{x["frase"]}”</h1><p class="an" style="--d:1.2s;margin-top:40px">Pensa rápido… 🤔</p>'),
                (4.6, f'<div class="c"><span class="selo {selo.lower()}" style="--d:.2s">{selo}</span><h2 class="an" style="--d:.9s;font-size:68px;margin-top:70px">{x["exp"]}</h2><p class="fonte an" style="--d:1.4s;margin-top:30px">{x["fonte"]}</p></div>'),
                (3.4, M.logo_cta("Acertou? <mark>Comenta</mark>", "E manda para o colega do setor de compras.", "Siga para mais"))]
    if x["tipo"] == "quiz":
        ops = "".join(f'<div class="op{" certa" if i == x["certa"] else ""}" style="--d:{.4+i*.35:.2f}s;--r:3.6s"><i>{"ABC"[i]}</i><span>{o}</span></div>' for i, o in enumerate(x["ops"]))
        return [(2.2, '<div class="c"><div class="k an">Quiz da quinta</div><h1 class="an" style="--d:.2s;font-size:160px">Você <mark>acerta</mark>?</h1></div>'),
                (5.4, f'<h2 class="an" style="font-size:80px">{x["q"]}</h2>{ops}<p class="an" style="--d:1.6s;margin-top:40px">3… 2… 1…</p>'),
                (3.6, f'<div class="k an">Resposta: {"ABC"[x["certa"]]}) {x["ops"][x["certa"]]}</div><h2 class="an" style="--d:.3s;font-size:76px">{x["exp"]}</h2><p class="fonte an" style="--d:.8s;margin-top:30px">{x["fonte"]}</p>'),
                (3.4, M.logo_cta("Acertou? <mark>Comenta</mark> 👇", "Toda quinta tem desafio novo.", "Siga para mais"))]
    w = x["k"].split(" "); tit = " ".join(w[:-2]) + " <mark>" + " ".join(w[-2:]) + "</mark>"
    return [(2.8, f'<div class="k an">Quinta do desafio</div><h1 class="an" style="--d:.25s;font-size:104px">{tit}</h1>'),
            (5.4, M.chk(x["itens"], .3, 1.1)),
            (3.0, f'<h1 class="an" style="font-size:120px">{x["punch"]}</h1>'),
            (3.4, M.logo_cta("Marca quem <mark>precisa ver</mark>", "E siga para mais conteúdo do setor público.", "Siga a DPA"))]

def r_lei():
    return [(2.8, '<div class="c"><div class="k an">1º de abril de 2021 → 2027</div><div class="big zoom">6</div><h1 class="an" style="--d:.5s;font-size:120px">anos da <mark>Lei 14.133</mark></h1></div>'),
            (6.4, '<div class="k an">O que ela trouxe</div>' + M.chk(["Pregão obrigatório para bens comuns", "PNCP: tudo num portal", "Diálogo competitivo", "Agente de contratação", "Dispensa com aviso de 3 dias úteis"], .3, 1.1)),
            (3.0, '<h1 class="an" style="font-size:116px">E a DPA <mark>acompanha tudo</mark> desde o 1º dia.</h1>'),
            (3.6, M.logo_cta("Nova lei, <mark>mesmo compromisso</mark>", "Envie seu edital."))]

def cenas_de(f):
    if f["slug"] == "lei_14133_faz_6_anos": return r_lei()
    return r_vendas(f["dados"], f["mus"]) if f["papel"] == "ter" else r_qui(f["dados"])

# ---------- estáticos
def telas_carrossel(x):
    T = len(x["telas"]) + 2; out = [M.f_capa(x["k"], x["t"], x["sub"], 1, T)]
    for i, tl in enumerate(x["telas"], 2):
        if tl[0] == "lista": out.append(M.f_lista(tl[1], tl[2], tl[3], f"{i}/{T}", arr=True))
        else: out.append(M.f_dica(tl[1], tl[2], tl[3], tl[4], f"{i}/{T}", arr=True))
    out.append(M.cta(x["ct"], x["cs"], n=f"{T}/{T}")); return out

def html_post(f):
    x, kd = f["dados"], f.get("kind")
    if kd == "kit":
        s = x["seg"]; return M.f_kit(x["k"], f"Kit <mark>{s['nome']}</mark>: tudo num só fornecedor", s["tiles"], "→ Mande a lista ou o edital pelo WhatsApp da bio")
    if kd == "produto": return M.f_produto(x.get("k", ""), x.get("t") or f"{x['nome']}", x.get("c") or "Para órgãos públicos, no mesmo CNPJ, com NF-e própria.", x["itens"])
    if kd == "numero": return M.f_numero(x["k"], x["n"], x["t"], x["c"])
    if kd == "lista": return M.f_lista(x["k"], x["t"], x["itens"], simb="✓")
    return M.f_dica(x["k"], x["t"], x["c"])

# ---------- legendas
def legenda(f, n):
    x, p = f["dados"], f["papel"]; h = HT[n % 3]
    if f["tipo"] == "story": return ""
    if f["slug"] == "lei_14133_faz_6_anos":
        t = ("A Lei 14.133/2021 faz 6 anos hoje (sancionada em 1º de abril de 2021) 🎉\n\nO que ela trouxe: pregão obrigatório para bens e serviços comuns (art. 6º, XLI), PNCP (art. 174), "
             "diálogo competitivo (art. 28), agente de contratação (art. 8º) e dispensa com aviso de 3 dias úteis (art. 75, § 3º).\n\nE a DPA acompanha tudo desde o primeiro dia.")
    elif f["tipo"] == "carrossel":
        t = f"{plain(x['t'])} 👉 (arraste e salve)\n\n{x['leg']}\n\n{plain(x['ct'])}: {x['cs']}" + ("\n\nSegunda do Edital: toda segunda, uma regra da compra pública em 1 minuto." if p == "seg" else "")
    elif p == "ter":
        tp, y = x[0], x[1]
        if tp == "linha": t = f"{plain(y['hooks'][x[2]])} {y['emo']}\n\n{y['nome']}: {', '.join(y['itens'])}.\n\nPara {y['k'].lower()}, no mesmo CNPJ, com NF-e própria e documentação em dia. Mande o item do edital: a DPA cota."
        else: t = f"{plain(y['hook'])} ✨\n\nKit {y['nome']} ({y['k']}): " + ", ".join(b for _, b in y["tiles"]) + ".\n\nTudo num só fornecedor, uma proposta e uma NF-e. Mande a lista de itens ou o edital."
    elif p == "qui":
        if x["tipo"] == "mito": t = f"Mito ou verdade? 🤔\n\n“{plain(x['frase'])}”\n\nResposta: {'VERDADE' if x['v'] else 'MITO'}. {x['exp']} ({x['fonte']})\n\nAcertou? Comenta 👇 e manda para o colega do setor de compras."
        elif x["tipo"] == "quiz": t = f"Quiz da quinta 🧠\n\n{x['q']}\n" + "\n".join(f"{'ABC'[i]}) {o}" for i, o in enumerate(x["ops"])) + f"\n\nComenta a sua resposta antes de ver o vídeo 👇\n\n(Resposta: {'ABC'[x['certa']]}. {x['exp']} {x['fonte']}.)"
        else: t = f"{x['k']} 😅\n\n" + "\n".join(f"✅ {i}" for i in x["itens"]) + f"\n\n{plain(x['punch'])} Marca quem precisa ver 👇"
    elif f.get("kind") == "kit":
        s = x["seg"]; t = f"{x['k']}: Kit {s['nome']} ✨\n\n" + ", ".join(b for _, b in s["tiles"]) + ".\n\nTudo num só fornecedor, uma proposta e uma NF-e."
    elif f.get("kind") == "produto": t = f"{plain(x.get('t') or x['nome'])}\n\n{x.get('c') or 'Para órgãos públicos, no mesmo CNPJ, com NF-e própria.'}\n\n" + ", ".join(x["itens"]) + "."
    elif f.get("kind") == "numero": t = f"{x['n']} {x['t']} 📊\n\n{x['c']}"
    elif f.get("kind") == "lista": t = f"{plain(x['t'])}\n\n" + "\n".join(f"✔️ {i}" for i in x["itens"])
    else: t = f"{plain(x['t'])}\n\n{x['c']}"
    t += f"\n\n{WPP}\n\n{h}"
    if f["tipo"] == "reel": t += f'\n\n🎵 Música: "{NOME_MUS(f["mus"])}", de Kevin MacLeod (incompetech.com), licença Creative Commons BY 4.0.'
    return t

def chave(f):
    tp = {"post": "post", "carrossel": "carrossel", "reel": "reel", "story": "story"}[f["tipo"]]
    return f"{f['data']}_{tp}_{f['slug']}"

def _render_reel(args):
    out, cenas, mus = args
    if os.path.exists(out): return out
    tmp = out[:-4] + ".parcial.mp4"
    M.reel(tmp, cenas, f"musica/{mus}.mp3", TR[mus + ".mp3"]["ini"]); os.replace(tmp, out); return out

def render_mes(mes, reels=True):
    base = f"out/2027/{mes}/"; os.makedirs(base, exist_ok=True)
    ag = [f for f in agenda() if f["data"].startswith(mes)]
    pecas, rl, L = [], [], {}
    for n, f in enumerate(ag):
        ch = chave(f); L[ch] = dict(quando=f"{f['data']} {f['hora']}", legenda=legenda(f, n), tipo=f["tipo"])
        if f["tipo"] == "carrossel": pecas += [(f"{base}{ch}_{i}.jpg", h, "feed") for i, h in enumerate(telas_carrossel(f["dados"]), 1)]
        elif f["tipo"] == "post": pecas.append((f"{base}{ch}.jpg", html_post(f), "feed"))
        elif f["tipo"] == "story": pecas.append((f"{base}{ch}.jpg", M.s_story(f["dados"]["k"], f["dados"]["t"], f["dados"]["c"], f["dados"]["b"]), "story"))
        else: rl.append((f"{base}{ch}.mp4", cenas_de(f), f["mus"]))
    json.dump(L, open(f"out/2027/legendas_{mes}.json", "w"), ensure_ascii=False, indent=1)
    if pecas: M.render(pecas)
    if reels and rl:
        with Pool(3) as pool:
            for r in pool.imap_unordered(_render_reel, rl): print("reel ok", r, flush=True)
    print(mes, len(ag), "publicações,", len(pecas), "imagens,", len(rl), "reels")

def plano():
    os.makedirs("out/2027", exist_ok=True)
    with open("out/2027/calendario_2027.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["data", "dia", "hora", "tipo", "papel", "tema", "musica"])
        sem = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
        for f in agenda():
            dd = D.date.fromisoformat(f["data"])
            w.writerow([f["data"], sem[dd.weekday()], f["hora"], f["tipo"], f["papel"], plain(titulo_curto(f) if f["tipo"] != "story" else f["dados"]["t"]), NOME_MUS(f.get("mus", "")) if f.get("mus") else ""])
    print("ok calendario")

if __name__ == "__main__":
    if sys.argv[1] == "plano": plano()
    elif sys.argv[1] == "render": render_mes(sys.argv[2], reels="--sem-reels" not in sys.argv)
