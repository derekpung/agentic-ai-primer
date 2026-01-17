import requests
import streamlit as st
from services.config import app_settings


class AuthSession(requests.Session):
    def __init__(self):
        super().__init__()
        # If app_token is stored in browser cookie, attach it to header
        token = st.context.cookies.get("app_token")
        if token:
            self.headers.update({"Authorization": f"Bearer {token}"})

    def request(self, *args, **kwargs):
        # Ensure every request carries the token
        token = st.context.cookies.get("app_token")
        if token:
            kwargs.setdefault("headers", {})
            kwargs["headers"]["Authorization"] = f"Bearer {token}"
            kwargs.setdefault("cookies", {})
            kwargs["cookies"]["app_token"] = token
        return super().request(*args, **kwargs)


def login():
    """Redirect user to backend login endpoint (Keycloak OAuth)."""
    login_url = f"{app_settings.BACKEND_URL}/auth/login"
    if st.button("🔐 Login with Keycloak"):
        st.write("Redirecting...")
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={login_url}">',
            unsafe_allow_html=True,
        )


def check_session():
    try:
        auth_session = AuthSession()
        r = auth_session.get(f"{app_settings.BACKEND_SVC}/auth/me", timeout=5)
        if r.status_code == 200:
            st.session_state.user = r.json().get("user")
            return True
        return False
    except Exception as e:
        st.error(f"Session check failed: {e}")
        return False


def logout():
    """Call backend logout endpoint to clear cookie."""
    try:
        auth_session = AuthSession()
        r = auth_session.post(f"{app_settings.BACKEND_SVC}/auth/logout", timeout=5)
        if r.status_code == 204:
            st.session_state.user = None
            st.success("Logged out successfully.")
            return True
        else:
            st.error("Logout failed.")
            return False
    except Exception as e:
        st.error(f"Logout error: {e}")
        return False
