from flask import Flask, render_template_string

app = Flask(__name__)

# Super Smooth & Performance Optimized Version
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zoe Verma Special ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #ff758f;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 15px;
            will-change: background;
        }

        /* Optimized Floating Hearts */
        .heart-float {
            position: absolute;
            color: #ff4d6d;
            pointer-events: none;
            animation: moveUp 5s linear forwards;
            will-change: transform, opacity;
            z-index: 1;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
            10% { opacity: 0.8; }
            100% { transform: translateY(-15vh) scale(1.2); opacity: 0; }
        }

        /* Top Title - Smooth Glow */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 1.8rem;
            color: #fff;
            text-align: center;
            margin-bottom: 15px;
            text-shadow: 0 0 10px rgba(255, 0, 85, 0.5);
            z-index: 10;
        }

        /* Header Box - GPU Friendly Pulse */
        .header-box {
            background: #ff4d6d;
            border: 2px solid #fff;
            padding: 12px 25px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(255, 77, 109, 0.4);
            animation: softPulse 3s infinite ease-in-out;
            z-index: 10;
        }
        @keyframes softPulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.03); }
        }

        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.2rem;
            color: #fff;
            letter-spacing: 2px;
        }

        /* Main Container - Balanced Sizing */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            min-height: 350px;
            padding: 30px 20px;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 25px;
            border: 2px solid #ffb3c1;
            text-align: center;
            z-index: 5;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #ff4d6d;
            margin-bottom: 10px;
        }

        .typing-text {
            font-size: 1.1rem;
            color: #444;
            min-height: 60px;
            margin-bottom: 25px;
            line-height: 1.4;
        }

        /* Footer Box */
        .footer-box {
            margin-top: 15px;
            background: #fff;
            border: 1px dashed #ff4d6d;
            padding: 10px 20px;
            border-radius: 40px;
            box-shadow: 0 4px 10px rgba(255, 77, 109, 0.2);
            z-index: 10;
        }
        .footer-box p {
            font-weight: 600;
            color: #ff4d6d;
            font-size: 0.95rem;
        }

        /* Button Styling */
        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            transition: 0.2s ease;
            box-shadow: 0 4px 12px rgba(255, 77, 109, 0.3);
        }
        .btn:active { transform: scale(0.95); }

        /* Custom Cursor - High Performance */
        #cursor {
            position: fixed;
            width: 18px; height: 18px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        .screen { display: none; }
        .active { display: block; animation: smoothFade 0.4s ease-out; }
        @keyframes smoothFade { from { opacity: 0; } to { opacity: 1; } }

    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop preload="auto">
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">HAPPY VALENTINE'S DAY MIZZ ZOE VERMA 😘</div>

    <div class="header-box">
        <h2>REHAN LOVES ZOE</h2>
    </div>

    <div class="love-card">
        <div id="page1" class="screen active">
            <h1>Hi Jaan ❤️</h1>
            <p class="typing-text" id="type1">Click niche karo ek surprise hai...</p>
            <button class="btn" onclick="startApp()">UNLOCK LOVE ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>Zoe Verma...</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
        </div>

        <div id="page3" class="screen">
            <h1>Be Mine?</h1>
            <p class="typing-text">Zoe, meri har khushi aap se shuru hoti hai. Kya hamesha mere saath rahoge? ❤️</p>
            <div style="display:flex; justify-content:center; gap:12px; position:relative;">
                <button class="btn" onclick="alert('I Love You Too, Zoe Jaan! 😘😘😘')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background:#888;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <div class="footer-box">
        <p>I LOVE YOU MERI JAAN ZOE VERMA 😘😘😘</p>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        const bgMusic = document.getElementById('bgMusic');

        // Throttle Mousemove for Performance
        let lastMove = 0;
        document.addEventListener('mousemove', (e) => {
            const now = Date.now();
            if (now - lastMove > 10) {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
                lastMove = now;
            }
        });

        const messages = {
            type1: "Aapke liye kuch bohot khaas banaya hai... Ready ho?",
            type2: "Aapki smile meri duniya hai, aur aap meri zindagi ka sabse haseen hissa ho."
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            el.innerHTML = "";
            const interval = setInterval(() => {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                } else {
                    clearInterval(interval);
                }
            }, 40);
        }

        function startApp() {
            bgMusic.play().catch(() => console.log("Music blocked"));
            nextPage(2);
        }

        function nextPage(num) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById('page' + num).classList.add('active');
            if(messages['type'+num]) typeEffect('type'+num, messages['type'+num]);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = (Math.random() * (window.innerWidth - 80)) + 'px';
            btn.style.top = (Math.random() * (window.innerHeight - 40)) + 'px';
        }

        // Optimized Particle Creation
        function createHeart() {
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 15 + 10) + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }
        setInterval(createHeart, 400); // Thoda gap rakha hai taaki hang na ho

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
