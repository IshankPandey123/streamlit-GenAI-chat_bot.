# 💬 Generative AI Chatbot

A simple and interactive **Generative AI chatbot** built with **Python, Streamlit, LangChain, and Google Gemini**.

The application provides real-time AI-powered responses through a conversational chat interface and maintains conversation history using **Streamlit Session State**.

---

## 🚀 Features

* 🤖 **Google Gemini-powered AI responses**
* 💬 Interactive **Streamlit chat interface**
* 🧠 Maintains **conversation history**
* 🔗 Uses **LangChain** for LLM integration
* 🔐 Secure API key management using `.env`
* ⚡ Fast and lightweight application
* 🖥️ Simple and user-friendly interface
* 🐍 Built completely with Python

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 🎨 Streamlit     | Web-based chat interface        |
| 🔗 LangChain     | LLM application framework       |
| 🤖 Google Gemini | Generative AI model             |
| 🔐 python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
GenAI/
│
├── chatbot.py          # Main Streamlit chatbot application
├── requirements.txt    # Python dependencies
├── .env                # API key configuration
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd GenAI
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Gemini API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY="your_api_key_here"
```

> ⚠️ **Important:** Never commit your `.env` file or expose your API key publicly.

Make sure `.env` is included in your `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

---

### 5️⃣ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run chatbot.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🧠 How It Works

The chatbot follows a simple conversational pipeline:

```text
        👤 User Input
              │
              ▼
      💬 Streamlit Chat UI
              │
              ▼
       🧠 Chat History
              │
              ▼
         🔗 LangChain
              │
              ▼
       🤖 Google Gemini
              │
              ▼
        💡 AI Response
              │
              ▼
       💬 Display Response
              │
              ▼
     🧠 Save to Chat History
```

### Conversation Flow

1. The user enters a message through the Streamlit chat interface.
2. The message is stored in the conversation history.
3. LangChain passes the conversation to Google Gemini.
4. Gemini generates an AI response.
5. The response is displayed in the chat interface.
6. The conversation is maintained using Streamlit's session state.

---

## 🖥️ Application Preview

> 📸 Add a screenshot or GIF of your chatbot here.

```text
screenshots/
└── chatbot.png
```

You can display it in your README using:

```markdown
![Generative AI Chatbot](screenshots/chatbot.png)
```

---

## 📦 Requirements

The project dependencies are defined in `requirements.txt`.

Example:

```text
streamlit
langchain
langchain-google-genai
python-dotenv
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

The application uses environment variables to securely store the Gemini API key.

| Variable         | Description           |
| ---------------- | --------------------- |
| `GEMINI_API_KEY` | Google Gemini API key |

Example:

```env
GEMINI_API_KEY="your_api_key_here"
```

---

## 🚧 Future Improvements

The project can be extended with several advanced features:

* 🌊 Add **streaming AI responses**
* 🎭 Add **multiple chatbot personalities**
* 📄 Implement **Document Q&A / RAG**
* 💾 Add persistent conversation storage
* 📥 Add **conversation export**
* 🗂️ Support multiple conversations
* 🎙️ Add voice input/output
* 🌐 Deploy using **Streamlit Cloud**
* 🔐 Add improved authentication and security
* 📊 Add chatbot usage analytics

---

## 🎯 Learning Outcomes

This project demonstrates the fundamentals of building a modern Generative AI application, including:

* Working with **Large Language Models (LLMs)**
* Integrating **Google Gemini APIs**
* Using **LangChain**
* Building AI applications with **Streamlit**
* Managing conversation state
* Handling API keys securely
* Creating an interactive chatbot interface

---

## 👨‍💻 Author

### Ishank Pandey

Computer Science / B.Tech Student
Interested in **Generative AI, Machine Learning, and Software Development**.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is intended for **educational and learning purposes**.
