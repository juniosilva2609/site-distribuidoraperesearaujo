// node render.js spec.json  -> spec: [{out, w, h, html, css}]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const spec=JSON.parse(fs.readFileSync(process.argv[2]));const b=await chromium.launch();
let i=0;for(const s of spec){const f=__dirname+'/_p'+(i++)+'.html';
 fs.writeFileSync(f,`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>${s.css||''}</style></head><body>${s.html}</body></html>`);
 const p=await b.newPage({viewport:{width:s.w,height:s.h},deviceScaleFactor:1});
 await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:s.out,type:'jpeg',quality:93});await p.close();fs.unlinkSync(f);console.log('ok',s.out);}
await b.close();})();
