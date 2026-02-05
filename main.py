from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Miss Zoe ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            color: white;
            font-family: 'Poppins', sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1000px;
        }

        #app-container {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background 1s ease;
        }

        .slide {
            display: none;
            text-align: center;
            padding: 30px;
            max-width: 600px;
            animation: zoomIn 0.8s ease-out forwards;
        }

        .slide.active { display: block; }

        @keyframes zoomIn {
            from { opacity: 0; transform: scale(0.5) rotate(-5deg); }
            to { opacity: 1; transform: scale(1) rotate(0deg); }
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 3.2rem;
            color: #ff4d6d;
            margin-bottom: 20px;
            text-shadow: 0 0 15px rgba(255, 77, 109, 0.8);
        }

        p { font-size: 1.4rem; line-height: 1.6; color: #fff; margin-bottom: 30px; }

        .btn-container {
            position: fixed;
            bottom: 50px;
            display: flex;
            gap: 20px;
        }

        .btn {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(5px);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 10px 25px;
            border-radius: 30px;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn:hover { background: #ff4d6d; border-color: #ff4d6d; }

        .progress {
            position: fixed;
            top: 20px;
            font-size: 0.9rem;
            color: #ffb3c1;
        }

        /* Floating Hearts Animation */
        .heart {
            position: absolute;
            pointer-events: none;
            animation: float Up 4s linear forwards;
            z-index: -1;
        }

        @keyframes floatUp {
            0% { transform: translateY(110vh) scale(0); opacity: 1; }
            100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
        }
    </style>
</head>
<body id="body-bg">

    <div class="progress" id="counter">1 / 20</div>

    <div id="app-container">
        </div>

    <div class="btn-container">
        <button class="btn" onclick="prevSlide()">Piche</button>
        <button class="btn" onclick="nextSlide()">Aage</button>
    </div>

    <script>
        // 20 Pages ka Data - Aap yahan text change kar sakte hain
        const slides = [
            { title: "Hi Miss Zoe", text: "Aapke liye ek chota sa surprise...", color: "#1a1a2e" },
            { title: "Page 2", text: "Aapki smile duniya ki sabse pyari cheez hai.", color: "#16213e" },
            { title: "Page 3", text: "Har din aapka intezar rehta hai.", color: "#0f3460" },
            { title: "Page 4", text: "Aapki aankhon mein alag hi chamak hai.", color: "#533483" },
            { title: "Page 5", text: "Valentine's Day toh bas ek bahana hai.", color: "#903749" },
            { title: "Page 6", text: "Asli maqsad toh aapko khush dekhna hai.", color: "#4b5d67" },
            { title: "Page 7", text: "Aap meri life ki sabse khoobsurat shayari ho.", color: "#2d4059" },
            { title: "Page 8", text: "Dua hai ki aap hamesha hasti raho.", color: "#6a0572" },
            { title: "Page 9", text: "Zindagi me aap aaye, baki sab bhul gaye.", color: "#ab83a1" },
            { title: "Page 10", text: "Adha safar tay kar liya humne!", color: "#212121" },
            { title: "Page 11", text: "Aapka style sabse alag hai.", color: "#322f3d" },
            { title: "Page 12", text: "Kya aapko pata hai aap kitni special ho?", color: "#45046a" },
            { title: "Page 13", text: "Mere har message ki wajah aap ho.", color: "#5c2a9d" },
            { title: "Page 14", text: "Khuda kare humari dosti hamesha rahe.", color: "#b5076b" },
            { title: "Page 15", text: "Valentine's ki raunak aap se hi hai.", color: "#303481" },
            { title: "Page 16", text: "Bas kuch der aur, dil ki baat aane wali hai.", color: "#111d5e" },
            { title: "Page 17", text: "Aapki baatein sukoon deti hain.", color: "#c70039" },
            { title: "Page 18", text: "Miss Zoe, aap sach mein unique ho.", color: "#900c3f" },
            { title: "Page 19", text: "Final surprise ke liye taiyar?", color: "#581845" },
            { title: "Page 20", text: "Happy Valentine's Day! Will you be mine forever? ❤️", color: "#ff4d6d" }
        ];

        let currentSlide = 0;

        function renderSlide() {
            const container = document.getElementById('app-container');
            const data = slides[currentSlide];
            
            container.innerHTML = `
                <div class="slide active">
                    <h1>${data.title}</h1>
                    <p>${data.text}</p>
                    <div style="font-size: 50px;">❤️</div>
                </div>
            `;
            
            document.body.style.background = data.color;
            document.getElementById('counter').innerText = `${currentSlide + 1} / ${slides.length}`;
        }

        function nextSlide() {
            if (currentSlide < slides.length - 1) {
                currentSlide++;
                renderSlide();
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                renderSlide();
            }
        }

        // Heart Animation Logic
        function createHeart() {
            const h = document.createElement('div');
            h.classList.add('heart');
            h.innerHTML = '❤️';
            h.style.left = Math.random() * 100 + 'vw';
            h.style.fontSize = Math.random() * 30 + 10 + 'px';
            h.style.animationDuration = Math.random() * 2 + 3 + 's';
            h.style.opacity = Math.random();
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4000);
        }

        setInterval(createHeart, 200);
        renderSlide(); // Initial call
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
