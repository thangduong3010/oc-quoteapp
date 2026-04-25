from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

quotes = os.getenv("QUOTES", "OpenShift is awesome|Tekton rocks|VMs and containers together").split("|")

@app.route("/")
def index():
    return f"<h1>{random.choice(quotes)}</h1>"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
