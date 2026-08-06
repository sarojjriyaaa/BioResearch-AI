import streamlit as st


def show_review(review: str):

    st.markdown("## 📖 AI Literature Review")

    st.markdown(review)