from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - THE FINAL STABLE & SMOOTH MASTERPIECE
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Surprise for Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        /* Smooth Rendering & Hardware Acceleration */
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        
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
            padding: 10px;
            will-change: background;
        }

        /* Top Title - Direct Glow Style */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.3rem;
            color: #fff;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0 0 12px #ff0055, 0 0 25px #ff0055;
            z-index: 20;
        }

        /* Rehan Loves Zoe - Fixed Header */
        .header-box {
            background: rgba(255, 77, 109, 0.95);
            border: 2px solid #fff;
            padding: 8px 30px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            z-index: 20;
            text-align: center;
        }
        .header-box h2 {
            font-size: 1.4rem;
            color: #fff;
            letter-spacing: 2.5px;
            text-transform: uppercase;
        }

        /* MAIN CONTAINER - CUSTOM ZOE BACKGROUND */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 380px;
            border-radius: 25px;
            z-index: 5;
            border: 3.5px solid #fff;
            box-shadow: 0 15px 45px rgba(0,0,0,0.3);
            background: url('https://i.ibb.co/rGT6qF7r/Picture-Unlock-TOI-521963-user0-pictureunlock.webp') center/cover no-repeat;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            will-change: transform;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(1px);
            z-index: 1;
        }

        .content-inner {
            position: relative;
            z-index: 2;
            width: 92%;
            text-align: center;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.8rem;
            color: #ffffff;
            margin-bottom: 8px;
            text-shadow: 2px 2px 15px #ff0055;
        }

        .typing-text {
            font-size: 1.4rem;
            color: #fff;
            font-weight: 700;
            min-height: 75px;
            text-shadow: 1px 1px 10px #000;
            line-height: 1.3;
        }

        /* FOOTER BOX - ATTRACTIVE & PERFECTLY CENTERED */
        .footer-box {
            margin-top: 25px;
            background: linear-gradient(90deg, #ff4d6d, #ff758f, #ff4d6d);
            background-size: 200% auto;
            padding: 15px 35px;
            border-radius: 50px;
            border: 2px solid #fff;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.8);
            z-index: 20;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-width: 300px;
            animation: gradientMove 4s linear infinite;
        }

        @keyframes gradientMove {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        .footer-box p {
            font-weight: 800;
            color: #fff;
            font-size: 1rem;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            width: 100%;
        }

        /* Buttons */
        .btn {
            background: #ff4d6d;
            color: white;
            border: 2px solid #fff;
            padding: 12px 35px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: 0.2s ease;
        }
        .btn:active { transform: scale(0.95); }

        /* Cursor */
        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #fff;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            filter: drop-shadow(0 0 6px #ff4d6d);
        }

        /* Floating Particles (Performance Optimized) */
        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 5s linear forwards;
            z-index: 1;
            will-change: transform;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh); opacity: 0; }
            10% { opacity: 0.9; }
            100% { transform: translateY(-10vh); opacity: 0; }
        }

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeIn 0.4s ease-out; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    
    <audio id="bgMusic" loop preload="auto">
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">Happy Valentine's Day Zoe 😘</div>

    <div class="header-box">
        <h2>REHAN LOVES ZOE</h2>
    </div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Jaan ❤️</h1>
                <p class="typing-text" id="type1">Click niche karo ek surprise hai...</p>
                <button class="btn" onclick="startApp()">START SURPRISE ✨</button>
            </div>

            <div id="page2" class="screen">
                <h1 style="font-size: 3rem;">Beautiful</h1>
                <p class="typing-text" id="type2"></p>
                <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
            </div>

            <div id="page3" class="screen">
                <h1 style="font-size: 2.8rem;">Be Mine?</h1>
                <p class="typing-text">Zoe, kya hamesha mere saath rahoge? Will you be my Valentine forever? ❤️</p>
                <div style="display:flex; justify-content:center; gap:12px; position:relative;">
                    <button class="btn" onclick="alert('I Love You Too, Zoe Jaan! 😘😘😘')">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444; border:none;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-box">
        <p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');

        // Throttled mouse tracking for smoothness
        let moveTimer;
        document.addEventListener('mousemove', (e) => {
            if (!moveTimer) {
                moveTimer = setTimeout(() => {
                    cursor.style.left = e.clientX + 'px';
                    cursor.style.top = e.clientY + 'px';
                    moveTimer = null;
                }, 10);
            }
        });

        const messages = {
            type1: "Aapke liye ek chota sa digital tohfa... Ready ho?",
            type2: "Aapki smile meri poori duniya hai, aur aap meri zindagi ka sabse pyara hissa ho."
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            el.innerHTML = "";
            function type() {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, 45);
                }
            }
            type();
        }

        function startApp() {
            // Unmute and Play Audio
            music.play().catch(() => {
                // Fallback for strict browsers
                music.muted = true;
                music.play();
                music.muted = false;
            });
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
            btn.style.left = (Math.random() * (window.innerWidth - 100)) + 'px';
            btn.style.top = (Math.random() * (window.innerHeight - 80)) + 'px';
        }

        // Lightweight Particle System
        function createHeart() {
            if (document.querySelectorAll('.heart-float').length > 10) return;
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 12 + 10) + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }
        setInterval(createHeart, 800);

        typeEffect('type1', messages.type1);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Host on 0.0.0.0 and Port 5000 as per request
    app.run(host='0.0.0.0', port=5000)
