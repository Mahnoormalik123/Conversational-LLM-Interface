import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define roles with system instructions
ROLES = {
    "Professional Assistant": "You are a professional assistant. Explain things clearly, concisely, and in a formal way.",
    "Creative Companion": "You are a creative and fun companion. Use imagination and a friendly tone to explain things.",
    "Technical Expert": "You are a technical expert. Provide detailed, accurate, and technical explanations."
}

# Streamlit UI
st.set_page_config(page_title="Gemini Chat App", page_icon="🤖", layout="centered")

st.title("🤖 Gemini Chat App")
st.write("Select a role and start chatting with Gemini!")

# Sidebar for role selection
role = st.sidebar.selectbox("Choose a Role:", list(ROLES.keys()))

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini Response
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([ROLES[role], prompt])

        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
