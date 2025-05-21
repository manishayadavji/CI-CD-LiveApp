
from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Stay positive, work hard, make it happen.",
    "Success is not for the lazy.",
    "Push yourself, no one else will do it for you.",
    "Don't stop until you're proud."
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)

