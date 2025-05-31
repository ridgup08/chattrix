# 💬 Chattrix

**Chattrix** is a Gen-Z inspired AI chatbot built with Python, Flask, and Google's Gemini 1.5 Flash.  
It’s fast, casual, and designed to help students chill and vibe when life gets overwhelming.

🌐 [Live Site](https://chattrix-8b8a.onrender.com)

---

### 🚀 Features
- Real-time chatbot powered by Gemini 1.5 Flash
- Animated typing indicator (`🤖...`)
- Mobile responsive UI with bubble chat design
- Send messages via Enter key or button
- Hosted on [Render](https://render.com)

---

### 📁 Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- AI Model: Google Gemini
- Hosting: Render
- Version Control: Git + GitHub

---

### 👩‍💻 About Me
Hi! I’m Ridhima Gupta — a computer engineering student who builds fun projects like this for real-world impact.  
Want to collab? [Email me](mailto:your.email@example.com) or connect on [LinkedIn](https://www.linkedin.com/in/your-profile)

---

### 📎 Resume
[Download my resume](resume.pdf)

---

## 🛠️ Build & Run Locally

Follow these steps to run Chattrix on your own machine:

### 1. Clone the Repository
```bash
git clone https://github.com/ridgup08/chattrix.git
cd chattrix
```

### 2. Set Up a Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# OR
source venv/bin/activate  # on Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Your Gemini API Key

You need a Google Gemini API key from [makersuite.google.com](https://makersuite.google.com). Then set it:

**On Windows (PowerShell):**
```bash
$env:GOOGLE_API_KEY = "your_api_key_here"
```

**On Mac/Linux:**
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 5. Run the Flask App
```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser 🚀
