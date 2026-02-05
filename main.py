from flask import Flask, render_template_string

app = Flask(__name__)

# Yahan humne HTML ko ek string mein daal diya hai
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valentine's Surprise</title>
    <style>
        body {
            margin: 0;
            background: #1a1a1a;
            color: #fff;
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            text-align: center;
        }
        .container {
            padding: 20px;
            border: 2px solid #ff4d6d;
            border-radius: 15px;
            background: rgba(255, 77, 109, 0.1);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px rgba(255, 77, 109, 0.5);
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            color: #ff4d6d;
            text-shadow: 0 0 10px #ff4d6d;
        }
        p {
            font-size: 1.5rem;
            color: #ffb3c1;
        }
        .heart {
            font-size: 80px;
            color: #ff4d6d;
            animation: beat 1s infinite alternate;
        }
        @keyframes beat {
            from { transform: scale(1); }
            to { transform: scale(1.2); }
        }
        .floating-heart {
            position: absolute;
            bottom: -50px;
            color: #ff4d6d;
            opacity: 0.6;
            animation: float 4s linear infinite;
        }
        @keyframes float {
            to { transform: translateY(-110vh) rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤</div>
        <h1>Happy Valentine's Day!</h1>
        <p>You make my world much brighter ✨</p>
    </div>

    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('floating-heart');
            heart.innerHTML = '❤️';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.fontSize = Math.random() * 20 + 20 + 'px';
            heart.style.animationDuration = Math.random() * 2 + 3 + 's';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 5000);
        }
        setInterval(createHeart, 200);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Host and Port settings as requested
    app.run(host='0.0.0.0', port=5000)
