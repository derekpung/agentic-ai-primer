import os


class AuthConfig:
    KEYCLOAK_BASE = os.getenv("KEYCLOAK_BASE", "")
    KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "llm-app")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "streamlit-app")
    KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "")
    KEYCLOAK_CALLBACK_URL = os.getenv("KEYCLOAK_CALLBACK_URL", "")

    APP_JWT_SECRET = os.getenv("APP_JWT_SECRET", "change-me")
    APP_JWT_ISSUER = "llm-app"
    APP_JWT_AUDIENCE = "chat-ui"
    APP_JWT_EXPIRE_MIN = int(os.getenv("APP_JWT_EXPIRE_MIN", "60"))


auth_config = AuthConfig()
