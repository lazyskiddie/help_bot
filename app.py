import streamlit as st
from components.chat_ui import chat_interface

st.set_page_config(page_title="MOSDAC Help Bot", layout="wide")

# loda kiya time pass
st.markdown(
    """
    <style>
    .stApp h1 {
        text-align: center;
        width: 100%; /* Ensure it takes full width for centering to work effectively */
    }

       st.chat_input usually handles spacing well above itself, but
       this can be useful for general content above the chat interface. */
    .main .block-container {
        /* Add some padding at the bottom to give space for content above the sticky chat input */
        padding-bottom: 5rem; /* Adjust as needed, 5rem is a good starting point */
    }

    .st-chat-message-container {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .st-chat-message-container.user {
        background-color: #0d283c; /* A darker shade for user messages */
        text-align: right; /* Align user messages to the right */
        margin-left: auto; /* Push user message container to the right */
        width: fit-content; /* Make container width fit content */
        max-width: 80%; /* Limit width */
    }
    .st-chat-message-container.assistant {
        background-color: #1a1a2e; /* A slightly lighter shade for bot messages */
        text-align: left; /* Align assistant messages to the left */
        margin-right: auto; /* Push assistant message container to the left */
        width: fit-content; /* Make container width fit content */
        max-width: 80%; /* Limit width */
    }
    .st-chat-message-container .stMarkdown {
        word-wrap: break-word; /* Ensure long words wrap */
    }

    </style>
    """,
    unsafe_allow_html=True 
)

# Description 
st.title("🛰️ MOSDAC AI Help Bot")
st.markdown("""
 
Ask any question about satellite data, missions, products, or scientific documentation!
""")

# --- Run Chatbot UI ---
chat_interface()