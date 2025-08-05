from flask import Flask, render_template, request
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "Kimi Chat",
        },
        json={
            "model": "moonshotai/kimi-k2:free",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        }
    )
    
    if response.status_code == 200:
        assistant_response = response.json()['choices'][0]['message']['content']
    else:
        assistant_response = "Sorry, I couldn't process your request at this time."

    return render_template('response.html', response=assistant_response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
