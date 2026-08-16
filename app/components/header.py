import streamlit as st


def render_header():

    st.markdown(
        """
<div class="hero">

<h1>🧬 BioResearch AI Platform</h1>

<p>
AI-powered Biomedical Literature Discovery & Evidence-based Research Assistant
</p>

</div>
""",
        unsafe_allow_html=True
    )