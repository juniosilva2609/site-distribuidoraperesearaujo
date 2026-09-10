# Site institucional — Distribuidora Peres & Araújo

Site estático (HTML/CSS/JS puro, sem build, sem dependências pagas) com 5 páginas:
`index.html` (Home), `sobre.html`, `segmentos.html`, `licitacoes.html`, `contato.html`.

Conteúdo montado a partir de dados reais da empresa: contrato social consolidado
(objeto social, CNPJ, data de fundação, sede) e amostra de notas fiscais de saída
de 2026 (segmentos de produtos e órgãos públicos atendidos). A logo usada é a
versão "Logo 2026 comemorativa 11 anos" fornecida pelo proprietário.

## Como ver localmente

Não precisa de servidor — pode abrir `index.html` direto no navegador. Ou, se
preferir servir por HTTP (recomendado para testar o formulário/links relativos):

```bash
cd site-dpa
python -m http.server 8000
```

Depois acesse `http://localhost:8000`.

## Domínio

**Registrado:** `peresaraujo.com.br` (já refletido em todo o site:
canonical, Open Graph, `robots.txt` e `sitemap.xml`).

## Como publicar (custo mínimo: só o domínio, já pago)

Este site é 100% estático, então a hospedagem pode ser **gratuita**. Três opções,
todas sem custo de servidor — escolha uma:

### Opção 1 — Cloudflare Pages (recomendado)

1. Criar um repositório no GitHub e enviar esta pasta (`git remote add origin ...`
   e `git push`).
2. Em [pages.cloudflare.com](https://pages.cloudflare.com), conectar esse
   repositório — build command vazio, output directory `/` (raiz).
3. Em **Custom domains**, adicionar `peresaraujo.com.br` e
   `www.peresaraujo.com.br`.
4. No painel do registro.br, apontar o DNS do domínio para a Cloudflare
   (a própria Cloudflare Pages mostra os registros exatos — geralmente 2
   registros `NS`, ou `CNAME`/`A` se preferir manter o DNS no registro.br).

### Opção 2 — GitHub Pages

1. Mesmo passo 1 acima (subir para um repositório GitHub).
2. Nas configurações do repositório → **Pages** → escolher a branch `master`
   e pasta raiz.
3. Em **Custom domain**, informar `peresaraujo.com.br`.
4. No registro.br, criar os registros DNS que o GitHub Pages indicar
   (tipicamente `A` apontando para os IPs do GitHub Pages + um `CNAME` para
   `www`).

### Opção 3 — Netlify

1. Arrastar esta pasta direto no painel da Netlify (ou conectar ao GitHub).
2. Em **Domain settings**, adicionar `peresaraujo.com.br`.
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
site-dpa/
  index.html          Home
  sobre.html           Sobre / dados formais / diferenciais
  segmentos.html        6 linhas de produto
  licitacoes.html        Como funciona, documentação, modalidades
  contato.html          Formulário + canais + mapa
  robots.txt            Libera indexação, aponta para o sitemap
  sitemap.xml            Lista as 5 páginas para os buscadores
  assets/
    css/style.css        Estilo único, responsivo (mobile/tablet/desktop)
    js/main.js            Menu mobile
    img/
      logo-full.png        Logo completa (fundo transparente) — não usada nas páginas, guardada para uso futuro (ex. materiais impressos)
      mark.png              Ícone/globo recortado da logo, usado no cabeçalho e rodapé
      favicon-*.png, favicon.ico  Ícones de aba gerados a partir da logo
```

## Atualizar conteúdo depois

Não há CMS nem editor visual — qualquer alteração de texto é feita direto no
HTML (procure o texto e edite). Isso é o principal trade-off da Opção B frente
ao Wix: mais controle e performance, porém sem editor "arrastar e soltar" para
quem não conhece código. Se isso virar um problema no dia a dia, dá pra
adicionar um CMS simples por cima depois sem refazer o site.
