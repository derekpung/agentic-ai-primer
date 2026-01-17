import streamlit as st
from utils.formatting import now
from typing import List, Dict


def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages: List[
            Dict
        ] = []  # [{"role": "user"/"assistant"/"system", "content": str, "time": str}]
    if "files" not in st.session_state:
        st.session_state.files: List[
            Dict
        ] = []  # [{"name": str, "type": str, "size": int, "data": bytes}] if "pending_user_text" not in st.session_state: st.session_state.pending_user_text = None


def add_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content, "time": now()})


def add_files(uploaded_files):
    for f in uploaded_files:
        st.session_state.files.append(
            {
                "name": f.name,
                "type": f.type,
                "size": f.size,
                "data": f.getvalue(),
                # bytes; swap for storage path if needed
                "time": now(),
            }
        )
