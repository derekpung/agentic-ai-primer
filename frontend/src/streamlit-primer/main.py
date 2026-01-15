# app.py
import streamlit as st
import requests
import os

backend_host = os.getenv("BACKEND_HOST", "")
backend_port = os.getenv("BACKEND_PORT", "")
backend_url = f"http://{backend_host}:{backend_port}"
agent_url = f"{backend_url}/generate"

st.title("LLM Chat UI")

user_input = st.text_area("Enter your prompt:")
if st.button("Send"):
    response = requests.post(agent_url, json={"text": user_input})
    st.write("LLM Response:", response.json()["response"])
