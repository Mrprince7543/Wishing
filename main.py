from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Miss Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        body {
            background: #0f0c29;
            background: linear-gradient(135deg, #24243e, #302b63, #0f0c29, #4b1248);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: white;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Custom Heart Cursor */
        #cursor {
            width: 20px;
            height: 20px;
            background: #ff4d6d;
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 10px #ff4d6d;
            transition: transform 0.1s;
        }

        .screen {
            display: none;
            text-align: center;
            padding: 30px;
            width: 90%;
            max-width: 500px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }
        .active { display: block; animation: zoomIn 0.8s ease forwards; }

        @keyframes zoomIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #ff4d6d;
            text-shadow: 0 0 15px rgba(255, 77, 109, 0.8);
            margin-bottom: 20px;
        }

        .typing-text {
            font-style: italic;
            font-size: 1.1rem;
            color: #ffb3c1;
            margin-bottom: 30px;
            min-height: 60px;
        }

        .heart-main {
            font-size: 80px;
            animation: heartbeat 1.2s infinite;
            margin-bottom: 10px;
            display: inline-block;
        }
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }

        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.3s;
            font-weight: 600;
            z-index: 100;
        }
        .btn:hover { background: #ff758f; transform: scale(1.1); }

        /* Prank No Button */
        #noBtn {
            position: relative;
            background: #555;
        }

        .particle {
            position: absolute;
            pointer-events: none;
            z-index: -1;
            animation: floatUp 4s linear infinite;
        }
        @keyframes floatUp {
            from { transform: translateY(110vh); opacity: 1; }
            to { transform: translateY(-10vh); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    
    <audio id="bgMusic" loop>
        <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
    </audio>

    <div id="page1" class="screen active">
        <div class="heart-main">❤️</div>
        <h1>Hi Miss Zoe!</h1>
        <p class="typing-text" id="type1"></p>
        <button class="btn" onclick="startApp()">Enter Her Heart ✨</button>
    </div>

    <div id="page2" class="screen">
        <div class="heart-main">🌹</div>
        <h1>Aapki Smile...</h1>
        <p class="typing-text" id="type2"></p>
        <button class="btn" onclick="nextPage(3)">Aage Dekho</button>
    </div>

    <div id="page3" class="screen">
        <div class="heart-main">✨</div>
        <h1>Sabse Khaas</h1>
        <p class="typing-text" id="type3"></p>
        <button class="btn" onclick="nextPage(4)">Aur Kuch?</button>
    </div>

    <div id="page4" class="screen">
        <div class="heart-main">💖</div>
        <h1>Sirf Tum</h1>
        <p class="typing-text" id="type4"></p>
        <button class="btn" onclick="nextPage(5)">Final Surprise</button>
    </div>

    <div id="page5" class="screen">
        <div class="heart-main">💍</div>
        <h1>Will You?</h1>
        <p class="typing-text">Will you make this Valentine's Day the best one ever, Miss Zoe?</p>
        <div style="display:flex; justify-content:center; gap:20px; position:relative;">
            <button class="btn" onclick="alert('Yay! ❤️ Zoe, You made my day!')">Yes! ❤️</button>
            <button class="btn" id="noBtn" onmouseover="moveNoButton()">No</button>
        </div>
    </div>

    <script>
        // Cursor Follower
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        const messages = {
            type1: "Aapke liye ek chota sa tohfa... Kya aap taiyar hain?",
            type2: "Tumhari muskurahat jaise koi pyaara khwaab hai, Zoe tumhara koi jawaab nahi.",
            type3: "Hazaaron milenge chehre is bheed mein, Par humara dil toh sirf aap pe fida hai.",
            type4: "Zindagi me aap aaye, baki sab bhul gaye. You are truly unique!"
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
            if(messages['type'+num]) {
                typeEffect('type'+num, messages['type'+num]);
            }
        }

        // Prank: Move No Button
        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 100);
            btn.style.position = 'fixed';
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }

        // Floating Hearts
        function createHeart() {
            const h = document.createElement('div');
            h.classList.add('particle');
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 20 + 10 + 'px';
            h.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
        }
        setInterval(createHeart, 200);

        // Initial Typing
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
