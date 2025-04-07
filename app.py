from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get Gemini API Key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY not found in environment!")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini 1.5 Pro model
model = genai.GenerativeModel("gemini-1.5-pro")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        print("Received:", user_message)
        response = model.generate_content(user_message)
        print("Raw Response:", response)
        bot_reply = response.text.strip()
    except Exception as e:
        print("Gemini API Error:", e)
        bot_reply = "Sorry, something went wrong. Try again later."

    return jsonify({'reply': bot_reply})


if __name__ == '__main__':
    app.run(debug=True)
