# Rotina semanal de Novidades (toda segunda, ~09h de Brasília)

Instruções seguidas pela tarefa agendada. Também servem para quem for publicar à mão.

## 1. Pesquisar
- Encontre **pelo menos 1** notícia **oficial** publicada nos últimos 7 dias (de preferência; no máximo 14).
- **Fontes permitidas (só estas):** planalto.gov.br, gov.br (inclusive /pncp, /compras, /receitafederal,
  /fazenda, /tesouronacional), portal.tcu.gov.br, tce.mg.gov.br, almg.gov.br, mg.gov.br,
  fazenda.mg.gov.br, planejamento.mg.gov.br, camara.leg.br, senado.leg.br, in.gov.br (DOU) e
  jornal Minas Gerais (iof.mg.gov.br).
- **Temas:** licitações e contratos (Lei 14.133/2021, PNCP, decretos, INs, acórdãos do TCU e do TCE-MG);
  reforma tributária (EC 132/2023, LC 214/2025, CBS/IBS, transição, Comitê Gestor do IBS); compras públicas,
  encerramento do exercício financeiro, notas fiscais.
- **Nunca:** nada político, partidário, polêmico ou crítico a órgãos. Nunca inventar nada.
- Antes de usar, **abra a página oficial** e confira: data de publicação, número do ato (se houver) e se o link abre.
- Não repita notícia que já está em `novidades/novidades.json` (compare `url` e assunto).

**Sem notícia oficial relevante na semana:** publique um "Você sabia?" sobre **um artigo da Lei 14.133/2021**,
categoria `Licitações`, com `url` = `https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm`
(confira que abre) e `tag` = `Art. N da Lei 14.133/2021`. Não repita artigo já usado.

**Nunca publique sem link oficial conferido.**

## 2. Acrescentar o registro
Acrescente um objeto no início de `novidades/novidades.json`:

```json
{
  "id": "slug-curto-sem-acentos",
  "data": "AAAA-MM-DD",
  "categoria": "Licitações | Reforma Tributária | DPA",
  "titulo": "Título curto e neutro",
  "resumo": "De 2 a 4 frases, em linguagem simples.",
  "fonte": "Nome do órgão",
  "url": "https://… (fonte oficial)",
  "tag": "opcional, ex.: Decreto 12.345/2026"
}
```
`data` = data de publicação **na fonte oficial**.

## 3. Validar e gerar
```bash
python3 build.py --check   # valida campos, categoria, domínio oficial e 2 a 4 frases
python3 build.py           # gera as páginas, o feed RSS, o sitemap e a "Última atualização"
```

## 4. Publicar
O site é publicado pelo GitHub Pages a partir da branch `master`:
```bash
git add -A && git commit -m "Novidades: <título>" && git push origin HEAD:master
```

## 5. Conferir no ar (1 a 3 minutos depois)
- `https://distribuidoraperesearaujo.com.br/novidades/` deve mostrar o novo título.
- `https://distribuidoraperesearaujo.com.br/novidades/feed.xml` deve conter o novo item.

## 6. Avisar
Criar um rascunho de e-mail no Gmail para **junioaraujo.adv@gmail.com**:
- Assunto: `Novidades DPA: <título>`
- Corpo: título, link no site (`https://distribuidoraperesearaujo.com.br/novidades/#<id>`) e link da fonte oficial.

## Automático (não precisa de ninguém)
- `.github/workflows/atualizar-site.yml` regera o site todo dia às 00:07 (Brasília):
  atualiza a contagem de anos, publica posts com data agendada e faz a troca do período de 12 anos
  (08/01/2027 a 31/01/2027) e a volta ao padrão em 01/02/2027.
