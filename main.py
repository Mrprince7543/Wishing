from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>75 Pages of Love for Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&family=Orbitron:wght@700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none; -webkit-tap-highlight-color: transparent; }
        body {
            background: #000;
            background: radial-gradient(circle at center, #1a0a0d 0%, #000000 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            padding: 10px;
        }
        .particle { position: absolute; pointer-events: none; animation: moveUp 7s linear forwards; z-index: 1; will-change: transform, opacity; }
        @keyframes moveUp { 0% { transform: translateY(110vh) scale(0.3); opacity: 0; } 20% { opacity: 0.6; } 100% { transform: translateY(-20vh) scale(1.2); opacity: 0; } }
        .top-title { font-family: 'Dancing Script', cursive; font-size: 2.8rem; color: #ff4d6d; text-align: center; margin-bottom: 10px; text-shadow: 0 0 15px #ff4d6d; z-index: 20; }
        .header-box { background: rgba(255, 77, 109, 0.1); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.3); padding: 10px 40px; border-radius: 50px; margin-bottom: 15px; z-index: 20; }
        .header-box h2 { font-family: 'Orbitron', sans-serif; font-size: 1.4rem; color: #fff; letter-spacing: 4px; text-transform: uppercase; }
        .love-card { position: relative; width: 100%; max-width: 550px; height: 480px; border-radius: 35px; z-index: 5; border: 2px solid rgba(255, 255, 255, 0.5); box-shadow: 0 0 50px rgba(255, 77, 109, 0.4); background: url('https://i.ibb.co/1YTf7R36/FB-IMG-16249452197243361.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: center; align-items: center; overflow: hidden; }
        .glass-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.65); backdrop-filter: blur(2px); z-index: 1; }
        .content-inner { position: relative; z-index: 2; width: 90%; text-align: center; }
        h1 { font-family: 'Dancing Script', cursive; font-size: 4.5rem; color: #ff4d6d; margin-bottom: 15px; text-shadow: 0 0 20px rgba(255, 77, 109, 0.8); }
        .typing-text { font-size: 1.6rem; color: #fff; font-weight: 700; min-height: 120px; line-height: 1.4; }
        .btn { background: #ff4d6d; color: #fff; border: none; padding: 16px 40px; border-radius: 50px; font-size: 1.2rem; font-weight: 800; cursor: pointer; margin-top: 20px; transition: 0.3s; }
        .btn:hover { transform: scale(1.1); box-shadow: 0 0 25px #ff4d6d; }
        #cursor { position: fixed; width: 25px; height: 25px; background: #ff4d6d; clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'); pointer-events: none; z-index: 9999; transform: translate(-50%, -50%); }
        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeEffect 0.6s ease-in; }
        @keyframes fadeEffect { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop>
        <source src="" type="audio/mpeg">
    </audio>

    <div class="top-title">Happy Valentine's Day Zoe 😘</div>
    <div class="header-box"><h2>REHAN LOVES ZOE</h2></div>

    <div class="love-card">
        <div class="glass-overlay"></div>
        <div class="content-inner">
            <div id="page1" class="screen active">
                <h1>Hi Zoe ❤️</h1>
                <p class="typing-text" id="type1">Aapke liye ye 75 pages ka sabse lamba aur pyara surprise taiyar hai... Ready?</p>
                <button class="btn" onclick="startApp()">START JOURNEY ✨</button>
            </div>
            
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1>Be Mine?</h1>
                <p class="typing-text">75 pages ki dastan ke baad, bas ek hi sawal... Will you be mine forever, Zoe? ❤️</p>
                <div style="display:flex; justify-content:center; gap:20px;">
                    <button class="btn" onclick="sayYes()">YES! ❤️</button>
                    <button class="btn" id="noBtn" style="background:#333; color:#fff;" onmouseover="moveNoButton()">NO</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        let currentPage = 0;

        // Inme se koi bhi random bajega (Direct MP3 links)
        const musicLinks = [
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", 
            "https://cdn.pixabay.com/audio/2022/05/27/audio_1808f3030e.mp3",
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
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
            }, 30);
        }

        function startApp() {
            // Pick a random song URL
            const randomSong = musicLinks[Math.floor(Math.random() * musicLinks.length)];
            music.src = randomSong;
            
            // Play with interaction (Zaroori hai browser ke liye)
            music.play().then(() => {
                console.log("Music started!");
            }).catch(e => {
                console.log("Error playing music: ", e);
            });

            document.getElementById('page1').style.display = 'none';
            document.getElementById('dynamic-content').style.display = 'block';
            nextStep();
        }

        // ... Baaki functions (nextStep, sayYes, moveNoButton, createParticle) wahi rahenge jo pehle the ...
        const story = [
            { h: "The Start", p: "Humari kahani meri zindagi ka sabse khoobsurat hissa hai." },
            { h: "The Smile", p: "Aapki muskurahat dekh kar mera din ban jata hai, Miss Zoe." },
            { h: "The Best", p: "Aap duniya ki sabse behtareen ladki ho." },
            { h: "My Everything", p: "Aap meri har khushi, har dua, har tamanna ho." },
            { h: "The Ending", p: "75 baatein khatam hui, magar pyar abhi shuru hua hai." }
        ];

        function nextStep() {
            if (currentPage < story.length) {
                const data = story[currentPage];
                document.getElementById('dyn-h1').innerText = data.h;
                typeEffect(document.getElementById('dyn-p'), data.p);
                currentPage++;
            } else {
                document.getElementById('dynamic-content').style.display = 'none';
                document.getElementById('final-page').style.display = 'block';
            }
        }

        function sayYes() {
            alert('I Love You Tooo Much, Zoe Jaan! 😘😘😘');
            setInterval(() => createParticle('❤️'), 100);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        function createParticle(symbol) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.innerHTML = symbol;
            p.style.left = Math.random() * 100 + 'vw';
            p.style.fontSize = (Math.random() * 20 + 10) + 'px';
            p.style.color = symbol === '❤️' ? '#ff4d6d' : '#fff';
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 7000);
        }

        setInterval(() => { createParticle('❤️'); }, 350);
        typeEffect(document.getElementById('type1'), "Aapke liye ye surprise taiyar hai... Ready?");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
