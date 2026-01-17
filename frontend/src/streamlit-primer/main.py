import streamlit as st
from ui.chat import render_chat, chat_input
from ui.file_upload import file_uploader
from ui.login import login_ui
from services.llm import send_request
from utils.state import init_state, add_message

st.set_page_config(page_title="LLM Chat UI", page_icon="💬")

init_state()

login_ui()

if st.session_state.get("user"):
    st.title("LLM Chat UI ")
    file_uploader()
    render_chat()

    user_text = chat_input()
    if user_text:
        reply = send_request(user_text)
        add_message("assistant", reply)
        st.rerun()
else:
    st.warning("Please log in to access the chat.")
    import streamlit as st
