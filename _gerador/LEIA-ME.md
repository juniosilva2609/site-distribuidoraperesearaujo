# Gerador das artes do Instagram da DPA (11/11/2026)

Artes em HTML/CSS renderizadas com Playwright (Chromium) e ffmpeg.

- `dpa.py`: funções `tela`, `cta`, `story`, `render` (JPEG 1080x1350 / 1080x1920) e `reel` (MP4 1080x1920, 30 fps, H.264,
  AAC 48 kHz, volume em -14 LUFS).
- `lote_a.py`, `lote_b.py`, `lote_c.py`: exemplos reais (encerramento do exercício, reforma tributária, datas de dez/2026).
  Cada dado tem a fonte na própria arte. Rodar com `python3 lote_x.py` nesta pasta (criar `out/a`, `out/b`, `out/c`).
- Música dos reels: Kevin MacLeod (incompetech.com), licença Creative Commons BY 4.0: é obrigatório dar o crédito na
  legenda ("Música: “Título”, de Kevin MacLeod (incompetech.com), licença Creative Commons BY 4.0"). Baixar o MP3 em
  `https://incompetech.com/music/royalty-free/mp3-royaltyfree/<Título>.mp3` para a pasta `musica/` (não versionada).
  A API do Instagram não usa as músicas da biblioteca do aplicativo: o som precisa estar dentro do arquivo.
- Nome dos arquivos entregues ao ERP: `AAAA-MM-DD_tipo_tema[_N].ext` (tipo: post, carrossel, reel, story), na pasta
  `AAAA-MM/` deste ramo; depois `scripts/api.sh instagram-links arquivos.json` no ERP.
