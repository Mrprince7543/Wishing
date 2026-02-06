From flask import Flask, render_template_string

app = Flask(__name__)

# Killer "Dangerous" Neon Edition Script
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UNSTOPPABLE LOVE | ZOE ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-pink: #ff0055;
            --neon-blue: #00fbff;
            --bg-dark: #050505;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background-color: var(--bg-dark);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Orbitron', sans-serif;
            overflow: hidden;
            perspective: 1000px;
        }

        /* Dangerous Animated Background */
        .bg-grid {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(rgba(255, 0, 85, 0.1) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255, 0, 85, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -2;
            animation: moveGrid 20s linear infinite;
        }
        @keyframes moveGrid {
            from { transform: translateY(0); }
            to { transform: translateY(50px); }
        }

        /* Custom Neon Cursor */
        #cursor {
            position: fixed;
            width: 15px; height: 15px;
            background: var(--neon-pink);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 15px var(--neon-pink), 0 0 30px var(--neon-pink);
            transform: translate(-50%, -50%);
        }

        /* The "Dangerous" Card */
        .neon-card {
            position: relative;
            width: 90%;
            max-width: 500px;
            padding: 40px;
            background: rgba(0, 0, 0, 0.8);
            border: 2px solid var(--neon-pink);
            border-radius: 20px;
            box-shadow: 0 0 20px var(--neon-pink), inset 0 0 15px var(--neon-pink);
            text-align: center;
            transform-style: preserve-3d;
            animation: floatCard 4s ease-in-out infinite;
        }

        @keyframes floatCard {
            0%, 100% { transform: translateY(0) rotateX(2deg) rotateY(2deg); }
            50% { transform: translateY(-15px) rotateX(-2deg) rotateY(-2deg); }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #fff;
            text-shadow: 0 0 10px var(--neon-pink), 0 0 20px var(--neon-pink), 0 0 40px var(--neon-pink);
            margin-bottom: 20px;
        }

        .typing-text {
            font-size: 1.1rem;
            color: var(--neon-blue);
            text-shadow: 0 0 5px var(--neon-blue);
            min-height: 80px;
            line-height: 1.6;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        /* Dangerous Glow Buttons */
        .btn {
            background: transparent;
            color: #fff;
            border: 1px solid var(--neon-pink);
            padding: 15px 40px;
            border-radius: 5px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 3px;
            transition: 0.5s;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0 10px var(--neon-pink);
        }

        .btn:hover {
            background: var(--neon-pink);
            box-shadow: 0 0 50px var(--neon-pink);
            transform: scale(1.1);
        }

        .screen { display: none; }
        .active { display: block; animation: screenIn 0.5s ease-out; }

        @keyframes screenIn {
            from { opacity: 0; transform: rotateY(90deg); }
            to { opacity: 1; transform: rotateY(0deg); }
        }

        /* Floating Skulls or Hearts */
        .particle {
            position: absolute;
            color: var(--neon-pink);
            pointer-events: none;
            animation: fall 5s linear forwards;
            opacity: 0.8;
            filter: blur(1px);
        }
        @keyframes fall {
            to { transform: translateY(-110vh) scale(1.5); opacity: 0; }
        }

        #noBtn { transition: 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    </style>
</head>
<body>

    <div class="bg-grid"></div>
    <div id="cursor"></div>

    <audio id="bgMusic" loop>
        <source src="https://www.bensound.com/bensound-music/bensound-highoctane.mp3" type="audio/mpeg">
    </audio>

    <div class="neon-card">
        <div id="page1" class="screen active">
            <h1 style="font-size: 1.5rem; font-family: 'Orbitron'; margin-bottom: 5px; color: var(--neon-blue);">SYSTEM INITIALIZED</h1>
            <h1>Miss Zoe</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">EXECUTE LOVE ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>The Smile</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">NEXT LEVEL</button>
        </div>

        <div id="page3" class="screen">
            <h1>Lethal Beauty</h1>
            <p class="typing-text" id="type3"></p>
            <button class="btn" onclick="nextPage(4)">SCANNING HEART...</button>
        </div>

        <div id="page4" class="screen">
            <h1>Connection</h1>
            <p class="typing-text" id="type4"></p>
            <button class="btn" onclick="nextPage(5)">FINAL PHASE</button>
        </div>

        <div id="page5" class="screen">
            <h1>Be Mine?</h1>
            <p class="typing-text">Zoe, access granted to my heart. Will you be my Valentine forever?</p>
            <div style="display:flex; justify-content:center; gap:20px; position:relative;">
                <button class="btn" onclick="alert('ACCESS GRANTED! ❤️ Love you Zoe!')">YES</button>
                <button class="btn" id="noBtn" style="border-color: #555; box-shadow: none;" onmouseover="moveNoButton()">NO</button>
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
            type1: "> WARNING: HIGH ATTENTION REQUIRED. Aapke liye ek bohot hi 'dangerous' surprise taiyar hai...",
            type2: "> ANALYSIS: Aapki smile se zyada khatarnak weapon poori duniya mein nahi hai. Pure magic!",
            type3: "> DATA: Hazaaron filters aur faces dekhe, par 'Zoe' jaisa unique encryption kahin nahi mila.",
            type4: "> STATUS: Heart rate increasing... Har pal bas aapka khayal. System overloaded with love."
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
                    setTimeout(type, 30);
                }
            }
            type();
        }

        function startApp() {
            document.getElementById('bgMusic').play().catch(() => {});
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
            h.classList.add('particle');
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.bottom = "-50px";
            h.style.fontSize = Math.random() * 20 + 10 + 'px';
            h.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }
        setInterval(createHeart, 150);

        typeEffect('type1', messages.type1);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Host and Port settings
    app.run(host='0.0.0.0', port=5000)


Es script me our kya add kar sakta hu
