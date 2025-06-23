import streamlit as st
import requests

API_URL = "f99ebf92-6d8c-4a20-a404-8d849a161fe2"  # Replace with actual FastAPI endpoint

def chat_interface():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask your question", key="input")
    if user_input:
        st.session_state.chat_history.append(("You", user_input))

        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"query": user_input})
                bot_reply = response.json().get("answer", "Sorry, I couldn't find that.")
            except Exception as e:
                bot_reply = f"Error: {str(e)}"

        st.session_state.chat_history.append(("MOSDAC Bot", bot_reply))

    # Display chat history
    for speaker, text in reversed(st.session_state.chat_history):
        st.markdown(f"**{speaker}:** {text}")
