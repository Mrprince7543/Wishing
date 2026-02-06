from flask import Flask, render_template_string

app = Flask(__name__)

# Ultimate Magical Love Edition
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background: #fff0f3;
            background: radial-gradient(circle, #ffdee9 0%, #b5fffc 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
        }

        /* Floating Bubbles Effect */
        .bubble {
            position: absolute;
            background: rgba(255, 182, 193, 0.4);
            border-radius: 50%;
            pointer-events: none;
            animation: floatUp 8s infinite ease-in;
            z-index: 1;
        }
        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            50% { opacity: 0.8; }
            100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
        }

        /* Custom Magic Heart Cursor */
        #cursor {
            position: fixed;
            width: 25px; height: 25px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 15px #ff4d6d;
            transform: translate(-50%, -50%);
        }

        /* Magical Card with Golden Glow */
        .love-card {
            position: relative;
            width: 90%;
            max-width: 450px;
            padding: 40px;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(15px);
            border: 3px solid #ffb3c1;
            border-radius: 30px;
            box-shadow: 0 15px 35px rgba(255, 77, 109, 0.2), 0 0 20px rgba(255, 215, 0, 0.3);
            text-align: center;
            z-index: 10;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ff4d6d;
            margin-bottom: 15px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }

        .typing-text {
            font-size: 1.2rem;
            color: #555;
            min-height: 70px;
            line-height: 1.6;
            margin-bottom: 25px;
            font-style: italic;
        }

        .btn {
            background: linear-gradient(45deg, #ff4d6d, #ff758f);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 8px 15px rgba(255, 77, 109, 0.3);
            transition: 0.3s ease;
        }
        .btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 12px 20px rgba(255, 77, 109, 0.4);
        }

        /* Access Key Styling */
        .key-input {
            width: 120px;
            padding: 10px;
            border: 2px solid #ffb3c1;
            border-radius: 15px;
            text-align: center;
            font-size: 1.5rem;
            color: #ff4d6d;
            margin: 20px 0;
            outline: none;
            background: rgba(255, 255, 255, 0.5);
        }

        .screen { display: none; }
        .active { display: block; animation: fadeIn 1s ease; }

        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }

        .heart-icon {
            font-size: 50px;
            color: #ff4d6d;
            animation: beat 1.2s infinite;
        }
        @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="love-card">
        <div class="heart-icon">❤️</div>
        
        <div id="page0" class="screen active">
            <h2 style="color: #ff4d6d; font-size: 1.2rem;">Enter Secret Love Key</h2>
            <input type="password" id="passInput" class="key-input" placeholder="****" maxlength="4">
            <br>
            <button class="btn" onclick="checkPass()">Unlock Heart ✨</button>
            <p id="errorMsg" style="color: #ff4d6d; margin-top: 10px; font-size: 0.8rem;"></p>
        </div>

        <div id="page1" class="screen">
            <h1>Hi Miss Zoe</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">Aage Dekho ❤️</button>
        </div>

        <div id="page2" class="screen">
            <h1>Your Smile...</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">Continue 🌹</button>
        </div>

        <div id="page3" class="screen">
            <h1>Will You?</h1>
            <p class="typing-text">Zoe, you are the most special person in my life. Will you be my Valentine forever?</p>
            <div style="display:flex; justify-content:center; gap:20px; position:relative;">
                <button class="btn" onclick="alert('Yay! ❤️ I Love You Zoe!')">YES! ❤️</button>
                <button class="btn" id="noBtn" style="background: #ccc;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <script>
        // Magic Cursor
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Bubbles Background
        function createBubble() {
            const b = document.createElement('div');
            b.classList.add('bubble');
            const size = Math.random() * 60 + 20 + 'px';
            b.style.width = size;
            b.style.height = size;
            b.style.left = Math.random() * 100 + 'vw';
            b.style.animationDuration = Math.random() * 5 + 5 + 's';
            document.body.appendChild(b);
            setTimeout(() => b.remove(), 8000);
        }
        setInterval(createBubble, 500);

        // Passcode Check
        function checkPass() {
            const pass = document.getElementById('passInput').value;
            if(pass === "1403") {
                document.getElementById('page0').classList.remove('active');
                document.getElementById('page1').classList.add('active');
                typeEffect('type1', "Aapke liye ek pyaara sa surprise taiyar hai... Kya aap dekhna chahengi?");
            } else {
                document.getElementById('errorMsg').innerText = "Oops! Wrong Key. Try again ❤️";
            }
        }

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
            const msgs = {
                2: "Aapki smile duniya ki sabse pyari cheez hai. Bas aise hi hamesha hasti raho!",
            };
            if(msgs[num]) typeEffect('type'+num, msgs[num]);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
