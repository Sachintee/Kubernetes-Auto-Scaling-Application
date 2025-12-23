from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Kubernetes Auto Scaling App 🚀"

@app.route("/load")
def load():
    for _ in range(10_000_000):
        pass
    return "Load Generated!"

app.run(host="0.0.0.0", port=5000)