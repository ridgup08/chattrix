from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Get API key from environment variable
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
chat = model.start_chat()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json.get("message")
    print(f"[Chattrix received]: {user_input}")

    try:
        prompt = f"You are Chattrix, a casual and helpful chatbot. Keep your responses short, clear, and to the point. Use minimal slang or emojis. Speak like a smart friend.\nUser: {user_input}"
        response = chat.send_message(prompt)
        reply_text = getattr(response, 'text', '').strip() or "Sorry, I spaced out 😵‍💫"
        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"reply": "uh oh 💀 something broke", "error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
