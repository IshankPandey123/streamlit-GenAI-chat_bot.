from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="💬 Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.0,
)

# Chat input
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    response = llm.invoke(
        [
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.content[0]["text"]

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_response)