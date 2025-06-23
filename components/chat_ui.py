import streamlit as st
import requests
# IMPORTANT: Replace with your actual FastAPI backend URL
# This URL should point to where your backend chat endpoint is hosted (e.g., Railway URL)
API_URL = "https://<your-railway-backend-url>/chat"

def chat_interface():
    # Initialize chat history in session state if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat messages from history
    for speaker, text in st.session_state.chat_history:
        if speaker == "You":
            with st.chat_message("user"):
                st.markdown(text)
        else: # Assumed to be "MOSDAC Bot"
            with st.chat_message("assistant"):
                st.markdown(text)

    user_input = st.chat_input("Ask your question")

    if user_input:
        # kal me add kar diya
        st.session_state.chat_history.append(("You", user_input))
        st.rerun() 

    # uski yade !!
    if st.session_state.chat_history and st.session_state.chat_history[-1][0] == "You" and \
       len(st.session_state.chat_history) % 2 != 0:
        query_to_send = st.session_state.chat_history[-1][1]

        with st.spinner("Thinking..."):
            try:
                # API request to your backend
                response = requests.post(API_URL, json={"query": query_to_send}, timeout=30)
                response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
                bot_reply = response.json().get("answer", "Sorry, I couldn't find that.")
            except requests.exceptions.RequestException as e:
                bot_reply = f"Error connecting to bot: {e}. Please check your backend URL and status."
            except Exception as e:
                bot_reply = f"An unexpected error occurred: {str(e)}"

        # chat history
        st.session_state.chat_history.append(("MOSDAC Bot", bot_reply))

        # Re-run the app to display the bot's response
        st.rerun() 