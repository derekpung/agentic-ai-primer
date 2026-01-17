import streamlit as st
from services import auth


def login_ui():
    if "user" not in st.session_state:
        st.session_state.user = None

    if not st.session_state.user:
        st.subheader("Login")
        auth.login()  # shows link to backend /auth/login
        if st.button("Check Session"):
            if auth.check_session():
                st.success(f"Logged in as {st.session_state.user.get('email')}")
            else:
                st.error("Not authenticated.")
    else:
        st.info(f"Logged in as {st.session_state.user.get('email')}")
        if st.button("Logout"):
            auth.logout()
