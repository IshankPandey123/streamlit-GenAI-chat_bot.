💬 Generative AI Chatbot

A conversational AI chatbot built using Python, Streamlit, LangChain, and Google Gemini. The chatbot provides real-time AI responses and maintains conversation history using Streamlit session state.

🚀 Features
🤖 Google Gemini-powered responses
💬 Interactive Streamlit chat interface
🧠 Maintains conversation history
🔗 Built using LangChain
🔐 API key managed securely using .env
⚡ Fast and simple chatbot experience
🛠️ Tech Stack
Python
Streamlit
LangChain
Google Gemini
python-dotenv
📁 Project Structure
GenAI/
│
├── chatbot.py
├── requirements.txt
├── .env
└── README.md
⚙️ Installation
1. Clone the repository
git clone <your-repository-url>
cd GenAI
2. Create a virtual environment
python3 -m venv venv

Activate it:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Add your Gemini API key

Create a .env file:

GEMINI_API_KEY="your_api_key_here"
5. Run the application
python -m streamlit run chatbot.py

The application will open at:

http://localhost:8501
🧠 How It Works
User Input
    ↓
Streamlit Chat UI
    ↓
Chat History
    ↓
LangChain
    ↓
Google Gemini
    ↓
AI Response
    ↓
Display + Save Response
📌 Future Improvements
Add streaming responses
Add multiple chatbot personalities
Add document/RAG support
Add conversation export
Deploy the chatbot to Streamlit Cloud
👨‍💻 Author

Ishank Pandey