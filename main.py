from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Surprise for Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        
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

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2rem;
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
            text-shadow: 0 0 10px #ff0055;
            z-index: 20;
        }

        .header-box {
            background: rgba(255, 77, 109, 0.95);
            border: 2px solid #fff;
            padding: 8px 30px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            z-index: 20;
        }
        .header-box h2 { font-size: 1.2rem; color: #fff; letter-spacing: 2px; text-transform: uppercase; }

        .love-card {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 400px;
            border-radius: 25px;
            z-index: 5;
            border: 3.5px solid #fff;
            box-shadow: 0 15px 45px rgba(0,0,0,0.3);
            background: url('https://i.ibb.co/rGT6qF7r/Picture-Unlock-TOI-521963-user0-pictureunlock.webp') center/cover no-repeat;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            will-change: transform;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(1px);
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 92%; text-align: center; }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.2rem;
            color: #ffffff;
            margin-bottom: 8px;
            text-shadow: 2px 2px 15px #ff0055;
        }

        .typing-text {
            font-size: 1.2rem;
            color: #fff;
            font-weight: 700;
            min-height: 80px;
            text-shadow: 1px 1px 10px #000;
            line-height: 1.4;
        }

        .footer-box {
            margin-top: 20px;
            background: linear-gradient(90deg, #ff4d6d, #ff758f, #ff4d6d);
            padding: 12px 30px;
            border-radius: 50px;
            border: 2px solid #fff;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.8);
            z-index: 20;
            text-align: center;
        }
        .footer-box p { font-weight: 800; color: #fff; font-size: 0.9rem; text-transform: uppercase; }

        .btn {
            background: #ff4d6d;
            color: white;
            border: 2px solid #fff;
            padding: 12px 25px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.2s ease;
        }
        .btn:active { transform: scale(0.95); }

        #cursor {
            position: fixed;
            width: 20px; height: 20px;
            background: #fff;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
        }

        .heart-float {
            position: absolute;
            color: #fff;
            pointer-events: none;
            animation: moveUp 5s linear forwards;
            z-index: 1;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh); opacity: 0; }
            100% { transform: translateY(-10vh); opacity: 0; }
        }

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeIn 0.4s ease-out; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop preload="auto">
        <source src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3" type="audio/mpeg">
    </audio>

    <div class="top-title">Happy Valentine's Day Zoe 😘</div>
    <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Jaan ❤️</h1>
                <p class="typing-text" id="type1">Zoe, aapke liye ek bahut lamba surprise taiyar kiya hai...</p>
                <button class="btn" onclick="startApp()">SHURU KAREIN? ✨</button>
            </div>
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1>Be Mine?</h1>
                <p class="typing-text">Zoe Verma, kya hamesha mere saath rahoge? Will you be mine forever? ❤️</p>
                <div style="display:flex; justify-content:center; gap:10px;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#444;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-box"><p>💖 I LOVE YOU MERI JAAN ZOE VERMA 💖</p></div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        let currentPage = 0;

        const story = [
            { h: "The Smile", p: "Aapki smile meri poori duniya ko roshan kar deti hai, Miss Zoe." },
            { h: "Pure Soul", p: "Maine duniya dekhi, par aap jaisa saaf dil aaj tak kahin nahi mila." },
            { h: "My Dream", p: "Har raat aapka hi khayal aata hai, aap mera sabse haseen khwaab ho." },
            { h: "Special", p: "Aap sirf ek ladki nahi, aap meri zindagi ki zarurat ban gaye ho." },
            { h: "The Magic", p: "Aapki aankhon mein wo jaadu hai jo mujhe har baar pagal kar deta hai." },
            { h: "Peace", p: "Aap se baat karke jo sukoon milta hai, wo poori duniya mein kahin nahi." },
            { h: "Destiny", p: "Mujhe lagta hai humara milna koi ittefaq nahi, naseeb ka faisla tha." },
            { h: "Happiness", p: "Aapki ek khushi ke liye main poori duniya se lad sakta hoon." },
            { h: "The Voice", p: "Jab aap mera naam lete ho, toh dil ki dhadkan thoda aur tez ho jati hai." },
            { h: "Wada", p: "Main kabhi aapka hath nahi chhodunga, chahe rasta kitna bhi mushkil ho." },
            { h: "Together", p: "Humein sath dekhna hi meri sabse badi tamanna hai, har pal, har jagah." },
            { h: "My Queen", p: "Aap mere dil ki rani ho, aur hamesha rahoge, meri jaan." },
            { h: "Forever", p: "Pyar toh sab karte hain, par main aapko hamesha pooja karunga." },
            { h: "The End?", p: "Nahi... Ye toh sirf humari nayi shuruat hai. Bas ek aakhri baat..." }
        ];

        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        function typeEffect(element, text) {
            let i = 0;
            element.innerHTML = "";
            clearInterval(window.typingInterval);
            window.typingInterval = setInterval(() => {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                } else { clearInterval(window.typingInterval); }
            }, 35);
        }

        function startApp() {
            music.play().catch(() => { window.addEventListener('click', () => music.play(), {once: true}); });
            document.getElementById('page1').classList.remove('active');
            document.getElementById('dynamic-content').classList.add('active');
            nextStep();
        }

        function nextStep() {
            if (currentPage < story.length) {
                const data = story[currentPage];
                document.getElementById('dyn-h1').innerText = data.h;
                typeEffect(document.getElementById('dyn-p'), data.p);
                currentPage++;
            } else {
                document.getElementById('dynamic-content').classList.remove('active');
                document.getElementById('final-page').classList.add('active');
            }
        }

        function sayYes() {
            alert('I Love You Tooo Much, Zoe Jaan! 😘😘😘');
            setInterval(createHeart, 150);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        function createHeart() {
            if (document.querySelectorAll('.heart-float').length > 12) return;
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 15 + 10) + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
        }
        setInterval(createHeart, 800);
        typeEffect(document.getElementById('type1'), "Zoe, aapke liye ek bahut lamba surprise taiyar kiya hai...");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
