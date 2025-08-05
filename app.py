from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

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
    app.run(debug=True)
