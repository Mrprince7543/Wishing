from flask import Flask, render_template_string

app = Flask(__name__)

# REHAN LOVES ZOE - 75-PAGE DARK MEGA EDITION (WITH RANDOM SONG)
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

        .particle {
            position: absolute;
            pointer-events: none;
            animation: moveUp 7s linear forwards;
            z-index: 1;
            will-change: transform, opacity;
        }

        @keyframes moveUp {
            0% { transform: translateY(110vh) scale(0.3); opacity: 0; }
            20% { opacity: 0.6; }
            100% { transform: translateY(-20vh) scale(1.2); opacity: 0; }
        }

        .top-title {
            font-family: 'Dancing Script', cursive;
            font-size: 2.8rem;
            color: #ff4d6d;
            text-align: center;
            margin-bottom: 10px;
            text-shadow: 0 0 15px #ff4d6d, 0 0 30px #ff0055;
            z-index: 20;
        }

        .header-box {
            background: rgba(255, 77, 109, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px 40px;
            border-radius: 50px;
            margin-bottom: 15px;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.3);
            z-index: 20;
        }
        .header-box h2 { 
            font-family: 'Orbitron', sans-serif;
            font-size: 1.4rem; 
            color: #fff; 
            letter-spacing: 4px; 
            text-transform: uppercase;
            text-shadow: 0 0 10px #ff4d6d;
        }

        .love-card {
            position: relative;
            width: 100%;
            max-width: 550px;
            height: 480px;
            border-radius: 35px;
            z-index: 5;
            border: 2px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 0 50px rgba(255, 77, 109, 0.4);
            background: url('https://i.ibb.co/1YTf7R36/FB-IMG-16249452197243361.jpg') center/cover no-repeat;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .glass-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(2px);
            z-index: 1;
        }

        .content-inner { position: relative; z-index: 2; width: 90%; text-align: center; }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4.5rem;
            color: #ff4d6d;
            margin-bottom: 15px;
            text-shadow: 0 0 20px rgba(255, 77, 109, 0.8);
        }

        .typing-text {
            font-size: 1.6rem;
            color: #fff;
            font-weight: 700;
            min-height: 120px;
            line-height: 1.4;
            text-shadow: 0 0 10px rgba(0,0,0,0.5);
        }

        .footer-box {
            margin-top: 20px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 15px 45px;
            border-radius: 60px;
            border: 1px solid #ff4d6d;
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.5);
            z-index: 20;
        }
        .footer-box p { font-weight: 800; color: #fff; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px;}

        .btn {
            background: #ff4d6d;
            color: #fff;
            border: none;
            padding: 16px 40px;
            border-radius: 50px;
            font-size: 1.2rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 20px;
            box-shadow: 0 0 15px #ff4d6d;
            transition: 0.3s;
        }
        .btn:hover { transform: scale(1.1); box-shadow: 0 0 25px #ff4d6d; }

        #cursor {
            position: fixed;
            width: 25px; height: 25px;
            background: #ff4d6d;
            clip-path: path('M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z');
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            filter: drop-shadow(0 0 10px #ff4d6d);
        }

        .screen { display: none; width: 100%; }
        .active { display: block; animation: fadeEffect 0.6s ease-in; }
        @keyframes fadeEffect { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
    </style>
</head>
<body>

    <div id="cursor"></div>
    <audio id="bgMusic" loop preload="auto"></audio>

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

    <div class="footer-box"><p>💖 I LOVE YOU ZOE VERMA FOREVER 💖</p></div>

    <script>
        const cursor = document.getElementById('cursor');
        const music = document.getElementById('bgMusic');
        let currentPage = 0;

        // Random Music List
        const musicList = [
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", // Example Slot
            "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tanishk_Bagchi/Raataan_Lambiyan.mp3",
            "https://www.pagalworld.com.sb/files/download/id/64630" // Kesariya (Just an example URL)
        ];

        const story = [
            { h: "The Start", p: "Humari kahani meri zindagi ka sabse khoobsurat hissa hai." },
            { h: "The Smile", p: "Aapki muskurahat dekh kar mera din ban jata hai, Miss Zoe." },
            { h: "Pure Soul", p: "Aapka dil itna saaf hai ki koi bhi aap se pyar kar baithe." },
            { h: "Dream Girl", p: "Maine sapno mein pari dekhi thi, asliyat mein aap mil gaye." },
            { h: "Unique", p: "Duniya mein hazaaron hain, par 'Zoe' sirf ek hi hai." },
            { h: "The Voice", p: "Aapki awaaz mere kaanon mein sukoon deti hai." },
            { h: "My World", p: "Maine apni duniya aapke charon taraf basayi hai." },
            { h: "Pure Love", p: "Mera pyar koi dikhava nahi, meri rooh ki sacchai hai." },
            { h: "Heartbeat", p: "Meri har dharkan bas aapka hi naam leti hai." },
            { h: "Sunshine", p: "Aap mere mausam ki pehli dhoop ho." },
            { h: "Soulmate", p: "Hum do jism magar ek jaan hain, Zoe." },
            { h: "The Queen", p: "Aap mere dil ke takht ki akeli malkin ho." },
            { h: "Priority", p: "Duniya ek taraf, aur mere liye aap hamesha pehle rahoge." },
            { h: "Home", p: "Ghar diwaron se nahi, aapke ehsaas se banta hai." },
            { h: "Loyalty", p: "Rehan sirf Zoe ka hai, aur hamesha rahega." },
            { h: "Blessing", p: "Upar wale ka sabse bada shukrana ki aap meri ho." },
            { h: "Safe Place", p: "Aapki bahon mein mujhe sabse zyada sukoon milta hai." },
            { h: "Forever", p: "Ye safar kabhi khatam nahi hoga, ye anant hai." },
            { h: "Beauty", p: "Aapki khoobsurti sirat aur surat dono mein hai." },
            { h: "Patience", p: "Aapka intezaar mere liye ibadat hai." },
            { h: "Healing", p: "Aapke ek message se mere saare zakhm bhar jate hain." },
            { h: "Wada", p: "Main hamesha aapka hath tham kar chalunga." },
            { h: "Stars", p: "Aasman ke sitaron se zyada chamak aapki aankhon mein hai." },
            { h: "Moonlight", p: "Andheri raaton mein aap meri chandni ho." },
            { h: "Breath", p: "Aap meri saans lene ki wajah ho." },
            { h: "Laughter", p: "Aapki hansi meri favourite dhun hai." },
            { h: "Pride", p: "Mujhe fakhr hai ki aap meri life mein ho." },
            { h: "Magic", p: "Aapki baaton mein ek alag hi jaadu hai." },
            { h: "Care", p: "Aapka mera khayal rakhna mujhe bohot achha lagta hai." },
            { h: "Gift", p: "Aap meri zindagi ka sabse bada tohfa ho." },
            { h: "Partner", p: "Aap meri best friend aur partner dono ho." },
            { h: "Deep Love", p: "Main aapko har guzarte din ke sath aur zyada chahne laga hoon." },
            { h: "Universe", p: "Meri puri kainaat aap mein samayi hai." },
            { h: "Truth", p: "Mera pyar aapke liye saccha aur pak hai." },
            { h: "Dreamer", p: "Main humesha humare sath hone ke sapne dekhta hoon." },
            { h: "Anchor", p: "Mushkil waqt mein aapne mujhe sambhala hai." },
            { h: "Passion", p: "Aapke liye mera junoon kabhi kam nahi hoga." },
            { h: "Sweetness", p: "Aapki mithaas ne meri zindagi me shahad ghol diya hai." },
            { h: "Galaxy", p: "Aap meri galaxy ka sabse chamkta sitara ho." },
            { h: "Treasure", p: "Aap mere dil ka sabse keemti khazana ho." },
            { h: "Rain", p: "Garmi ki pehli baarish jaisi thandak ho aap." },
            { h: "Light", p: "Aapne mere andhere raste ko roshan kiya hai." },
            { h: "Strength", p: "Meri himmat aur meri takat aap hi ho." },
            { h: "Inspiration", p: "Aapko dekh kar mujhe behtar banne ki umeed milti hai." },
            { h: "Destiny", p: "Humara milna likha hua tha." },
            { h: "Angel", p: "Duniya ki is bheed mein aap ek farishta ho." },
            { h: "Promise", p: "Main kabhi aapka dil nahi dukhane ka wada karta hoon." },
            { h: "Happiness", p: "Meri asli khushi aapki muskurahat mein hai." },
            { h: "Devotion", p: "Main aapka hoon aur sirf aapka rahunga." },
            { h: "The Best", p: "Aap duniya ki sabse behtareen ladki ho." },
            { h: "Belonging", p: "Mera har ek lamha aapke naam hai." },
            { h: "Serenity", p: "Aapke sath bitaya har pal sukoon deta hai." },
            { h: "Gravity", p: "Aapka pyar mujhe humesha khench lata hai." },
            { h: "Symphony", p: "Humara rishta ek khoobsurat geet jaisa hai." },
            { h: "Reflection", p: "Main aap mein khud ko dekhta hoon." },
            { h: "Infinite", p: "Hamara pyar samandar ki gehrai se zyada hai." },
            { h: "Support", p: "Main hamesha aapke piche khada rahunga." },
            { h: "Adore", p: "Main aapko had se zyada adore karta hoon." },
            { h: "Vision", p: "Mera har kal aapke bina adhura hai." },
            { h: "Obsession", p: "Main aapke pyar mein giraftar hoon." },
            { h: "Warmth", p: "Sardi ki dhoop jaisi garmahat ho aap." },
            { h: "Unconditional", p: "Mera pyar bina kisi shart ke hai." },
            { h: "Harmony", p: "Aapke aane se meri life balance ho gayi." },
            { h: "Spark", p: "Humare beech ki wo chingari hamesha rahegi." },
            { h: "Faith", p: "Mujhe hum par pura yakeen hai." },
            { h: "Eternity", p: "Janmo janmo tak aapka sath chahiye." },
            { h: "Vibe", p: "Aapki vibe ekdam match karti hai mujhse." },
            { h: "Smile Again", p: "Aapki ek smile ke liye main kuch bhi kar sakta hoon." },
            { h: "One & Only", p: "Zindagi ki is race mein sirf aap meri winner ho." },
            { h: "Commitment", p: "Main sirf aapka rehne ka faisla kar chuka hoon." },
            { h: "Beautiful Zoe", p: "Aap meri sabse sundar haqeeqat ho." },
            { h: "My Everything", p: "Aap meri har khushi, har dua, har tamanna ho." },
            { h: "The Ending", p: "75 baatein khatam hui, magar pyar abhi shuru hua hai." }
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
            // Pick a random song from the list
            const randomSong = musicList[Math.floor(Math.random() * musicList.length)];
            music.src = randomSong;
            music.play().catch(() => { 
                console.log("Autoplay blocked, waiting for interaction.");
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
            p.style.color = symbol === '❤️' ? '#ff4d6d' : (symbol === '★' ? '#ffea00' : '#fff');
            document.body.appendChild(p);
            setTimeout(() => p.remove(), 7000);
        }

        setInterval(() => {
            createParticle('❤️');
            createParticle('★');
            createParticle('○');
        }, 350);

        typeEffect(document.getElementById('type1'), "Aapke liye ye 75 pages ka sabse lamba aur pyara surprise taiyar hai... Ready?");
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
