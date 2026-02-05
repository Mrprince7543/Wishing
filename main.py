from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Queen - Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #050505;
            color: white;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Animated Glowing Border Container */
        .border-box {
            position: relative;
            width: 90%;
            max-width: 450px;
            padding: 5px;
            background: linear-gradient(45deg, #ff4d6d, #ff758f, #c71585, #ff4d6d);
            background-size: 400%;
            border-radius: 25px;
            animation: borderGlow 8s linear infinite;
            box-shadow: 0 0 30px rgba(255, 77, 109, 0.5);
        }

        @keyframes borderGlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Glass Content Area */
        .screen {
            display: none;
            background: rgba(15, 12, 41, 0.9);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 40px 20px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .active { display: block; animation: fadeIn 1s ease-in; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Custom Cursor */
        #cursor {
            width: 25px;
            height: 25px;
            background: rgba(255, 77, 109, 0.8);
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 20px #ff4d6d;
            transform: translate(-50%, -50%);
            transition: width 0.2s, height 0.2s;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.2rem;
            color: #ff4d6d;
            margin-bottom: 15px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        }

        .typing-text {
            font-style: italic;
            font-size: 1.2rem;
            color: #ffb3c1;
            margin-bottom: 30px;
            min-height: 70px;
            line-height: 1.5;
        }

        .btn {
            background: linear-gradient(to right, #ff4d6d, #ff758f);
            color: white;
            border: none;
            padding: 12px 35px;
            border-radius: 50px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 10px 20px rgba(255, 77, 109, 0.3);
            transition: 0.4s;
        }
        .btn:hover { transform: scale(1.1); box-shadow: 0 0 25px #ff4d6d; }

        /* Floating Elements */
        .particle {
            position: absolute;
            pointer-events: none;
            z-index: -1;
            animation: float 5s linear infinite;
        }
        @keyframes float {
            0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
            20% { opacity: 1; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
    </audio>

    <div class="border-box">
        <div id="page1" class="screen active">
            <h1 style="font-size: 50px;">🌹</h1>
            <h1>Miss Zoe</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">Open Your Heart ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>The Smile...</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">Continue 💖</button>
        </div>

        <div id="page3" class="screen">
            <h1>Uniqueness</h1>
            <p class="typing-text" id="type3"></p>
            <button class="btn" onclick="nextPage(4)">Wait, more...</button>
        </div>

        <div id="page4" class="screen">
            <h1>True Feelings</h1>
            <p class="typing-text" id="type4"></p>
            <button class="btn" onclick="nextPage(5)">The Question 💍</button>
        </div>

        <div id="page5" class="screen">
            <h1>Be Mine?</h1>
            <p class="typing-text">Zoe, will you make my world beautiful forever by being my Valentine?</p>
            <div style="display:flex; justify-content:center; gap:15px; position:relative;">
                <button class="btn" onclick="alert('I Knew it! ❤️ Love you forever Zoe!')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background:#444;" onmouseover="moveNoButton()">NO</button>
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
            type1: "Aapke liye kuch bohot khaas hai... Kya aap dekhna chahengi?",
            type2: "Aapki ek smile poore din ki thakaan mita deti hai. Truly Magical!",
            type3: "Hazaaron hain is duniya mein, par Zoe jaisa koi dusra nahi hai.",
            type4: "Har pal aapka khayal, har dua mein aapka naam. Bas yahi hai dil ka haal."
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
                    setTimeout(type, 40);
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
            h.innerHTML = ['❤️', '💖', '✨', '🌹'][Math.floor(Math.random()*4)];
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 20 + 15 + 'px';
            h.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 5000);
        }
        setInterval(createHeart, 250);

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
