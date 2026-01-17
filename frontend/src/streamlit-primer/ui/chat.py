import streamlit as st
from utils.state import add_message


def render_chat():
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])


def chat_input():
    user_text = st.chat_input("Message…")
    if user_text:
        add_message("user", user_text)
        return user_text
    return None
