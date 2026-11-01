# Site institucional — Distribuidora Peres & Araújo

Site estático (HTML/CSS/JS puro, sem dependências pagas), publicado pelo **GitHub Pages**
a partir da branch `master`, no domínio `distribuidoraperesearaujo.com.br`.

As páginas são **geradas** pelo `build.py` (Python 3, sem bibliotecas externas) a partir de:

- `_src/pages/*.html` — conteúdo de cada página (Home, Quem somos, Segmentos, Como atendemos, Contato);
- `novidades/novidades.json` — notícias da aba Novidades (uma entrada por notícia).

**Não edite à mão** `index.html`, `sobre/`, `segmentos/`, `como-atendemos/`, `contato/`, `novidades/index.html`,
`novidades/feed.xml`, `sitemap.xml`, `404.html` nem os redirecionamentos `*.html` — edite as fontes e rode
`python3 build.py`. A página `/links/` é a exceção: é mantida à mão em `links/index.html`.

### Publicar uma notícia
Veja `ROTINA-NOVIDADES.md`. Resumo: acrescentar o registro no JSON → `python3 build.py --check` →
`python3 build.py` → commit e push no `master`.

### 12 anos (08/01/2027 a 31/01/2027)
Programado por data, sem depender de ninguém: logo comemorativa no header e na `/links/`, faixa na home,
post "DPA completa 12 anos" e `og.jpg` comemorativa. Em 01/02/2027 tudo volta ao padrão. O JavaScript faz a
troca visual na hora exata e o workflow `.github/workflows/atualizar-site.yml` (diário, 00:07) regera o site
e troca a `og.jpg`. Para testar: `DPA_HOJE=2027-01-10 python3 build.py` (depois rode `python3 build.py` de novo).

## Como ver localmente

Os links usam caminhos absolutos (`/assets/...`), então sirva por HTTP:

```bash
python3 build.py
python3 -m http.server 8000
```

Depois acesse `http://localhost:8000`.

## Domínio

**Registrado:** `distribuidoraperesearaujo.com.br` (já refletido em todo o site:
canonical, Open Graph, `robots.txt` e `sitemap.xml`).

## Como publicar (custo mínimo: só o domínio, já pago)

Este site é 100% estático, então a hospedagem pode ser **gratuita**. Três opções,
todas sem custo de servidor — escolha uma:

### Opção 1 — Cloudflare Pages (recomendado)

1. Criar um repositório no GitHub e enviar esta pasta (`git remote add origin ...`
   e `git push`).
2. Em [pages.cloudflare.com](https://pages.cloudflare.com), conectar esse
   repositório — build command vazio, output directory `/` (raiz).
3. Em **Custom domains**, adicionar `distribuidoraperesearaujo.com.br` e
   `www.distribuidoraperesearaujo.com.br`.
4. No painel do registro.br, apontar o DNS do domínio para a Cloudflare
   (a própria Cloudflare Pages mostra os registros exatos — geralmente 2
   registros `NS`, ou `CNAME`/`A` se preferir manter o DNS no registro.br).

### Opção 2 — GitHub Pages

1. Mesmo passo 1 acima (subir para um repositório GitHub).
2. Nas configurações do repositório → **Pages** → escolher a branch `master`
   e pasta raiz.
3. Em **Custom domain**, informar `distribuidoraperesearaujo.com.br`.
4. No registro.br, criar os registros DNS que o GitHub Pages indicar
   (tipicamente `A` apontando para os IPs do GitHub Pages + um `CNAME` para
   `www`).

### Opção 3 — Netlify

1. Arrastar esta pasta direto no painel da Netlify (ou conectar ao GitHub).
2. Em **Domain settings**, adicionar `distribuidoraperesearaujo.com.br`.
3. Apontar o DNS conforme instruções da Netlify.

Em qualquer uma das três, o certificado HTTPS é emitido automaticamente e
sem custo pela própria plataforma.

## Formulário de contato

O formulário da página `contato.html` usa o serviço gratuito **FormSubmit**
(sem necessidade de conta ou backend próprio). **No primeiro envio real**, o
FormSubmit manda um e-mail de confirmação para `distribuidora.peres@hotmail.com`
pedindo para ativar o recebimento — é preciso abrir esse e-mail e confirmar uma
única vez, senão as mensagens seguintes não chegam.

## Estrutura

```
build.py                 Gerador do site (valida e gera as páginas)
_src/pages/              Conteúdo das páginas (não publicado; o Jekyll do GitHub Pages ignora pastas com "_")
novidades/novidades.json Notícias
links/                   Página de links (index.html, og.jpg, contato.vcf)
assets/css/site.css      Estilo único (identidade grafite e vermelho, Anton + Montserrat)
assets/js/site.js        Menu, seletor de WhatsApp, animações, contagem de anos, período de 12 anos, filtro
assets/fonts/            Anton e Montserrat (woff2, hospedadas no site)
assets/img/              Logo (WebP), favicons, og-padrao.jpg, mosaico do Instagram, glifo oficial do Instagram
assets/img/12anos/       Logos oficiais de 12 anos e og-12anos.jpg
.github/workflows/       Regeração diária automática
```

O glifo do Instagram (`assets/img/instagram-glyph-branco.svg`) é o arquivo oficial do Meta Brand Resources
(versão branca), usado sem alterações de forma ou cor.
