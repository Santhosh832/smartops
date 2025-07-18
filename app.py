from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import openai
from log_reader import read_logs

load_dotenv()
print("API Key loaded:", os.getenv("OPENAI_API_KEY"))

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/analyze')
def analyze_logs():
    logs = read_logs()
    result = "⚠️ OpenAI API quota exceeded. Here's a mock response: Check for 500 errors, DB connection issues, or misconfigured services."

    return jsonify({"logs": logs, "analysis": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

