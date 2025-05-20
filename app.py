from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route("/gemini", methods=["POST"])
def gemini_proxy():
    prompt = request.json.get("prompt")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(url, json=payload)
    return jsonify(response.json())
