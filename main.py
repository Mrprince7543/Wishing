from flask import Flask, render_template_string

app = Flask(__name__)

# Ultra-Attractive "Zoe Verma" Edition with Custom Background
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zoe Verma Special ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;700&family=Orbitron:wght@700&display=swap" rel="stylesheet">
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
            padding: 10px;
        }

        /* Top Title - Large & Colorful */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            color: #ff0055;
            text-align: center;
            margin-bottom: 10px;
            background: white;
            padding: 5px 15px;
            border-radius: 50px;
            box-shadow: 0 5px 15px rgba(255, 0, 85, 0.3);
            z-index: 10;
        }

        /* Rehan Loves Zoe - Neon Effect */
        .header-box {
            background: #ff4d6d;
            border: 3px solid #fff;
            padding: 10px 30px;
            border-radius: 15px;
            margin-bottom: 15px;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.6);
            z-index: 10;
        }
        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.6rem;
            color: #fff;
            letter-spacing: 2px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        }

        /* MAIN CONTAINER WITH YOUR IMAGE */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 550px;
            min-height: 400px;
            padding: 40px 25px;
            border-radius: 30px;
            text-align: center;
            z-index: 5;
            border: 5px solid #fff;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            
            /* Background Image Setup */
            background-image: url('https://i.ibb.co/rGT6qF7r/Picture-Unlock-TOI-521963-user0-pictureunlock.webp');
            background-size: cover;
            background-position: center;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Overlay for Text Readability */
        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(255, 255, 255, 0.15); /* Light glass effect */
            backdrop-filter: blur(2px);
            z-index: -1;
        }

        /* Large Colorful Words */
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4.5rem;
            color: #fff;
            margin-bottom: 10px;
            text-shadow: 4px 4px 10px #ff0055, -2px -2px 10px #000;
        }

        .typing-text {
            font-size: 1.6rem;
            color: #fff;
            font-weight: 700;
            min-height: 80px;
            margin-bottom: 25px;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
            background: rgba(0,0,0,0.3);
            padding: 10px;
            border-radius: 15px;
        }

        /* Footer Box */
        .footer-box {
            margin-top: 15px;
            background: #ff4d6d;
            padding: 10px 25px;
            border-radius: 50px;
            border: 2px solid #fff;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.5);
            z-index: 10;
        }
        .footer-box p {
            font-weight: 700;
            color: #fff;
            font-size: 1.2rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        }

        /* Bigger Buttons */
        .btn {
            background: #fff;
            color: #ff4d6d;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 1.3rem;
            font-weight: 900;
            text-transform: uppercase;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .btn:hover { transform: scale(1.1); background: #ff4d6d; color: #fff; }

        /* Custom Cursor */
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

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeIn 0.5s ease-in; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 6s linear forwards;
            z-index: 1;
        }
        @keyframes moveUp {
            from { transform: translateY(110vh); opacity: 1; }
            to { transform: translateY(-10vh); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">HAPPY VALENTINE'S DAY ZOE 😘</div>

    <div class="header-box">
        <h2>REHAN LOVES ZOE</h2>
    </div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        
        <div id="page1" class="screen active">
            <h1>Hi Jaan ❤️</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">START SURPRISE ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>Beautiful</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
        </div>

        <div id="page3" class="screen">
            <h1 style="font-size: 3rem;">Be Mine Forever?</h1>
            <p class="typing-text">Zoe, kya hamesha mere saath rahoge? Will you be my Valentine? ❤️</p>
            <div style="display:flex; justify-content:center; gap:15px; position:relative;">
                <button class="btn" onclick="alert('I Love You Too, Zoe Jaan! 😘😘😘')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background:#888; color:#fff;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <div class="footer-box">
        <p>I LOVE YOU MERI JAAN ZOE VERMA 😘😘😘</p>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "Aapke liye kuch bohot colorful banaya hai... Ready ho?",
            type2: "Aapki smile meri duniya hai, aur aap meri zindagi ka sabse haseen hissa ho."
        };

        function typeEffect(elementId, text) {
            let i = 0;
            const el = document.getElementById(elementId);
            el.innerHTML = "";
            function type() {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, 50);
                }
            }
            type();
        }

        function startApp() {
            document.getElementById('bgMusic').play();
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

        setInterval(() => {
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 20 + 15 + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }, 250);

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
