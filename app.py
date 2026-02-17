from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday</title>

<style>
body{
margin:0;
padding:0;
overflow:hidden;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background: radial-gradient(circle at top,#ff4e8b,#1a1a40);
font-family:-apple-system,BlinkMacSystemFont,sans-serif;
color:white;
text-align:center;
}

/* 20 */
.number{
position:absolute;
top:7%;
left:50%;
transform:translateX(-50%);
font-size:65px;
font-weight:bold;
text-shadow:0 0 25px rgba(255,255,255,0.8);
display:flex;
gap:12px;
align-items:center;
}

/* SİMLER */
.sparkle{
position:absolute;
width:4px;
height:4px;
background:white;
border-radius:50%;
animation: twinkle 2s infinite ease-in-out;
}

@keyframes twinkle{
0%{opacity:0;}
50%{opacity:1;}
100%{opacity:0;}
}

/* PASTA */
.cake{
position:relative;
width:180px;
height:140px;
margin:auto;
cursor:pointer;
}

.layer1{
position:absolute;
bottom:0;
width:180px;
height:60px;
background:#f8c8dc;
border-radius:20px;
}

.layer2{
position:absolute;
bottom:55px;
left:20px;
width:140px;
height:50px;
background:#ffe5b4;
border-radius:20px;
}

.icing{
position:absolute;
bottom:100px;
left:30px;
width:120px;
height:30px;
background:#ff6f91;
border-radius:20px;
}

.candle{
position:absolute;
bottom:125px;
left:85px;
width:10px;
height:40px;
background:white;
}

.flame{
position:absolute;
bottom:165px;
left:80px;
width:20px;
height:25px;
background:gold;
border-radius:50%;
animation:flicker 0.5s infinite alternate;
}

@keyframes flicker{
from{opacity:0.6; transform:scale(1);}
to{opacity:1; transform:scale(1.15);}
}

/* BALON */
.balloon{
position:absolute;
bottom:-120px;
width:40px;
height:50px;
border-radius:50%;
animation: floatUp linear infinite;
}

@keyframes floatUp{
from{transform:translateY(0);}
to{transform:translateY(-120vh);}
}

/* BUTON */
.circle-btn{
position:absolute;
bottom:8%;
left:50%;
transform:translateX(-50%);
width:70px;
height:70px;
background:#0a1f44;
border-radius:50%;
display:flex;
justify-content:center;
align-items:center;
font-size:28px;
cursor:pointer;
box-shadow:0 0 15px rgba(0,0,0,0.4);
transition:0.2s;
}

.circle-btn:active{
transform:translateX(-50%) scale(0.9);
}
</style>
</head>

<body>

<!-- MÜZİK -->
<audio id="bgMusic" autoplay loop>
<source src="/static/music.mp3" type="audio/mpeg">
</audio>

<div class="number">
<span>✨</span>
<span>20</span>
<span>✨</span>
</div>

<div class="cake" onclick="blowCandle()">
<div class="layer1"></div>
<div class="layer2"></div>
<div class="icing"></div>
<div class="candle"></div>
<div class="flame" id="flame"></div>
</div>

<div class="circle-btn" onclick="surprise()">👉</div>

<script>

/* MESAJI BURADAN DEĞİŞTİR */
function surprise(){
alert("BURAYA KENDİ MESAJINI YAZ");
}

/* iPhone autoplay fallback */
document.addEventListener("click", function(){
document.getElementById("bgMusic").play();
}, {once:true});

/* MUM SÖNME + HAVAİ FİŞEK */
function blowCandle(){
let flame=document.getElementById("flame");
flame.style.display="none";
launchFireworks();
}

/* BALON RENKLERİ */
const colors=["silver","gold","#b30000","#0a1f44"];

for(let i=0;i<40;i++){
let b=document.createElement("div");
b.className="balloon";
b.style.left=Math.random()*100+"vw";
b.style.background=colors[Math.floor(Math.random()*colors.length)];
b.style.animationDuration=(6+Math.random()*4)+"s";
document.body.appendChild(b);
}

/* SİMLER */
for(let i=0;i<80;i++){
let s=document.createElement("div");
s.className="sparkle";
s.style.left=Math.random()*100+"vw";
s.style.top=Math.random()*100+"vh";
s.style.animationDelay=Math.random()*2+"s";
document.body.appendChild(s);
}

/* HAVAİ FİŞEK */
function launchFireworks(){
for(let i=0;i<60;i++){
let fw=document.createElement("div");
fw.style.position="absolute";
fw.style.width="6px";
fw.style.height="6px";
fw.style.borderRadius="50%";
fw.style.background="hsl("+Math.random()*360+",100%,50%)";
fw.style.left="50%";
fw.style.top="50%";
fw.style.transition="all 1s ease-out";
document.body.appendChild(fw);

setTimeout(()=>{
fw.style.left=(50+Math.random()*50-25)+"%";
fw.style.top=(50+Math.random()*50-25)+"%";
fw.style.opacity="0";
},10);

setTimeout(()=>{
fw.remove();
},1000);
}
}
</script>

</body>
</html>
"""

import os

if __name__ == "__main__":
    app.run()
    


