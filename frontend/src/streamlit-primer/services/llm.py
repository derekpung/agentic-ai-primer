import requests
from services.config import app_settings
from services.auth import AuthSession


def send_request(user_input: str):
    auth_session = AuthSession()
    response = auth_session.post(app_settings.LLM_CHAT_URL, json={"text": user_input})
    return response.json()["response"]
