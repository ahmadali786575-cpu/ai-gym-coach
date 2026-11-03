import streamlit as st
import uuid

def get_or_create_user(username):
    if "users" not in st.session_state:
        st.session_state["users"] = {}

    key = username.strip().casefold()
    users = st.session_state["users"]

    if key not in users:
        users[key] = {
            "id": str(uuid.uuid4()),
            "username": username.strip()
        }

    return users[key]

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("🏋️‍♂️ AI Real-time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="unique name e.g. Ahmad Ali")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        user = get_or_create_user(username)
    
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.rerun()

    return False