from flask import Flask, render_template_string

app = Flask(__name__)

# The Ultimate Romantic Masterpiece Script
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Life - Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #ff758f;
            background: radial-gradient(circle, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow-x: hidden;
            padding: 40px 0;
        }

        /* 1. TOP TITLE: HAPPY VALENTINE'S DAY MIZZ ZOE VERMA */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            color: #fff;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 15px #ff0055, 0 0 30px #ff0055, 2px 2px 5px rgba(0,0,0,0.3);
            animation: bounceIn 2s infinite alternate;
            z-index: 100;
        }

        @keyframes bounceIn {
            from { transform: scale(1); opacity: 0.9; }
            to { transform: scale(1.05); opacity: 1; }
        }

        /* 2. REHAN LOVES ZOE BOX */
        .header-box {
            background: linear-gradient(45deg, #ff4d6d, #ff758f);
            border: 3px solid #fff;
            padding: 20px 50px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 0 30px rgba(255, 77, 109, 0.8);
            animation: pulseBox 2.5s infinite ease-in-out;
            z-index: 100;
        }

        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 2rem;
            color: #fff;
            letter-spacing: 4px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        }

        @keyframes pulseBox {
            0%, 100% { transform: scale(1); box-shadow: 0 0 30px rgba(255, 77, 109, 0.8); }
            50% { transform: scale(1.08); box-shadow: 0 0 50px rgba(255, 77, 109, 1); }
        }

        /* 3. MAIN LARGE CONTAINER */
        .love-card {
            position: relative;
            width: 95%;
            max-width: 650px;
            min-height: 400px;
            padding: 60px 40px;
            background: rgba(255, 255, 255, 0.96);
            border-radius: 50px;
            box-shadow: 0 25px 60px rgba(255, 77, 109, 0.4);
            border: 5px solid #ffb3c1;
            text-align: center;
            z-index: 10;
            backdrop-filter: blur(8px);
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4rem;
            color: #ff4d6d;
            margin-bottom: 25px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        .typing-text {
            font-size: 1.4rem;
            color: #333;
            min-height: 80px;
            margin-bottom: 40px;
            font-weight: 500;
            line-height: 1.6;
        }

        /* 4. FOOTER BOX: I LOVE YOU MERI JAAN */
        .footer-box {
            margin-top: 40px;
            background: #fff;
            border: 3px dashed #ff4d6d;
            padding: 20px 40px;
            border-radius: 60px;
            box-shadow: 0 0 25px rgba(255, 77, 109, 0.5);
            z-index: 100;
            animation: slideUp 1s ease-out;
        }

        .footer-box p {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            color: #ff4d6d;
            font-size: 1.3rem;
            text-transform: uppercase;
        }

        /* Buttons & Cursor */
        .btn {
            background: linear-gradient(to right, #ff4d6d, #c71585);
            color: white;
            border: none;
            padding: 18px 45px;
            border-radius: 60px;
            font-size: 1.3rem;
            font-weight: 700;
            cursor: pointer;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 25px rgba(255, 77, 109, 0.5);
        }
        .btn:hover { transform: scale(1.1); box-shadow: 0 0 35px #ff4d6d; }

        #cursor {
            position: fixed;
            width: 25px; height: 25px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 15px #ff4d6d;
        }

        .heart-float {
            position: absolute;
            pointer-events: none;
            animation: moveUp 7s linear infinite;
        }

        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0); opacity: 0; }
            50% { opacity: 0.9; }
            100% { transform: translateY(-10vh) scale(2); opacity: 0; }
        }

        .screen { display: none; }
        .active { display: block; animation: zoomIn 0.8s ease; }
        @keyframes zoomIn { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">
        HAPPY VALENTINE'S DAY MIZZ ZOE VERMA 😘
    </div>

    <div class="header-box">
        <h2>REHAN LOVES ZOE</h2>
    </div>

    <div class="love-card">
        <div id="page1" class="screen active">
            <h1>Hi My Life ❤️</h1>
            <p class="typing-text" id="type1">System initialized... Loading your surprise...</p>
            <button class="btn" onclick="startApp()">CLICK TO UNLOCK MY HEART ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>Zoe Verma...</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">AAGE DEKHO JAAN 🌹</button>
        </div>

        <div id="page3" class="screen">
            <h1>Hamesha Ke Liye?</h1>
            <p class="typing-text">Zoe, meri har dua aapke naam se shuru hoti hai. Will you stay with me forever as my Valentine? ❤️</p>
            <div style="display:flex; justify-content:center; gap:30px; position:relative;">
                <button class="btn" onclick="alert('I Love You Tooo Much, Zoe Jaan! 😘😘😘')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background:#555; box-shadow:none;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <div class="footer-box">
        <p>I LOVE YOU MERI JAAN ZOE VERMA 😘😘😘</p>
    </div>

    <script>
        // Custom Cursor Follower
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "Aapke liye ek bohot pyaara surprise taiyar hai... Ready ho na?",
            type2: "Aapki smile duniya ki sabse haseen cheez hai, aur aap meri poori duniya ho, Zoe."
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
            const music = document.getElementById('bgMusic');
            music.play().catch(e => console.log("Audio needs user interaction"));
            nextPage(2);
        }

        function nextPage(num) {
            document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
            const next = document.getElementById('page' + num);
            next.classList.add('active');
            if(messages['type'+num]) typeEffect('type'+num, messages['type'+num]);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 120) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 120) + 'px';
        }

        // Floating Magical Hearts & Flowers
        setInterval(() => {
            const h = document.createElement('div');
            h.className = 'heart-float';
            const icons = ['❤️', '💖', '💍', '🌹', '✨'];
            h.innerHTML = icons[Math.floor(Math.random()*icons.length)];
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 30 + 15 + 'px';
            h.style.color = '#ff4d6d';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 7000);
        }, 200);

        typeEffect('type1', messages.type1);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Hosted on 0.0.0.0 and port 5000 as requested
    app.run(host='0.0.0.0', port=5000)
