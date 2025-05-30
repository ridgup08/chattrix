from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API Key from Google AI Studio
genai.configure(api_key="AIzaSyAz2Tb7Rz_hqBGS-BeNHUDYAJaPA-iX4XU")

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

        # Safely get reply text
        reply_text = getattr(response, 'text', '').strip() or "Sorry, I spaced out 😵‍💫"

        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"reply": "uh oh 💀 something broke", "error": str(e)})



if __name__ == "__main__":
    app.run(debug=True)

