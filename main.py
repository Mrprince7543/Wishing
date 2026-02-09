from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - 8 PAGE ULTIMATE SMOOTH EDITION
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Surprise for Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
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

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.1rem;
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
            text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055;
            z-index: 20;
        }

        .header-box {
            background: rgba(255, 77, 109, 0.95);
            border: 2px solid #fff;
            padding: 8px 30px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            z-index: 20;
        }
        .header-box h2 { font-size: 1.3rem; color: #fff; letter-spacing: 2px; text-transform: uppercase; }

        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 400px;
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
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(1px);
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 92%; text-align: center; }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ffffff;
            margin-bottom: 8px;
            text-shadow: 2px 2px 15px #ff0055;
        }

        .typing-text {
            font-size: 1.3rem;
            color: #fff;
            font-weight: 700;
            min-height: 85px;
            text-shadow: 1px 1px 10px #000;
            line-height: 1.3;
        }

        .footer-box {
            margin-top: 20px;
            background: linear-gradient(90deg, #ff4d6d, #ff758f, #ff4d6d);
            padding: 12px 30px;
            border-radius: 50px;
            border: 2px solid #fff;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.8);
            z-index: 20;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-width: 280px;
        }
        .footer-box p { font-weight: 800; color: #fff; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px; }

        .btn {
            background: #ff4d6d;
            color: white;
            border: 2px solid #fff;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transition: 0.2s ease;
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
            filter: drop-shadow(0 0 5px #ff4d6d);
        }

        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 5s linear forwards;
            z-index: 1;
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
    <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Jaan ❤️</h1>
                <p class="typing-text" id="type1">Aapke liye ek special surprise wait kar raha hai...</p>
                <button class="btn" onclick="startApp()">START SURPRISE ✨</button>
            </div>
            <div id="page2" class="screen">
                <h1>The Smile</h1>
                <p class="typing-text" id="type2"></p>
                <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
            </div>
            <div id="page3" class="screen">
                <h1>Your Voice</h1>
                <p class="typing-text" id="type3"></p>
                <button class="btn" onclick="nextPage(4)">Wait, One More... 💖</button>
            </div>
            <div id="page4" class="screen">
                <h1>The Magic</h1>
                <p class="typing-text" id="type4"></p>
                <button class="btn" onclick="nextPage(5)">Dekhte Raho ✨</button>
            </div>
            <div id="page5" class="screen">
                <h1>My World</h1>
                <p class="typing-text" id="type5"></p>
                <button class="btn" onclick="nextPage(6)">Almost There... 🌹</button>
            </div>
            <div id="page6" class="screen">
                <h1>Promises</h1>
                <p class="typing-text" id="type6"></p>
                <button class="btn" onclick="nextPage(7)">Final Page 💍</button>
            </div>
            <div id="page7" class="screen">
                <h1>Be Mine?</h1>
                <p class="typing-text">Zoe, kya aap hamesha mere saath rahoge? Will you be mine forever? ❤️</p>
                <div style="display:flex; justify-content:center; gap:10px; position:relative;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-box"><p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p></div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type2: "Aapki smile meri duniya hai, aur aap meri zindagi ka sabse pyara hissa ho.",
            type3: "Aapki baatein sunna mujhe sukoon deta hai. Har pal bas aapka hi khayal rehta hai.",
            type4: "Jaadu hai aapki aankhon mein, jab bhi dekhta hoon, khud ko bhool jata hoon.",
            type5: "Zindagi mein sab kuch mil gaya, jab se aap mile. Ab kuch aur nahi chahiye.",
            type6: "Wada hai mera, har khushi aur har gham mein aapka hath kabhi nahi chhodunga."
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            el.innerHTML = "";
            const timer = setInterval(() => {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                } else { clearInterval(timer); }
            }, 40);
        }

        function startApp() {
            music.play().catch(() => {
                window.addEventListener('click', () => music.play(), {once: true});
            });
            nextPage(2);
        }

        function nextPage(num) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            document.getElementById('page' + num).classList.add('active');
            if(messages['type'+num]) typeEffect('type'+num, messages['type'+num]);
        }

        function sayYes() {
            alert('I Love You Too, Zoe Jaan! 😘😘😘');
            setInterval(() => {
                createHeart();
            }, 100);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

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
        setInterval(createHeart, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
