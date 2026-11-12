# Uso: python3 publicar_mes.py AAAA-MM  -> entrega ao ERP (links do ramo midia-instagram) e grava legenda/horário como RASCUNHO.
# Não aprova: a aprovação é do Júnio (tela "Aprovar os N prontos" ou ordem expressa na conversa).
import json, os, sys, glob, subprocess, time
S = os.path.dirname(os.path.abspath(__file__)); mes = sys.argv[1]
ERP = "/home/user/PlataformaERP-DPA"
B = "https://raw.githubusercontent.com/juniosilva2609/site-distribuidoraperesearaujo/midia-instagram"


def cli(*a):
    d = {}
    for _ in range(6):
        r = subprocess.run(["python", "ferramentas/enviar_pre_nota.py", *a], cwd=ERP, capture_output=True, text=True)
        try:
            d = json.loads(r.stdout)
        except Exception:
            d = {"erro": (r.stdout + r.stderr)[-300:]}
        if d.get("http") == 429:
            time.sleep(90)
            continue
        time.sleep(4.5)
        return d
    return d


L = json.load(open(f"{S}/out/2027/legendas_{mes}.json"))
arqs = sorted(a for a in glob.glob(f"{S}/out/2027/{mes}/*") if a.endswith((".jpg", ".mp4")) and ".parcial." not in a)
links = [{"nome": os.path.basename(a), "url": f"{B}/{mes}/{os.path.basename(a)}"} for a in arqs]
json.dump(links, open(f"{S}/links_{mes}.json", "w"))
for _ in range(4):
    d = cli("instagram-links", f"{S}/links_{mes}.json")
    print("links", {k: v for k, v in d.items() if k != "posts"}, flush=True)
    if d.get("baixados", 1) == 0 and d.get("novos", 1) == 0:
        break
q = cli("sql", f"SELECT id, chave, estado FROM marketing_post WHERE chave LIKE '{mes}-%'")
ids = {c: (i, e) for i, c, e in q["linhas"]}
feitos = 0
for ch, v in sorted(L.items(), key=lambda x: x[1]["quando"]):
    if ch not in ids:
        print("FALTA", ch, flush=True)
        continue
    pid, est = ids[ch]
    if est != "RASCUNHO":
        continue
    f = f"{S}/leg/{mes}_{pid}.txt"
    open(f, "w").write(v["legenda"])
    r = cli("instagram-legenda", str(pid), "--arquivo", f, "--quando", v["quando"])
    feitos += r.get("estado") == "RASCUNHO"
print(mes, "rascunhos com legenda e horário:", feitos, "de", len(L), flush=True)
