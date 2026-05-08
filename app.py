from flask import Flask, render_template
from utils.generate import generate_face

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():

    generate_face()

    return {
        "image": "/static/generated/output.png"
    }

if __name__ == "__main__":
    app.run(debug=True)