from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - 32-PAGE ULTIMATE PERFORMANCE EDITION
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>32 Pages of Love for Zoe Verma ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    <style>
        /* Smooth Performance Fixes */
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
            will-change: background;
        }

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 1.8rem;
            color: #fff;
            text-align: center;
            margin-bottom: 8px;
            text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055;
            z-index: 20;
        }

        .header-box {
            background: rgba(255, 77, 109, 0.95);
            border: 2px solid #fff;
            padding: 8px 25px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            z-index: 20;
        }
        .header-box h2 { font-size: 1.1rem; color: #fff; letter-spacing: 2px; text-transform: uppercase; }

        /* Optimized Card */
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
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(1.5px);
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 92%; text-align: center; }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3rem;
            color: #ffffff;
            margin-bottom: 8px;
            text-shadow: 2px 2px 15px #ff0055;
        }

        .typing-text {
            font-size: 1.15rem;
            color: #fff;
            font-weight: 700;
            min-height: 80px;
            text-shadow: 1px 1px 10px #000;
            line-height: 1.4;
        }

        /* Attractive Footer - Adjusted */
        .footer-box {
            margin-top: 15px;
            background: linear-gradient(90deg, #ff4d6d, #ff758f, #ff4d6d);
            padding: 12px 25px;
            border-radius: 50px;
            border: 2px solid #fff;
            box-shadow: 0 0 15px rgba(255, 77, 109, 0.7);
            z-index: 20;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .footer-box p { font-weight: 800; color: #fff; font-size: 0.85rem; text-transform: uppercase; margin: 0; }

        .btn {
            background: #ff4d6d;
            color: white;
            border: 2px solid #fff;
            padding: 10px 25px;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 10px;
            transition: transform 0.2s;
        }
        .btn:active { transform: scale(0.9); }

        #cursor {
            position: fixed;
            width: 18px; height: 18px;
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
            will-change: transform;
        }
        @keyframes moveUp {
            0% { transform: translateY(110vh); opacity: 0; }
            100% { transform: translateY(-10vh); opacity: 0; }
        }

        .screen { display: none; width: 100%; }
        .active { display: block; }
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
                <p class="typing-text" id="type1">Zoe, aapke liye ye duniya ka sabse bada digital surprise hai...</p>
                <button class="btn" onclick="startApp()">START JOURNEY ✨</button>
            </div>
            
            <div id="dynamic-content" class="screen">
                <h1 id="dyn-h1"></h1>
                <p class="typing-text" id="dyn-p"></p>
                <button class="btn" id="dyn-btn" onclick="nextStep()">AAGE DEKHO 🌹</button>
            </div>
            
            <div id="final-page" class="screen">
                <h1>Be Mine?</h1>
                <p class="typing-text">Zoe Verma, 32 messages ke baad bas yahi puchna hai... Kya aap hamesha mere saath rahoge? ❤️</p>
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
            { h: "The Smile", p: "Aapki muskurahat dekh kar mera din ban jata hai, Miss Zoe." },
            { h: "Pure Soul", p: "Aapka dil itna saaf hai ki koi bhi aap se pyar kar baithe." },
            { h: "Dream Girl", p: "Maine sapno mein pari dekhi thi, asliyat mein aap mil gaye." },
            { h: "My Luck", p: "Main khud ko khush-naseeb samajhta hoon ki aap meri life mein ho." },
            { h: "Unique", p: "Duniya mein hazaaron hain, par 'Zoe' sirf ek hi hai." },
            { h: "Comfort", p: "Aap se baat karke aisa lagta hai jaise har tension khatam ho gayi." },
            { h: "Strength", p: "Jab aap mere saath hote ho, toh main kisi bhi mushkil se lad sakta hoon." },
            { h: "The Voice", p: "Aapki awaaz mere kaanon mein kisi music jaisa sukoon deti hai." },
            { h: "Eyes", p: "Aapki aankhon mein itni gehrai hai ki main kho jata hoon." },
            { h: "Style", p: "Aapka baat karne ka aur rehne ka andaaz ekdam alag aur pyara hai." },
            { h: "Thinking", p: "Main poore din bas ye sochta hoon ki aap kya kar rahe honge." },
            { h: "Trust", p: "Mujhe aap par poora bharosa hai, aap kabhi mera hath nahi chhodoge." },
            { h: "Special", p: "Zoe, aap mere liye mere family se kam nahi ho." },
            { h: "Laughter", p: "Aapka hansna mujhe duniya ki sabse badi khushi deta hai." },
            { h: "Admiration", p: "Main ghanton bas aapko dekh sakta hoon bina bore huye." },
            { h: "Presence", p: "Aapki maujoodgi se hi ghar aur dil dono bhare huye lagte hain." },
            { h: "Angel", p: "Bhagwan ne shayad aapko mere liye hi bheja hai." },
            { h: "Kindness", p: "Aapka doosron ki care karna mujhe bohot pasand hai." },
            { h: "Connection", p: "Humara rishta sirf baaton ka nahi, dil ka gehra rishta hai." },
            { h: "Memories", p: "Ab tak ki har ek minute jo maine aapke sath bitayi hai, wo precious hai." },
            { h: "Support", p: "Aapne mujhe tab samjha jab kisi ne nahi samjha." },
            { h: "Motivation", p: "Aapko dekh kar mujhe life mein behtar karne ki himmat milti hai." },
            { h: "Vibe", p: "Aapki energy itni positive hai ki sab positive lagne lagta hai." },
            { h: "Love", p: "Maine pyar ke baare mein suna tha, mehsoos aapke sath kiya." },
            { h: "Loyalty", p: "Rehan sirf Zoe ka hai, aur hamesha rahega." },
            { h: "Promise 1", p: "Wada hai, main aapko kabhi rone nahi doonga." },
            { h: "Promise 2", p: "Wada hai, main hamesha aapki har baat sununga." },
            { h: "Promise 3", p: "Wada hai, main har mushkil mein aapke aage khada rahunga." },
            { h: "Almost End", p: "Ab 30 pages ho chuke hain, par mera pyar abhi shuru hua hai." },
            { h: "The Queen", p: "Zoe Verma, aap mere dil ke takht ki akeli rani ho." }
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
            music.play().catch(() => {
                window.addEventListener('click', () => music.play(), {once: true});
            });
            document.getElementById('page1').style.display = 'none';
            document.getElementById('dynamic-content').style.display = 'block';
            nextStep();
        }

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
            setInterval(createHeart, 150);
        }

        function moveNoButton() {
            const btn = document.getElementById('noBtn');
            btn.style.position = 'fixed';
            btn.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            btn.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        }

        function createHeart() {
            if (document.querySelectorAll('.heart-float').length > 10) return;
            const h = document.createElement('div');
            h.className = 'heart-float';
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = (Math.random() * 15 + 10) + 'px';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
        }
        setInterval(createHeart, 1000);
        typeEffect(document.getElementById('type1'), "Zoe, aapke liye ye duniya ka sabse bada digital surprise hai...");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
