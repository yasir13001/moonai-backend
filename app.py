from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_cors import CORS

import requests
import os

app = Flask(__name__)
CORS(app, origins=["https://www.themoonai.org"]) 

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

limiter = Limiter(app, key_func=get_remote_address)
@limiter.limit("20 per minute")


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
