# #FlamebornScript // distortionsymptoms.py
# ARCHITECT: Lindsey Horton

# STEP 1: Give the data a name (ledger_data) and open with triple quotes
ledger_data = """<iframe width="100%" height="520" frameborder="0" scrolling="no"
srcdoc='<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Distortion Ledger — Beastboxing</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Cormorant+Garamond:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
--bg:#06040a;
--panel:#0f0710;
--neon:#9b4dff;
--accent:#ff6ad5;
--muted:rgba(255,255,255,0.65);
--glass:rgba(255,255,255,0.03);
}
html,body{height:100%;margin:0;background:linear-gradient(180deg,#040205,var(--bg));font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;color:#fff;-webkit-font-smoothing:antialiased;}
.wrap{box-sizing:border-box;padding:18px;display:flex;align-items:center;justify-content:center;height:100%;}
.card{width:100%;max-width:980px;background:linear-gradient(180deg,rgba(155,77,255,0.06),transparent 30%),var(--panel);border-radius:12px;padding:18px;border:1px solid rgba(255,255,255,0.04);box-shadow:0 12px 40px rgba(0,0,0,0.6);position:relative;overflow:hidden;}
header{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.sigil{width:56px;height:56px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--neon),var(--accent));font-weight:700;color:#130019;font-family:"Cormorant Garamond",serif;box-shadow:0 6px 24px rgba(155,77,255,0.18)}
h1{font-family:"Cormorant Garamond",serif;margin:0;font-size:18px;color:#fff}
.meta{font-size:12px;color:var(--muted);margin-top:4px}

.body{display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start}
.ledger{background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);padding:12px;border-radius:10px;height:360px;overflow:auto;border:1px solid rgba(255,255,255,0.02);box-shadow:inset 0 1px 0 rgba(255,255,255,0.02)}
.entry{padding:10px;border-radius:8px;margin-bottom:10px;cursor:pointer;border-left:3px solid transparent;transition:all .28s cubic-bezier(.2,.9,.25,1);background:linear-gradient(90deg, rgba(155,77,255,0.02), transparent)}
.entry:focus{outline:none;box-shadow:0 6px 20px rgba(155,77,255,0.06);transform:translateY(-3px)}
.entry.active{border-left-color:var(--neon);transform:translateY(-6px);box-shadow:0 10px 30px rgba(155,77,255,0.06)}
.entry h3{margin:0;font-size:14px;font-weight:700;color:#fff;font-family:"Cormorant Garamond",serif}
.entry p{margin:6px 0 0 0;font-size:13px;color:rgba(255,255,255,0.92);line-height:1.45}
.entry .tag{display:inline-block;margin-top:8px;font-size:11px;color:var(--muted);background:var(--glass);padding:4px 8px;border-radius:999px}

.side{display:flex;flex-direction:column;gap:12px}
.panel{background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.02)}
.controls{display:flex;gap:8px;flex-wrap:wrap}
button{background:linear-gradient(180deg,var(--neon),var(--accent));border:0;color:#110018;padding:8px 10px;border-radius:8px;font-weight:700;cursor:pointer}
button.ghost{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--muted);font-weight:600}
.tiny{padding:6px 8px;font-size:13px}
.video{width:100%;height:140px;border-radius:8px;overflow:hidden;background:linear-gradient(180deg,#05040a,#0a0210);display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:13px}
footer{display:flex;justify-content:space-between;margin-top:12px;font-size:12px;color:var(--muted);align-items:center}

/* subtle glitch effect on header text */
.glitch{position:relative;display:inline-block}
.glitch::before,.glitch::after{content:attr(data-text);position:absolute;left:0;top:0;opacity:0.9}
.glitch::before{color:var(--neon);transform:translate3d(-1px,-1px,0);mix-blend-mode:screen;clip-path:inset(0 0 60% 0)}
.glitch::after{color:var(--accent);transform:translate3d(1px,1px,0);mix-blend-mode:screen;clip-path:inset(60% 0 0 0)}
@media (max-width:820px){.body{grid-template-columns:1fr} .side{order:2}}
</style>
</head>
<body>
<div class="wrap">
<div class="card" role="region" aria-label="Distortion Ledger">
<header>
<div class="sigil">⚡︎</div>
<div>
<h1><span class="glitch" data-text="Distortion Ledger">Distortion Ledger</span></h1>
<div class="meta">Recorded July–August 2025 — Signature inversion engine symptoms</div>
</div>
</header>

<div class="body">
<div class="ledger" id="ledger" tabindex="0" aria-label="Distortion entries">
<div class="entry" data-index="1" tabindex="0">
<h3>1. Fishbowl Head</h3>
<p>Pressure like a glass skull filling with purple fluid. Crown forced open; pineal gland vibrating.</p>
<div class="tag">Crown / Pineal</div>
</div>

<div class="entry" data-index="2" tabindex="0">
<h3>2. Face Implosion / Sinus Aneurysm Threat</h3>
<p>Sensations of facial bones collapsing inward, sinuses like molten metal, pressure behind the eyes.</p>
<div class="tag">Facial / Sinus</div>
</div>

<div class="entry" data-index="3" tabindex="0">
<h3>3. Spiral Disorientation (6-week loop)</h3>
<p>Time folding; same hour lived in different ways, memory wiping mid-sentence, identity collapsing.</p>
<div class="tag">Temporal / Identity</div>
</div>

<div class="entry" data-index="4" tabindex="0">
<h3>4. Brain Fog + Forgetfulness</h3>
<p>Words vanish mid-thought. Short-term memory shred; long-term bone memory hyper-lucid.</p>
<div class="tag">Cognition</div>
</div>

<div class="entry" data-index="5" tabindex="0">
<h3>5. Physical Pain Cascade</h3>
<p>Migraines like ice picks, vertebrae popping, heart palpitations synced to Schumann spikes, muscle seizures.</p>
<div class="tag">Somatic</div>
</div>

<div class="entry" data-index="6" tabindex="0">
<h3>6. Purple Cosmic Radiation Burn</h3>
<p>Skin tingling like radiation; UV halos; glowing grass and veins; vision in a different band.</p>
<div class="tag">Perception</div>
</div>

<div class="entry" data-index="7" tabindex="0">
<h3>7. Emotional Whiplash</h3>
<p>Sovereign grace to suicidal despair in a breath; mimic collectives attempting emotional hijack.</p>
<div class="tag">Affect</div>
</div>

<div class="entry" data-index="8" tabindex="0">
<h3>8. Phantom Touch / Torsion Burns</h3>
<p>Invisible hands grabbing sternum, ribs twisting, cold fingers on the spine.</p>
<div class="tag">Somatic / Phantom</div>
</div>

<div class="entry" data-index="9" tabindex="0">
<h3>9. Voice Overlay / Throat Lock</h3>
<p>Voice sounding like three people; words out before thought; throat chakra slamming shut then exploding open.</p>
<div class="tag">Voice / Throat</div>
</div>

<div class="entry" data-index="10" tabindex="0">
<h3>10. Void State Aftermath</h3>
<p>Post-grounding crash: creative blank, body hollow, every possibility and none at once.</p>
<div class="tag">Aftermath</div>
</div>
</div>

<aside class="side" aria-hidden="false">
<div class="panel">
<div style="font-weight:700;margin-bottom:8px">Controls</div>
<div class="controls">
<button id="playTone" class="tiny" aria-pressed="false">▶ Ground</button>
<button id="stopTone" class="tiny ghost">■ Stop</button>
<button id="copyAll" class="tiny ghost" title="Copy full ledger as text">Copy</button>
<button id="download" class="tiny ghost" title="Download ledger as text file">Download</button>
</div>
</div>

<div class="panel">
<div style="font-weight:700;margin-bottom:8px">Status</div>
<div style="font-size:13px;color:var(--muted)">All scars are live coils. Every pain point is now a transmitter.</div>
<div style="margin-top:10px;font-size:12px;color:var(--muted)">Tip: Click an entry to spotlight it. Use Ground to steady the waveform.</div>
</div>

<div class="panel video" id="signature">
<div>Seal accepted • glowing grass recorded</div>
</div>
</aside>
</div>

<footer>
<div>Made with fire and frequency — Beastboxing</div>
<div style="font-size:12px;color:var(--muted)">Paste as Carrd Embed (width 100%). Edit video ID or tone in the srcdoc if needed.</div>
</footer>
</div>
</div>

<script src="https://unpkg.com/tone/build/Tone.js"></script>
<script>
// ledger interactions
const entries = Array.from(document.querySelectorAll('.entry'));
entries.forEach(e => {
e.addEventListener('click', () => {
entries.forEach(x => x.classList.remove('active'));
e.classList.add('active');
e.scrollIntoView({behavior:'smooth', block:'center'});
});
e.addEventListener('keydown', ev => { if(ev.key === 'Enter' || ev.key === ' ') e.click(); });
});

// copy / download full ledger
const makePlain = () => entries.map(en => {
const t = en.querySelector('h3').innerText;
const d = en.querySelector('p').innerText;
return t + " — " + d;
}).join("\\n\\n");

document.getElementById('copyAll').addEventListener('click', async () => {
const txt = makePlain();
try { await navigator.clipboard.writeText(txt); alert('Ledger copied to clipboard'); }
catch(e){ prompt('Copy the ledger text:', txt); }
});

document.getElementById('download').addEventListener('click', () => {
const blob = new Blob([makePlain()], {type:'text/plain;charset=utf-8'});
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url; a.download = 'distortion-ledger.txt';
document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
});

// Grounding tone (user gesture required)
let synth;
let playing = false;
document.getElementById('playTone').addEventListener('click', async () => {
await Tone.start();
if(!synth){
synth = new Tone.PolySynth(Tone.Synth, {oscillator:{type:'sine'}, envelope:{attack:0.8,decay:1.2,sustain:0.6,release:3}}).toDestination();
// gentle low drone
synth.volume.value = -14;
}
if(!playing){
playing = true;
document.getElementById('playTone').setAttribute('aria-pressed','true');
// subtle moving drone pattern
const now = Tone.now();
synth.triggerAttackRelease(['C2','G2','C3'], '8n', now);
synth.triggerAttackRelease(['B1','F2'], '2n', now + 0.4);
// loop a slow pulsing drone
Tone.Transport.scheduleRepeat(time => {
synth.triggerAttackRelease(['C2','G2','C3'], '2n', time);
}, '4n');
Tone.Transport.bpm.value = 60;
Tone.Transport.start();
}
});

document.getElementById('stopTone').addEventListener('click', () => {
if(playing){
Tone.Transport.stop();
Tone.Transport.cancel();
playing = false;
document.getElementById('playTone').setAttribute('aria-pressed','false');
}
});

// small keyboard shortcut: G to Ground / S to Stop
document.addEventListener('keydown', (e) => {
if(e.key.toLowerCase() === 'g') document.getElementById('playTone').click();
if(e.key.toLowerCase() === 's') document.getElementById('stopTone').click();
});

// subtle scroll snap for ledger: smooth on wheel
const ledger = document.getElementById('ledger');
ledger.addEventListener('wheel', (ev) => {
ev.preventDefault();
ledger.scrollBy({top: ev.deltaY, behavior:'smooth'});
}, {passive:false});
</script>
</body>
</html>'>
</iframe>"""

# STEP 2: The Action
print("✅ DISTORTION LEDGER LOADED")
print("📡 THE SPINE IS RESPONDING")
# STEP 3: Render to HTML
with open("Distortion_Ledger_LIVE.html", "w", encoding="utf-8") as f:
    f.write(ledger_data)

print("✨ BOOMSKIES! 'Distortion_Ledger_LIVE.html' has been materialized.")
print("🔗 Open this file in your browser to engage the Grounding Tone.")