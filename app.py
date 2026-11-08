
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Happy Diwali - Kinkar</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body {
    margin: 0;
    min-height: 100vh;
    background: radial-gradient(circle, #702000, #170500);
    color: #ffd700;
    font-family: Georgia, serif;
    text-align: center;
    overflow-x: hidden;
}

.container {
    padding: 80px 15px 40px;
}

h1 {
    font-size: 42px;
    text-shadow: 0 0 20px orange;
}

h2 {
    color: #fff0b0;
}

.message {
    font-size: 21px;
    line-height: 1.7;
    margin: 25px auto;
    max-width: 600px;
}

.diyas {
    font-size: 55px;
    animation: glow 1s infinite alternate;
}

.lights {
    font-size: 30px;
    margin: 20px;
    animation: glow 0.8s infinite alternate;
}

button {
    background: #ffd700;
    color: #701900;
    border: none;
    padding: 15px 25px;
    border-radius: 30px;
    font-size: 17px;
    cursor: pointer;
}

@keyframes glow {
    from { text-shadow: 0 0 5px orange; }
    to { text-shadow: 0 0 30px yellow, 0 0 50px orange; }
}

.star {
    position: fixed;
    color: gold;
    animation: sparkle 3s infinite;
    pointer-events: none;
}

@keyframes sparkle {
    0% { opacity: 0; transform: translateY(0); }
    50% { opacity: 1; }
    100% { opacity: 0; transform: translateY(-100px); }
}
</style>
</head>

<body>

<div class="lights">✨ 🪔 ✨ 🪔 ✨</div>

<div class="container">

<div class="diyas">🪔 🪔 🪔</div>

<h1>Happy Deepawali!</h1>

<h2>Wishing You a Festival Full of Light</h2>

<div class="message">
May this Diwali bring happiness, love,<br>
peace and prosperity into your life.<br><br>
May every diya brighten your life<br>
and every moment bring a new smile.Ar abar ekbar amar torof theke shuba Deepawali!<br>
</div>

<h2>With Love,</h2>
<h1>Kinkar ❤️</h1>

<div class="diyas">🪔 ✨ 🪔</div>

<br>

<button onclick="document.getElementById('music').play()">
🎵 Play Diwali Music
</button>

<audio id="music" loop>
<source src="/static/diwali.mp3" type="audio/mpeg">
</audio>

</div>

<script>
for(let i = 0; i < 25; i++) {
    let star = document.createElement("div");
    star.className = "star";
    star.innerHTML = "✨";
    star.style.left = Math.random() * 100 + "vw";
    star.style.top = Math.random() * 100 + "vh";
    star.style.animationDelay = Math.random() * 3 + "s";
    document.body.appendChild(star);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
