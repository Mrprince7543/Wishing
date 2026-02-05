#!/usr/bin/env python3
"""
Complete Flask Wishing Site for Termux
Run: python wishing_site.py
Access: http://localhost:5000
"""

import os
import sys
from datetime import datetime
import random

# Check if Flask is installed
try:
    from flask import Flask, render_template_string, request, redirect, url_for, jsonify
    print("✅ Flask imported successfully")
except ImportError:
    print("❌ Flask not installed. Installing...")
    os.system('pip install flask')
    from flask import Flask, render_template_string, request, redirect, url_for, jsonify

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'wishing-site-secret-key-2024'

# Sample wishes storage
wishes = []

# HTML Template with all CSS/JS
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WishCraft - Beautiful Wishing Site</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #f0f2f5; }
        
        .navbar {
            background: linear-gradient(90deg, #6a11cb, #2575fc);
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
            margin-left: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            transition: background 0.3s;
        }
        
        .nav-links a:hover {
            background: rgba(255,255,255,0.2);
        }
        
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(rgba(106,17,203,0.8), rgba(37,117,252,0.8));
            color: white;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .btn {
            display: inline-block;
            background: #ff6b6b;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 1rem;
            border: none;
            cursor: pointer;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .form-container {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin: 2rem auto;
            max-width: 600px;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #555;
        }
        
        .form-control {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .wish-card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            border-left: 5px solid #6a11cb;
        }
        
        .card-preview {
            background: white;
            border-radius: 10px;
            padding: 3rem;
            margin: 2rem auto;
            max-width: 600px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 2px dashed #6a11cb;
        }
        
        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .category {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s;
        }
        
        .category:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .footer {
            text-align: center;
            padding: 2rem;
            background: #2c3e50;
            color: white;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .nav-links { display: none; }
        }
    </style>
</head>
<body>
    {% block content %}{% endblock %}
    
    <script>
        function validateForm() {
            const sender = document.getElementById('sender');
            const receiver = document.getElementById('receiver');
            const message = document.getElementById('message');
            
            if(!sender.value.trim()) {
                alert('Please enter your name');
                sender.focus();
                return false;
            }
            
            if(!receiver.value.trim()) {
                alert('Please enter receiver name');
                receiver.focus();
                return false;
            }
            
            if(!message.value.trim()) {
                alert('Please enter your wish message');
                message.focus();
                return false;
            }
            
            return true;
        }
        
        function shareWish() {
            alert('Share this URL: ' + window.location.href);
        }
    </script>
</body>
</html>
'''

# Routes
@app.route('/')
def home():
    template = HTML_TEMPLATE.replace(
        '{% block content %}',
        '''
        <nav class="navbar">
            <div class="logo">🎉 WishCraft</div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/create">Create</a>
                <a href="/gallery">Gallery</a>
            </div>
        </nav>
        
        <section class="hero">
            <h1>Create Beautiful Wishes</h1>
            <p>Send personalized wishes for birthdays, anniversaries, festivals and special occasions</p>
            <a href="/create" class="btn">Create Your Wish</a>
        </section>
        
        <div class="container">
            <h2 style="text-align: center; margin: 2rem 0;">Popular Categories</h2>
            <div class="categories">
                <div class="category" onclick="location.href='/create?category=birthday'">
                    <h3>🎂 Birthday</h3>
                    <p>Birthday wishes with animations</p>
                </div>
                <div class="category" onclick="location.href='/create?category=anniversary'">
                    <h3>❤️ Anniversary</h3>
                    <p>Romantic wishes for couples</p>
                </div>
                <div class="category" onclick="location.href='/create?category=festival'">
                    <h3>🎉 Festival</h3>
                    <p>Diwali, Christmas, Eid wishes</p>
                </div>
                <div class="category" onclick="location.href='/create?category=thankyou'">
                    <h3>🙏 Thank You</h3>
                    <p>Express gratitude beautifully</p>
                </div>
            </div>
            
            <div style="text-align: center; margin: 3rem 0;">
                <h2>How It Works</h2>
                <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 2rem; flex-wrap: wrap;">
                    <div style="text-align: center;">
                        <div style="background: #6a11cb; color: white; width: 50px; height: 50px; line-height: 50px; border-radius: 50%; margin: 0 auto 1rem;">1</div>
                        <p>Fill details</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="background: #2575fc; color: white; width: 50px; height: 50px; line-height: 50px; border-radius: 50%; margin: 0 auto 1rem;">2</div>
                        <p>Choose design</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="background: #ff6b6b; color: white; width: 50px; height: 50px; line-height: 50px; border-radius: 50%; margin: 0 auto 1rem;">3</div>
                        <p>Share & Send</p>
                    </div>
                </div>
            </div>
        </div>
        
        <footer class="footer">
            <p>© 2024 WishCraft | Made with ❤️ for spreading happiness</p>
        </footer>
        '''
    ).replace('{% endblock %}', '')
    return render_template_string(template)

@app.route('/create')
def create():
    category = request.args.get('category', '')
    
    template = HTML_TEMPLATE.replace(
        '{% block content %}',
        f'''
        <nav class="navbar">
            <div class="logo">🎉 WishCraft</div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/create" style="background: rgba(255,255,255,0.2);">Create</a>
                <a href="/gallery">Gallery</a>
            </div>
        </nav>
        
        <div class="container">
            <h1 style="text-align: center; margin: 2rem 0;">Create Your Wish</h1>
            
            <form class="form-container" action="/preview" method="POST" onsubmit="return validateForm()">
                <div class="form-group">
                    <label>Your Name</label>
                    <input type="text" id="sender" name="sender" class="form-control" placeholder="Enter your name" required value="User">
                </div>
                
                <div class="form-group">
                    <label>Receiver's Name</label>
                    <input type="text" id="receiver" name="receiver" class="form-control" placeholder="Enter receiver's name" required value="Special Person">
                </div>
                
                <div class="form-group">
                    <label>Occasion</label>
                    <select id="category" name="category" class="form-control" required>
                        <option value="">Select occasion</option>
                        <option value="birthday" {'selected' if category == 'birthday' else ''}>🎂 Birthday</option>
                        <option value="anniversary" {'selected' if category == 'anniversary' else ''}>❤️ Anniversary</option>
                        <option value="festival" {'selected' if category == 'festival' else ''}>🎉 Festival</option>
                        <option value="thankyou" {'selected' if category == 'thankyou' else ''}>🙏 Thank You</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Your Message</label>
                    <textarea id="message" name="message" class="form-control" rows="5" placeholder="Write your heartfelt message..." required>Wishing you all the happiness in the world! May your day be filled with joy and laughter!</textarea>
                </div>
                
                <div style="text-align: center;">
                    <button type="submit" class="btn">Preview Wish</button>
                    <a href="/" style="margin-left: 1rem; color: #666;">Cancel</a>
                </div>
            </form>
        </div>
        '''
    ).replace('{% endblock %}', '')
    return render_template_string(template)

@app.route('/preview', methods=['GET', 'POST'])
def preview():
    if request.method == 'POST':
        sender = request.form.get('sender', 'Friend')
        receiver = request.form.get('receiver', 'Special Person')
        message = request.form.get('message', 'Best wishes!')
        category = request.form.get('category', 'birthday')
        
        # Store wish
        wish = {
            'id': len(wishes) + 1,
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'category': category,
            'date': datetime.now().strftime('%B %d, %Y')
        }
        wishes.append(wish)
        
        category_titles = {
            'birthday': '🎂 Happy Birthday!',
            'anniversary': '❤️ Happy Anniversary!',
            'festival': '🎉 Festival Greetings',
            'thankyou': '🙏 Thank You'
        }
        
        category_title = category_titles.get(category, '🎊 Best Wishes!')
        
        template = HTML_TEMPLATE.replace(
            '{% block content %}',
            f'''
            <nav class="navbar">
                <div class="logo">🎉 WishCraft</div>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/create">Create New</a>
                    <a href="#" onclick="shareWish()">Share</a>
                </div>
            </nav>
            
            <div class="container">
                <h1 style="text-align: center; margin: 2rem 0;">Your Wish Card</h1>
                
                <div class="card-preview">
                    <h2 style="color: #6a11cb; margin-bottom: 1rem;">{category_title}</h2>
                    <p style="color: #666; margin-bottom: 2rem;">For: <strong>{receiver}</strong></p>
                    
                    <div style="font-size: 1.2rem; line-height: 1.6; margin: 2rem 0; padding: 1rem; background: #f8f9ff; border-radius: 10px;">
                        "{message}"
                    </div>
                    
                    <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid #eee;">
                        <p>With warm wishes,</p>
                        <p style="font-weight: bold; color: #2575fc; font-size: 1.2rem;">{sender}</p>
                        <p style="color: #888; margin-top: 1rem;">{wish['date']}</p>
                    </div>
                </div>
                
                <div style="text-align: center; margin: 3rem 0;">
                    <button onclick="shareWish()" class="btn" style="background: #25D366;">Share on WhatsApp</button>
                    <a href="/create" class="btn" style="margin-left: 1rem; background: #6a11cb;">Create Another</a>
                    <a href="/gallery" class="btn" style="margin-left: 1rem; background: #ff6b6b;">View Gallery</a>
                </div>
            </div>
            '''
        ).replace('{% endblock %}', '')
        return render_template_string(template)
    
    return redirect('/create')

@app.route('/gallery')
def gallery():
    wish_cards = ''
    for wish in wishes[-10:]:
        wish_cards += f'''
        <div class="wish-card">
            <h3>{wish["category"].title()} Wish</h3>
            <p>"{wish["message"][:100]}{"..." if len(wish["message"]) > 100 else ""}"</p>
            <div style="display: flex; justify-content: space-between; color: #888; margin-top: 1rem;">
                <span>From: {wish["sender"]}</span>
                <span>{wish["date"]}</span>
            </div>
        </div>
        '''
    
    if not wish_cards:
        wish_cards = '''
        <div class="wish-card">
            <h3>🎂 Birthday Wish</h3>
            <p>"Happy Birthday! May your day be filled with joy and happiness!"</p>
            <div style="display: flex; justify-content: space-between; color: #888; margin-top: 1rem;">
                <span>From: User</span>
                <span>Today</span>
            </div>
        </div>
        '''
    
    template = HTML_TEMPLATE.replace(
        '{% block content %}',
        f'''
        <nav class="navbar">
            <div class="logo">🎉 WishCraft</div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/create">Create</a>
                <a href="/gallery" style="background: rgba(255,255,255,0.2);">Gallery</a>
            </div>
        </nav>
        
        <div class="container">
            <h1 style="text-align: center; margin: 2rem 0;">Wish Gallery</h1>
            <p style="text-align: center; color: #666; margin-bottom: 2rem;">
                Total Wishes Created: {len(wishes) + 1}
            </p>
            
            {wish_cards}
            
            <div style="text-align: center; margin: 3rem 0;">
                <a href="/create" class="btn">Create Your Wish</a>
            </div>
        </div>
        '''
    ).replace('{% endblock %}', '')
    return render_template_string(template)

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'wishes': len(wishes)})

# Run the app
if __name__ == '__main__':
    print("🚀 Starting WishCraft on Termux...")
    print("🌐 Local: http://localhost:5000")
    print("📱 Mobile: Connect to same WiFi and use your IP:5000")
    print("📂 Routes: /, /create, /preview, /gallery, /health")
    print("⏳ Starting server...")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False  # Set to True for development
    )
