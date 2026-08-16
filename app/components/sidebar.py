import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🧬 BioResearch AI")

        st.caption("Biomedical Research Platform")

        st.divider()

        st.write("### Navigation")

        st.write("🏠 Dashboard")

        st.write("📚 Literature Review")

        st.write("📄 Paper Explorer")

        st.write("🤖 AI Workspace")

        st.write("📊 Analytics")

        st.write("💾 Research History")

        st.divider()

        st.write("### System")

        st.success("🟢 Gemini Connected")

        st.write("Embedding")

        st.code("all-MiniLM-L6-v2")

        st.write("Vector DB")

        st.code("FAISS")

        st.write("Database")

        st.code("SQLite")