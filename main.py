from flask import Flask, render_template_string

app = Flask(__name__)

# Single file script with CSS, JS and HTML combined
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Miss Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #0f0c29;
            background: linear-gradient(to bottom, #24243e, #302b63, #0f0c29);
            color: white;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Screen Management */
        .screen {
            display: none;
            text-align: center;
            padding: 20px;
            animation: fadeIn 1.5s ease-in-out forwards;
        }
        .active { display: block; }

        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }

        /* Typography */
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: #ff4d6d;
            text-shadow: 0 0 20px rgba(255, 77, 109, 0.6);
            margin-bottom: 20px;
        }
        .shayari {
            font-style: italic;
            font-size: 1.2rem;
            line-height: 1.6;
            color: #ffb3c1;
            margin-bottom: 30px;
        }

        /* Buttons */
        .btn {
            background: #ff4d6d;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.4);
        }
        .btn:hover {
            background: #ff758f;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(255, 77, 109, 0.6);
        }

        /* Heart Animation */
        .heart-main {
            font-size: 100px;
            color: #ff4d6d;
            animation: heartbeat 1.2s infinite;
            margin-bottom: 10px;
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            15% { transform: scale(1.3); }
            30% { transform: scale(1); }
            45% { transform: scale(1.15); }
            60% { transform: scale(1); }
        }

        /* Particle Hearts */
        .particle {
            position: absolute;
            color: #ff4d6d;
            pointer-events: none;
            z-index: -1;
            animation: moveUp 4s linear infinite;
        }
        @keyframes moveUp {
            from { transform: translateY(100vh) rotate(0deg); opacity: 1; }
            to { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="page1" class="screen active">
        <div class="heart-main">❤️</div>
        <h1>Happy Valentine's Day, Miss Zoe</h1>
        <div class="shayari">
            "Tumhari muskurahat jaise koi khwaab hai,<br>
            Har pal tumhara saath mere liye la-jawaab hai."
        </div>
        <button class="btn" onclick="nextPage()">Aage Dekho ✨</button>
    </div>

    <div id="page2" class="screen">
        <h1>Will You Be My Valentine?</h1>
        <p style="font-size: 1.3rem; margin-bottom: 20px;">
            Aapka saath meri har khushi ko doguna kar deta hai. 🌹
        </p>
        <div class="heart-main" style="font-size: 60px;">💖</div>
        <p style="color: #ffb3c1;">#SpecialMoments #Zoe</p>
        <br>
        <button class="btn" onclick="prevPage()">Wapas Chalo</button>
    </div>

    <script>
        function nextPage() {
            document.getElementById('page1').classList.remove('active');
            document.getElementById('page2').classList.add('active');
        }

        function prevPage() {
            document.getElementById('page2').classList.remove('active');
            document.getElementById('page1').classList.add('active');
        }

        // Particle Heart Generator
        function createParticle() {
            const p = document.createElement('div');
            p.classList.add('particle');
            p.innerHTML = '❤️';
            p.style.left = Math.random() * 100 + 'vw';
            p.style.fontSize = Math.random() * 20 + 10 + 'px';
            p.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 4000);
        }
        setInterval(createParticle, 150);
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
