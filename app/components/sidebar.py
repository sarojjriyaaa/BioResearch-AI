import streamlit as st


def render_sidebar():

    with st.sidebar:
        st.title("🧬 BioResearch AI")
        st.markdown("### Navigation")
        st.info("🏠 Dashboard")
        st.info("📚 Literature Review")
        st.info("📄 Paper Explorer")
        st.info("🤖 AI Workspace")
        st.divider()
        st.markdown("### System")
        st.success("🟢 Gemini Connected")
        st.write("Embedding Model")
        st.code("all-MiniLM-L6-v2")
        st.write("Vector Database")
        st.code("FAISS")
        st.caption("Version 2.0")