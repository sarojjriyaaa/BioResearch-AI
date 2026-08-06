import streamlit as st


def render_header():

    st.title("🧬 BioResearch AI")

    st.caption(
        "AI-powered Biomedical Research Platform"
    )

    st.write(
        "Search PubMed, retrieve biomedical literature, perform semantic ranking, "
        "and generate evidence-based literature reviews using AI agents."
    )

    st.divider()