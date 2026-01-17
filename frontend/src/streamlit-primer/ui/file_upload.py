import streamlit as st
from utils.state import add_files


def file_uploader():
    uploaded = st.file_uploader(
        "Upload documents", type=["pdf", "txt", "docx"], accept_multiple_files=True
    )
    if uploaded:
        add_files(uploaded)
        st.success(f"Added {len(uploaded)} file(s).")
