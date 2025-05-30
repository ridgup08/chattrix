import google.generativeai as genai

# ✅ Replace with your API key from https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyAz2Tb7Rz_hqBGS-BeNHUDYAJaPA-iX4XU")

# Load the Gemini Pro model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")




# Start a new chat session
chat = model.start_chat()

print("Chattrix: what’s good, ready to chat? Type 'bye' to bounce.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chattrix: see ya!")
        break

    try:
        response = chat.send_message(user_input)
        print("Chattrix:", response.text.strip())
    except Exception as e:
        print("Chattrix: uh oh 💀 something broke")
        print("Error:", e)
