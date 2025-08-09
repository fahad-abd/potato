from flask import Flask, request
from pyngrok import ngrok

# =======================
# 1. Set Ngrok Token
# =======================
NGROK_TOKEN = "312HiqfvzTK8zNs0djzASUWb0N7_3QYdiSWYJXcsEBZH3XmJf"
ngrok.set_auth_token(NGROK_TOKEN)

# =======================
# 2. Mood → Potato → Song Mapping
# =======================
potato_data = {
    "happy": {
        "message": "You are French fries — fun, chaotic, and a crowd favorite!",
        "image": "/static/french_fries.png",
        "song": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    },
    "sad": {
        "message": "You are mashed potato — soft, warm, and impossible to dislike.",
        "image": "/static/mashed_potato.png",
        "song": "https://www.youtube.com/watch?v=RB-RcX5DS5A"
    },
    "tired": {
        "message": "You are a baked potato — reliable, cozy, and a little sleepy.",
        "image": "/static/baked_potato.png",
        "song": "https://www.youtube.com/watch?v=5qap5aO4i9A"
    },
    "angry": {
        "message": "You are a crispy burnt potato — fiery and unstoppable.",
        "image": "/static/burnt_potato.png",
        "song": "https://www.youtube.com/watch?v=3YxaaGgTQYM"
    },
    "excited": {
        "message": "You are potato chips — crispy, sassy, and ready to party!",
        "image": "/static/potato_chips.png",
        "song": "https://www.youtube.com/watch?v=fLexgOxsZu0"
    }
}

default_data = {
    "message": "You are a raw potato — mysterious and full of potential.",
    "image": "/static/raw.potato.png",
    "song": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}

# =======================
# 3. Flask App
# =======================
app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mood = request.form.get("mood", "").strip().lower()
        data = potato_data.get(mood, default_data)
        return f"""
        <html>
        <body style='text-align:center; font-family:Arial;'>
            <h1>🥔 Your Potato Personality</h1>
            <p><b>Mood:</b> {mood if mood else 'Unknown'}</p>
            <h2>{data['message']}</h2>
            <img src='{data['image']}' style='max-width:300px;'><br><br>
            <a href='{data['song']}' target='_blank'>🎵 Listen to your mood song</a>
            <br><br>
            <a href='/'>Go Back</a>
        </body>
        </html>
        """
    return """
    <html>
    <body style='text-align:center; font-family:Arial;'>
        <h1>🥔 Potato Advisor</h1>
        <form method='POST'>
            <label>How are you feeling today?</label><br><br>
            <input name='mood' placeholder='e.g. happy, sad, tired'>
            <button type='submit'>Find my potato type</button>
        </form>
    </body>
    </html>
    """

# =======================
# 4. Start server & public link
# =======================
if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
    app.run(port=5000)

