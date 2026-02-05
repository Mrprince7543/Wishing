from flask import Flask, render_template_string

app = Flask(__name__)

# Full Single File Script: 5 Pages with Animations & Shayari
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special for Miss Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
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

        /* Screen Transitions */
        .screen {
            display: none;
            text-align: center;
            padding: 30px;
            width: 90%;
            max-width: 500px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            animation: slideUp 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }
        .active { display: block; }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(50px) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #ff4d6d;
            text-shadow: 0 0 15px rgba(255, 77, 109, 0.8);
            margin-bottom: 20px;
        }

        .shayari {
            font-style: italic;
            font-size: 1.1rem;
            line-height: 1.6;
            color: #ffb3c1;
            margin-bottom: 30px;
            min-height: 80px;
        }

        /* Heart Animation */
        .heart-main {
            font-size: 80px;
            color: #ff4d6d;
            animation: heartbeat 1.2s infinite;
            margin-bottom: 10px;
            filter: drop-shadow(0 0 10px #ff4d6d);
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            20% { transform: scale(1.3); }
            40% { transform: scale(1); }
        }

        /* Buttons */
        .btn-group { display: flex; justify-content: center; gap: 15px; }
        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 50px;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.4);
            font-weight: 600;
        }
        .btn:hover {
            background: #ff758f;
            transform: scale(1.05);
        }
        .btn-back { background: rgba(255,255,255,0.1); }

        /* Floating Particles */
        .particle {
            position: absolute;
            color: #ff4d6d;
            pointer-events: none;
            z-index: -1;
            animation: floatUp 4s linear infinite;
        }
        @keyframes floatUp {
            from { transform: translateY(110vh) rotate(0deg); opacity: 1; }
            to { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="page1" class="screen active">
        <div class="heart-main">❤️</div>
        <h1>Hi Miss Zoe!</h1>
        <div class="shayari">
            "Aapki ek jhalak ke liye taraste hain,<br>
            Hum har pal bas aapki raah takte hain."
        </div>
        <button class="btn" onclick="showPage(2)">Aage Dekho ✨</button>
    </div>

    <div id="page2" class="screen">
        <div class="heart-main">✨</div>
        <h1>Aapki Smile...</h1>
        <div class="shayari">
            "Tumhari muskurahat jaise koi pyaara khwaab hai,<br>
            Pure jahaan mein Zoe, tumhara koi jawaab nahi."
        </div>
        <div class="btn-group">
            <button class="btn btn-back" onclick="showPage(1)">Piche</button>
            <button class="btn" onclick="showPage(3)">Next 🌹</button>
        </div>
    </div>

    <div id="page3" class="screen">
        <div class="heart-main">🌟</div>
        <h1>Har Pal Khaas</h1>
        <div class="shayari">
            "Phoolon se haseen tumhari adaa hai,<br>
            Aapko dekh kar hi dil ko milta sukoon hai."
        </div>
        <div class="btn-group">
            <button class="btn btn-back" onclick="showPage(2)">Piche</button>
            <button class="btn" onclick="showPage(4)">Aur Kuch... 🎁</button>
        </div>
    </div>

    <div id="page4" class="screen">
        <div class="heart-main">🔥</div>
        <h1>Sabse Alag</h1>
        <div class="shayari">
            "Hazaaron milenge chehre is bheed mein,<br>
            Par humara dil toh sirf 'Zoe' pe fida hai."
        </div>
        <div class="btn-group">
            <button class="btn btn-back" onclick="showPage(3)">Piche</button>
            <button class="btn" onclick="showPage(5)">Final Surprise 💖</button>
        </div>
    </div>

    <div id="page5" class="screen">
        <div class="heart-main">💝</div>
        <h1>Happy Valentine's Day</h1>
        <div class="shayari">
            "Will you make this day special by being mine?<br>
            Happy Valentine's Day, Miss Zoe!"
        </div>
        <div class="btn-group">
            <button class="btn btn-back" onclick="showPage(4)">Wapas</button>
            <button class="btn" onclick="alert('Yay! ❤️ I Love You Zoe!')">Yes! 💍</button>
        </div>
    </div>

    <script>
        function showPage(pageNumber) {
            // Hide all screens
            const screens = document.querySelectorAll('.screen');
            screens.forEach(s => s.classList.remove('active'));
            
            // Show requested screen
            document.getElementById('page' + pageNumber).classList.add('active');
        }

        // Particle Heart Generator
        function createParticle() {
            const p = document.createElement('div');
            p.classList.add('particle');
            const hearts = ['❤️', '💖', '💗', '🌹', '✨'];
            p.innerHTML = hearts[Math.floor(Math.random() * hearts.length)];
            p.style.left = Math.random() * 100 + 'vw';
            p.style.fontSize = Math.random() * 20 + 15 + 'px';
            p.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 4000);
        }
        setInterval(createParticle, 200);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Running on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
