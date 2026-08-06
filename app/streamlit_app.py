"""
streamlit_app.py

BioResearch AI
AI-powered Biomedical Research Platform

Author: Riya Saroj
"""

from pathlib import Path
import time

import streamlit as st

# ----------------------------
# CSS
# ----------------------------

css_path = Path(__file__).parent / "assets" / "styles.css"

if css_path.exists():
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ----------------------------
# Components
# ----------------------------

from components.header import render_header
from components.sidebar import render_sidebar
from components.workflow import render_workflow
from components.metrics import render_metrics
from components.review_tab import show_review
from components.paper_tab import render_papers
from components.analytics import render_analytics
from components.footer import render_footer

# ----------------------------
# Agents
# ----------------------------

from agents.orchestrator import AgentOrchestrator

# ----------------------------
# Streamlit Config
# ----------------------------

st.set_page_config(
    page_title="BioResearch AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Sidebar
# ----------------------------

render_sidebar()

# ----------------------------
# Header
# ----------------------------

render_header()

# ----------------------------
# User Input
# ----------------------------

query = st.text_input(
    "🔍 Research Question",
    placeholder="Example: PCOS, Breast Cancer, BRCA1, Alzheimer's Disease"
)

top_k = st.slider(
    "Number of Relevant Papers",
    min_value=5,
    max_value=20,
    value=5
)

analyze = st.button(
    "🚀 Analyze Literature",
    use_container_width=True
)

# ----------------------------
# Run Pipeline
# ----------------------------

if analyze:

    if query.strip() == "":
        st.warning("Please enter a research question.")
        st.stop()

    orchestrator = AgentOrchestrator()

    start = time.time()

    with st.spinner("🤖 AI Agents are working..."):

        result = orchestrator.run(
            query=query,
            top_k=top_k
        )

    elapsed = round(
        time.time() - start,
        2
    )

    st.success("Analysis Complete!")

    st.divider()

    # ----------------------------
    # Workflow
    # ----------------------------

    render_workflow(
        result["status"]
    )

    st.divider()

    # ----------------------------
    # Metrics
    # ----------------------------

    render_metrics(
        result["stats"],
        elapsed
    )

    st.divider()

    # ----------------------------
    # Tabs
    # ----------------------------

    review_tab, papers_tab, analytics_tab = st.tabs([
        "📖 Literature Review",
        "📚 Papers",
        "📊 Analytics"
    ])

    # ----------------------------
    # Review
    # ----------------------------

    with review_tab:

        show_review(
            result["review"]
        )

    # ----------------------------
    # Papers
    # ----------------------------

    with papers_tab:

        render_papers(
            result["papers"]
        )

    # ----------------------------
    # Analytics
    # ----------------------------

    with analytics_tab:

        render_analytics(
            result["visuals"]
        )

# ----------------------------
# Footer
# ----------------------------

render_footer()