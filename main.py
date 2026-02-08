from flask import Flask, render_template_string

app = Flask(__name__)

# Stable & Attractive Version (No Zooming, Perfect Alignment)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #ff758f;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 20px;
        }

        /* 1. TOP TITLE - STABLE */
        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.2rem;
            color: #fff;
            text-align: center;
            margin-bottom: 15px;
            text-shadow: 2px 2px 10px #ff0055;
            z-index: 100;
        }

        /* 2. REHAN LOVES ZOE BOX - FIXED SIZE */
        .header-box {
            background: #ff4d6d;
            border: 3px solid #fff;
            padding: 15px 35px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.5);
            z-index: 100;
            text-align: center;
        }

        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
            color: #fff;
            letter-spacing: 2px;
        }

        /* 3. MAIN CONTAINER - MAINTAINED SIZE */
        .love-card {
            position: relative;
            width: 100%;
            max-width: 550px;
            min-height: 380px;
            padding: 40px 25px;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 30px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
            border: 3px solid #ffb3c1;
            text-align: center;
            z-index: 10;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ff4d6d;
            margin-bottom: 15px;
        }

        .typing-text {
            font-size: 1.2rem;
            color: #444;
            min-height: 70px;
            margin-bottom: 30px;
            line-height: 1.5;
        }

        /* 4. FOOTER BOX - ADJUSTED */
        .footer-box {
            margin-top: 25px;
            background: #fff;
            border: 2px dashed #ff4d6d;
            padding: 12px 30px;
            border-radius: 50px;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.3);
            z-index: 100;
        }

        .footer-box p {
            font-weight: 600;
            color: #ff4d6d;
            font-size: 1.1rem;
            text-align: center;
        }

        /* Buttons */
        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.3);
            align-self: center;
        }
        .btn:hover { background: #c71585; transform: translateY(-2px); }

        /* Cursor */
        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        /* Floating Hearts (No Zoom) */
        .heart-float {
            position: absolute;
            color: #ff4d6d;
            pointer-events: none;
            animation: moveUp 6s linear infinite;
        }
        @keyframes moveUp {
            from { transform: translateY(110vh); opacity: 1; }
            to { transform: translateY(-10vh); opacity: 0; }
        }

        .screen { display: none; }
        .active { display: block; animation: fadeIn 0.5s ease-in; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
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
            <p class="typing-text">Zoe, kya aap hamesha mere saath rahoge? Will you be my Valentine forever? ❤️</p>
            <div style="display:flex; justify-content:center; gap:15px; position:relative;">
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
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "Aapke liye kuch bohot khaas banaya hai... Ready ho?",
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
            h.style.fontSize = Math.random() * 20 + 10 + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 6000);
        }, 300);

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
