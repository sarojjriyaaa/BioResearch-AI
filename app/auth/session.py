import streamlit as st


def login(user):

    st.session_state.logged_in = True

    st.session_state.user_id = user.id

    st.session_state.username = user.username


def logout():

    st.session_state.clear()