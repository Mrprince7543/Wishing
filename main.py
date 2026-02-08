from flask import Flask, render_template_string

app = Flask(__name__)

# Ultimate Romantic Edition: "Rehan Loves Zoe" Special
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rehan Loves Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #ffe5ec;
            background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
        }

        /* Top Special Box: REHAN LOVES ZOE */
        .header-box {
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid #ff4d6d;
            padding: 15px 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.6);
            animation: pulseBox 2s infinite ease-in-out;
            backdrop-filter: blur(10px);
            z-index: 100;
        }

        .header-box h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
            color: #fff;
            text-shadow: 0 0 10px #ff4d6d, 0 0 20px #ff4d6d;
            letter-spacing: 2px;
            text-align: center;
        }

        @keyframes pulseBox {
            0%, 100% { transform: scale(1); box-shadow: 0 0 20px rgba(255, 77, 109, 0.6); }
            50% { transform: scale(1.05); box-shadow: 0 0 40px rgba(255, 77, 109, 0.9); }
        }

        /* Floating Hearts Animation */
        .heart-float {
            position: absolute;
            color: #ff4d6d;
            pointer-events: none;
            animation: moveHearts 6s linear infinite;
            z-index: 1;
        }
        @keyframes moveHearts {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            20% { opacity: 0.8; }
            100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }

        /* Custom Heart Cursor */
        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        /* Main Container */
        .love-card {
            position: relative;
            width: 90%;
            max-width: 450px;
            padding: 40px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            border: 2px solid #ffb3c1;
            text-align: center;
            z-index: 10;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #ff4d6d;
            margin-bottom: 20px;
        }

        .typing-text {
            font-size: 1.1rem;
            color: #444;
            min-height: 60px;
            margin-bottom: 30px;
            font-style: italic;
        }

        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.4);
        }
        .btn:hover { transform: scale(1.1); background: #ff758f; }

        .screen { display: none; }
        .active { display: block; animation: fadeIn 0.8s ease; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="header-box">
        <h2>REHAN LOVES ZOE</h2>
    </div>

    <div class="love-card">
        <div id="page1" class="screen active">
            <h1>Hi Miss Zoe ❤️</h1>
            <p class="typing-text" id="type1">Loading your surprise...</p>
            <button class="btn" onclick="startApp()">Enter Heart ✨</button>
        </div>

        <div id="page2" class="screen">
            <h1>Just for You</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">Aage Dekho 🌹</button>
        </div>

        <div id="page3" class="screen">
            <h1>Always Yours</h1>
            <p class="typing-text">Zoe, will you be my Valentine forever?</p>
            <div style="display:flex; justify-content:center; gap:15px; position:relative;">
                <button class="btn" onclick="alert('I Love You Too, Zoe! ❤️')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background:#aaa;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <script>
        // Cursor
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Typing Effect
        const messages = {
            type1: "Aapke liye ek chota sa tohfa... Kya aap taiyar hain?",
            type2: "Tumhari muskurahat jaise koi pyaara khwaab hai, baki sab fika hai."
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

        // Floating Hearts
        setInterval(() => {
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 20 + 15 + 'px';
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
