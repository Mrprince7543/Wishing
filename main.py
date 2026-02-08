from flask import Flask, render_template_string

app = Flask(__name__)

# Ultra-Smooth & Fixed Audio Edition
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zoe Verma Special ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        /* Smooth Rendering & Performance */
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
        }

        /* Titles - Properly Adjusted */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.2rem;
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
            text-shadow: 0 0 10px #ff0055;
            z-index: 10;
        }

        .header-box {
            background: rgba(255, 77, 109, 0.9);
            border: 2px solid #fff;
            padding: 8px 25px;
            border-radius: 10px;
            margin-bottom: 12px;
            z-index: 10;
        }
        .header-box h2 {
            font-size: 1.3rem;
            color: #fff;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        /* MAIN CONTAINER - SMOOTH & ADJUSTED */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 380px;
            border-radius: 25px;
            text-align: center;
            z-index: 5;
            border: 3px solid #fff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
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
            width: 90%;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ffffff;
            margin-bottom: 5px;
            text-shadow: 2px 2px 15px #ff0055;
        }

        .typing-text {
            font-size: 1.3rem;
            color: #fff;
            font-weight: 700;
            min-height: 60px;
            margin-bottom: 20px;
            text-shadow: 1px 1px 5px #000;
        }

        /* FOOTER - ATTRACTIVE & GLOWING */
        .footer-box {
            margin-top: 18px;
            background: linear-gradient(90deg, #ff4d6d, #ff758f, #ff4d6d);
            background-size: 200% auto;
            padding: 12px 30px;
            border-radius: 40px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px rgba(255, 77, 109, 0.7);
            z-index: 10;
            animation: shine 3s linear infinite;
        }
        @keyframes shine { to { background-position: 200% center; } }

        .footer-box p {
            font-weight: 800;
            color: #fff;
            font-size: 1rem;
            letter-spacing: 1px;
        }

        .btn {
            background: #ff4d6d;
            color: white;
            border: 2px solid #fff;
            padding: 12px 35px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 800;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn:active { transform: scale(0.95); }

        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #fff;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 4s linear forwards;
            z-index: 1;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(1); opacity: 0; }
            20% { opacity: 1; }
            100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
        }

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeIn 0.3s ease-out; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    
    <audio id="bgMusic" loop preload="auto">
        <source src="https://www.mboxdrive.com/raataan.mp3" type="audio/mpeg">
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
                <p class="typing-text" id="type1"></p>
                <button class="btn" onclick="startApp()">START SURPRISE ✨</button>
            </div>

            <div id="page2" class="screen">
                <h1 style="font-size: 3rem;">Beautiful</h1>
                <p class="typing-text" id="type2"></p>
                <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
            </div>

            <div id="page3" class="screen">
                <h1 style="font-size: 2.8rem;">Be Mine?</h1>
                <p class="typing-text">Zoe, kya hamesha mere saath rahoge? ❤️</p>
                <div style="display:flex; justify-content:center; gap:10px;">
                    <button class="btn" onclick="alert('I Love You Too, Zoe Jaan! 😘')">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444;" onmouseover="moveNoButton()">NO</button>
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

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "Aapke liye ek chota sa tohfa... Button dabaiye!",
            type2: "Aapki smile meri poori duniya hai, Zoe."
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            el.innerHTML = "";
            function type() {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, 40);
                }
            }
            type();
        }

        function startApp() {
            music.play().catch(e => console.log("Audio play failed, need user interaction."));
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
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        // Reduced frequency to prevent lag
        function createHeart() {
            if (document.querySelectorAll('.heart-float').length > 10) return;
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 10 + 10) + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
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
    app.run(host='0.0.0.0', port=5000)
