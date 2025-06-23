import streamlit as st
from components.chat_ui import chat_interface

st.set_page_config(page_title="MOSDAC Help Bot", layout="wide")

st.title("🛰️ MOSDAC AI Help Bot")
st.markdown("""
Welcome to the MOSDAC Help Bot powered by LLM + Knowledge Graph.  
Ask any question about satellite data, missions, products, or scientific documentation!
""")
chat_interface()
