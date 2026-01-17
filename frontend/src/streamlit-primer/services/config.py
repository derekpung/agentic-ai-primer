import os


class AppSettings:
    BACKEND_SVC = os.getenv("BACKEND_SVC", "")
    BACKEND_URL = os.getenv("BACKEND_URL", "")

    LLM_CHAT_URL = f"{BACKEND_SVC}/llm/chat"


app_settings = AppSettings()
