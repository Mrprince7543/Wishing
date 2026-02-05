from flask import Flask, render_template_string

app = Flask(__name__)

# The Ultimate Cyber-Love Terminal Script
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TERMINAL: ZOE_SECRET_ACCESS</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-pink: #ff0055;
            --neon-blue: #00fbff;
            --bg-black: #050505;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; }
        
        body {
            background-color: var(--bg-black);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Orbitron', sans-serif;
            overflow: hidden;
            color: white;
        }

        /* Matrix Rain Effect */
        canvas { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }

        /* Custom Laser Cursor */
        #cursor {
            position: fixed;
            width: 12px; height: 12px;
            background: #fff;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 15px #fff, 0 0 30px var(--neon-pink);
            transform: translate(-50%, -50%);
        }

        /* Scan Line Effect */
        .scan-line {
            position: absolute;
            width: 100%;
            height: 4px;
            background: var(--neon-pink);
            box-shadow: 0 0 20px var(--neon-pink);
            top: 0;
            z-index: 5;
            animation: scan 3s linear infinite;
            opacity: 0.5;
        }
        @keyframes scan {
            0% { top: 0; }
            100% { top: 100%; }
        }

        .neon-card {
            position: relative;
            width: 90%;
            max-width: 480px;
            padding: 40px;
            background: rgba(0, 0, 0, 0.85);
            border: 2px solid var(--neon-pink);
            border-radius: 5px;
            box-shadow: 0 0 25px var(--neon-pink), inset 0 0 15px var(--neon-pink);
            text-align: center;
            overflow: hidden;
        }

        /* Passcode Screen */
        #passcode-screen { display: block; }
        .input-code {
            background: transparent;
            border: 1px solid var(--neon-blue);
            color: var(--neon-blue);
            padding: 10px;
            text-align: center;
            font-size: 1.5rem;
            width: 150px;
            margin: 20px 0;
            outline: none;
        }

        /* Screens */
        .screen { display: none; }
        .active { display: block; animation: glitch 0.2s linear; }

        @keyframes glitch {
            0% { transform: translate(2px, -2px); }
            25% { transform: translate(-2px, 2px); }
            50% { transform: translate(2px, 2px); }
            100% { transform: translate(0); }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            text-shadow: 0 0 15px var(--neon-pink);
            margin-bottom: 20px;
        }

        .typing-text {
            color: var(--neon-blue);
            min-height: 80px;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .btn {
            background: transparent;
            color: white;
            border: 1px solid var(--neon-pink);
            padding: 12px 30px;
            font-family: 'Orbitron';
            font-weight: 900;
            letter-spacing: 2px;
            cursor: pointer;
            box-shadow: 0 0 10px var(--neon-pink);
            transition: 0.3s;
        }
        .btn:hover { background: var(--neon-pink); box-shadow: 0 0 30px var(--neon-pink); }

        .particle {
            position: absolute;
            color: var(--neon-pink);
            pointer-events: none;
            animation: moveUp 5s linear forwards;
        }
        @keyframes moveUp { from { bottom: -20px; opacity: 1; } to { bottom: 100vh; opacity: 0; } }
    </style>
</head>
<body>

    <canvas id="matrix"></canvas>
    <div id="cursor"></div>

    <audio id="bgMusic" loop>
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="neon-card">
        <div class="scan-line"></div>
        
        <div id="passcode-screen" class="screen active">
            <h2 style="color: var(--neon-blue); font-size: 0.9rem;">ENCRYPTED ACCESS ONLY</h2>
            <input type="password" id="passInput" class="input-code" placeholder="****">
            <br>
            <button class="btn" onclick="checkPass()">UNLOCK</button>
            <p id="errorMsg" style="color: red; margin-top: 10px; font-size: 0.7rem;"></p>
        </div>

        <div id="page1" class="screen">
            <h2 style="font-size: 0.8rem; color: var(--neon-blue);">SYSTEM DECODED</h2>
            <h1>Hi Zoe...</h1>
            <p class="typing-text" id="type1"></p>
            <button class="btn" onclick="startApp()">EXECUTE LOVE</button>
        </div>

        <div id="page2" class="screen">
            <h1>The Smile</h1>
            <p class="typing-text" id="type2"></p>
            <button class="btn" onclick="nextPage(3)">DEEP SCAN</button>
        </div>

        <div id="page3" class="screen">
            <h1>Unique Soul</h1>
            <p class="typing-text" id="type3"></p>
            <button class="btn" onclick="nextPage(4)">HEART STATUS</button>
        </div>

        <div id="page5" class="screen">
            <h1>Will You?</h1>
            <p class="typing-text">Zoe, access to my heart is forever granted to you. Will you be my Valentine?</p>
            <div style="display:flex; justify-content:center; gap:20px; position:relative;">
                <button class="btn" onclick="alert('ACCESS GRANTED FOREVER! ❤️')">YES</button>
                <button class="btn" id="noBtn" style="border-color: #444;" onmouseover="moveNoButton()">NO</button>
            </div>
        </div>
    </div>

    <script>
        // Matrix Effect
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const letters = "01LOVEZOE01";
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);

        function drawMatrix() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#ff0055";
            ctx.font = fontSize + "px Orbitron";
            for (let i = 0; i < drops.length; i++) {
                const text = letters.charAt(Math.floor(Math.random() * letters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(drawMatrix, 50);

        // Cursor
        const cursor = document.getElementById('cursor');
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Passcode Check
        function checkPass() {
            const pass = document.getElementById('passInput').value;
            if(pass === "1403") { // DEFAULT CODE
                document.getElementById('passcode-screen').classList.remove('active');
                document.getElementById('page1').classList.add('active');
                typeEffect('type1', "> ACCESS GRANTED. Zoe, aapke liye ek lethal surprise load ho raha hai...");
            } else {
                document.getElementById('errorMsg').innerText = "ACCESS DENIED: WRONG KEY";
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
            const next = document.getElementById('page' + num);
            if(next) next.classList.add('active');
            
            const msgs = {
                2: "> ANALYSIS: Aapki smile se bada khatra meri stability ko aur kisi cheez se nahi hai.",
                3: "> DATA: Encryption level 100. Zoe jaisa unique interface poore server mein nahi mila.",
                4: "> STATUS: Connection Established. Heart beat syncing with Raataan Lambiyan..."
            };
            if(msgs[num]) typeEffect('type'+num, msgs[num]);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        setInterval(() => {
            const p = document.createElement('div');
            p.className = 'particle';
            p.innerHTML = '❤️';
            p.style.left = Math.random() * 100 + 'vw';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 5000);
        }, 300);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
