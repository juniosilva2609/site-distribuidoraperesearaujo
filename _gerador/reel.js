// node reel.js spec.json -> {out,dur,html,css,audio,inicio}
const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const s=JSON.parse(fs.readFileSync(process.argv[2]));const FPS=30,W=1080,H=1920;
const f=__dirname+'/_reel.html';
fs.writeFileSync(f,`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><link rel="stylesheet" href="reel.css"><style>body{--total:${s.dur}s}${s.css||''}</style></head><body>${s.html}</body></html>`);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:W,height:H},deviceScaleFactor:1});
await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const fade=Math.max(0,s.dur-1.2);
const args=['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-'];
if(s.audio)args.push('-ss',String(s.inicio||0),'-i',s.audio);else args.push('-f','lavfi','-i','anullsrc=r=48000:cl=stereo');
args.push('-map','0:v','-map','1:a','-t',String(s.dur),'-c:v','libx264','-preset','slow','-crf','15','-profile:v','high','-pix_fmt','yuv420p','-r',String(FPS),'-g','60','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',
 '-af',`loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=in:d=0.3,afade=t=out:st=${fade}:d=1.2`,'-c:a','aac','-b:a','128k','-ar','48000','-ac','2','-movflags','+faststart',s.out);
const ff=spawn('ffmpeg',args,{stdio:['pipe','inherit','inherit']});
const n=Math.round(s.dur*FPS);
for(let k=0;k<n;k++){await p.evaluate(t=>{document.getAnimations().forEach(a=>{a.pause();a.currentTime=t})},k*1000/FPS);
 const buf=await p.screenshot({type:'jpeg',quality:96});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();fs.unlinkSync(f);console.log('ok',s.out,n/FPS+'s');})();
