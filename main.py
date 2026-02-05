from flask import Flask, render_template_string

app = Flask(__name__)

# Ultimate Dangerous Neon Edition with "Raataan Lambiyan" Song
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TERMINAL: ZOE ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-pink: #ff0055;
            --neon-blue: #00fbff;
            --main-bg: #030303;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background-color: var(--main-bg);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Orbitron', sans-serif;
            overflow: hidden;
        }

        /* Dangerous Matrix/Grid Background */
        .bg-layer {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, rgba(255, 0, 85, 0.05) 0%, transparent 80%);
            z-index: -1;
        }

        /* Custom Laser Cursor */
        #cursor {
            position: fixed;
            width: 10px; height: 10px;
            background: #fff;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 10px #fff, 0 0 20px var(--neon-pink), 0 0 40px var(--neon-pink);
            transform: translate(-50%, -50%);
        }

        /* Neon Frame */
        .neon-frame {
            position: relative;
            width: 90%;
            max-width: 500px;
            padding: 40px;
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid var(--neon-pink);
            border-radius: 10px;
            box-shadow: 0 0 30px var(--neon-pink), inset 0 0 20px var(--neon-pink);
            text-align: center;
            overflow: hidden;
        }

        /* Pulsing Glow Border Animation */
        .neon-frame::before {
            content: '';
            position: absolute;
            top: -2px; left: -2px; right: -2px; bottom: -2px;
            border: 2px solid var(--neon-blue);
            border-radius: 10px;
            animation: pulseBorder 2s linear infinite;
            z-index: -1;
        }

        @keyframes pulseBorder {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0; }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #fff;
            text-shadow: 0 0 10px var(--neon-pink), 0 0 20px var(--neon-pink);
            margin-bottom: 20px;
        }

        .typing-text {
            font-size: 1rem;
            color: var(--neon-blue);
            min-height: 80px;
            line-height: 1.5;
            margin-bottom: 25px;
            text-shadow: 0 0 5px var(--neon-blue);
        }

        .btn {
            background: transparent;
            color: #fff;
            border: 2px solid var(--neon-pink);
            padding: 15px 30px;
            border-radius: 0;
            text-transform: uppercase;
            letter-spacing: 5px;
            font-weight: 900;
            transition: 0.4s;
            box-shadow: 0 0 10px var(--neon-pink);
        }

        .btn:hover {
            background: var(--neon-pink);
            box-shadow: 0 0 40px var(--neon-pink);
            color: #000;
            transform: skewX(-10deg);
        }

        .screen { display: none; }
        .active { display: block; animation: glitchedIn 0.3s ease-out; }

        @keyframes glitchedIn {
            0% { opacity: 0; transform: translateX(-20px); filter: blur(10px); }
            100% { opacity: 1; transform: translateX(0); filter: blur(0); }
        }

        /* Floating Cyber Hearts */
        .heart {
            position: absolute;
            color: var(--neon-pink);
            pointer-events: none;
            z-index: -1;
            animation: moveUp 4s linear infinite;
        }
        @keyframes moveUp {
            from { transform: translateY(100vh); opacity: 1; }
            to { transform: translateY(-10vh); opacity: 0; }
        }
    </style>
</head>
<body>

    <div class="bg-layer"></div>
    <div id="cursor"></div>

    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>

    <div class="neon-frame">
        <div id="page1" class="screen active">
            <h1 style="font-family:'Orbitron'; font-size: 1.2rem; color: var(--neon-blue); letter-spacing: 5px;">SYSTEM SECURE</h1>
            <h1>Miss Zoe</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">INITIATE LOVE</button>
        </div>

        <div id="page2" class="screen">
            <h1>The Smile</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">NEXT LEVEL</button>
        </div>

        <div id="page3" class="screen">
            <h1>Uniqueness</h1>
            <p class="typing-text" id="type3"></p>
            <button class="btn" onclick="nextPage(4)">DECODING...</button>
        </div>

        <div id="page4" class="screen">
            <h1>True Feelings</h1>
            <p class="typing-text" id="type4"></p>
            <button class="btn" onclick="nextPage(5)">FINAL STAGE</button>
        </div>

        <div id="page5" class="screen">
            <h1>Be Mine?</h1>
            <p class="typing-text" style="color:#fff;">Zoe, you are the most dangerous distraction for my heart. Will you be my Valentine?</p>
            <div style="display:flex; justify-content:center; gap:20px; position:relative;">
                <button class="btn" onclick="alert('CONNECTED! ❤️ Love you Zoe!')">YES</button>
                <button class="btn" id="noBtn" style="border-color: #444; box-shadow: none;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "> ACCESSING FILES... Aapke liye ek khatarnak surprise hai, Miss Zoe. Ready?",
            type2: "> STATUS: Aapki smile se zyada deadly weapon poori duniya mein nahi hai. Pure magic!",
            type3: "> SCANNING... Hazaaron faces dekhe, par 'Zoe' jaisa unique encryption kahin nahi mila.",
            type4: "> WARNING: Heart rate at maximum. Har dua mein bas aapka hi naam hai. System Overload!"
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            if(!el) return;
            el.innerHTML = "";
            function type() {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, 35);
                }
            }
            type();
        }

        function startApp() {
            const music = document.getElementById('bgMusic');
            music.play().catch(e => console.log("Music click interaction required"));
            nextPage(2);
        }

        function nextPage(num) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById('page' + num).classList.add('active');
            if(messages['type'+num]) {
                typeEffect('type'+num, messages['type'+num]);
            }
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        function createHeart() {
            const h = document.createElement('div');
            h.classList.add('heart');
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 15 + 10 + 'px';
            h.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
        }
        setInterval(createHeart, 200);

        typeEffect('type1', messages.type1);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
