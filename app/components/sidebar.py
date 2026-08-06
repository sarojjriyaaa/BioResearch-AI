import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🧬 BioResearch AI")

        st.caption("Biomedical Research Platform")

        st.divider()

        st.subheader("Navigation")

        st.page_link(
            "streamlit_app.py",
            label="🏠 Dashboard"
        )

        st.page_link(
            "pages/1_Literature_Review.py",
            label="📚 Literature Review"
        )

        st.page_link(
            "pages/2_Paper_Explorer.py",
            label="📄 Paper Explorer"
        )

        st.page_link(
            "pages/3_AI_Agents.py",
            label="🤖 AI Workspace"
        )

        st.page_link(
            "pages/4_About.py",
            label="ℹ About"
        )

        st.divider()

        st.subheader("System")

        st.success("🟢 Gemini Connected")

        st.info(
            """
Embedding Model

all-MiniLM-L6-v2
"""
        )

        st.info(
            """
Vector Database

FAISS
"""
        )

        st.divider()

        st.caption("Version 2.0")