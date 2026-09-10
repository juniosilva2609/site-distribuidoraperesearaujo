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

## Como publicar (custo mínimo: só o domínio)

Este site é 100% estático, então a hospedagem pode ser **gratuita**. Três opções,
todas sem custo de servidor:

1. **Cloudflare Pages** (recomendado) — conecta direto num repositório GitHub,
   deploy automático a cada alteração, e o próprio Cloudflare pode ser o registrador
   do domínio (preço de custo, sem markup).
2. **GitHub Pages** — grátis, direto do mesmo repositório GitHub.
3. **Netlify** — grátis, arrastar a pasta ou conectar ao GitHub.

Passo a passo:

1. Registrar o domínio (ex.: `distribuidoraperes.com.br` no registro.br, ou uma
   variação `.com`/`.com.br` disponível — é o único custo real desta opção).
2. Criar um repositório no GitHub e enviar esta pasta.
3. Conectar o repositório à Cloudflare Pages (ou Netlify/GitHub Pages).
4. Apontar o DNS do domínio para a plataforma escolhida (instruções ficam
   disponíveis na própria plataforma ao cadastrar o domínio).

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
