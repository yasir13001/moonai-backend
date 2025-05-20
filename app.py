from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_cors import CORS
from flask_limiter.util import get_remote_address
import requests
import os



app = Flask(__name__)
CORS(app, origins=["https://www.themoonai.org"]) 

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)


@app.route("/gemini", methods=["POST"])
@limiter.limit("20 per minute")

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
