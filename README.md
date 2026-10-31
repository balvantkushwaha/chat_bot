# ✨ Groq AI Chatbot

An AI-powered chatbot built using **Python and Groq API**. This project provides a simple, clean, and responsive chat interface where users can ask questions, explore ideas, and receive AI-generated responses.

🌐 **Live Website:** https://chat-bot-r524.onrender.com/

## 🚀 Features

- 🤖 AI-powered conversational responses using Groq API.
- 💬 Interactive and user-friendly chat interface.
- 🆕 Start a new conversation with the New Chat option.
- 🕒 Recent chats section for accessing previous conversations.
- 📱 Responsive design for desktop and mobile devices.
- ⚡ Fast AI responses powered by Groq.
- ☁️ Live deployment using Render.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Groq API | AI-powered responses |
| Django / Flask | Backend Framework |
| HTML5 | Web Structure |
| CSS3 | Styling and Responsive Design |
| JavaScript | Frontend Interactions |
| Gunicorn | Production WSGI Server |
| Render | Deployment Platform |

## 📸 Project Preview

Visit the live application to explore the chatbot:

👉 https://chat-bot-r524.onrender.com/

## 📁 Project Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=django-insecure-riznemfqq83
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Get your API key from the official Groq Console:

https://console.groq.com/keys

**Important:** Never share your API key or upload your `.env` file to GitHub.

Add the following to your `.gitignore` file:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

### 5. Run the Application

Use the command according to your backend framework.

**For Django:**

```bash
python manage.py migrate
python manage.py runserver
```

**For Flask:**

```bash
python app.py
```

Open the local development URL in your browser.

## ☁️ Deployment

This project is deployed on **Render**.

Deployment steps:

1. Push the project code to GitHub.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Configure the build and start commands.
5. Add `GROQ_API_KEY` under Render Environment Variables.
6. Deploy your application.

**Example Gunicorn commands:**

For Flask:

```bash
gunicorn app:app
```

For Django:

```bash
gunicorn core.wsgi:application
```

Replace `core` with your actual Django project package name.

## 🔐 Security

- Store API keys securely using environment variables.
- Never commit `.env` files or private credentials.
- Keep sensitive configuration out of public repositories.
- Verify AI-generated information before relying on it.

## 👨‍💻 Developer

**Balvant Kushwaha**

Full Stack Developer | MERN Stack | Python | AI Enthusiast

- GitHub: https://github.com/balvantkushwaha

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with ❤️ by Balvant Kushwaha**
