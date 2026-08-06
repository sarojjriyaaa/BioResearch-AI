import streamlit as st


def render_workflow(status):

    st.subheader("🤖 Multi-Agent Workflow")

    icons = {
        "Planner Complete": "🧠",
        "Retrieval Complete": "📚",
        "Filtering Complete": "🧹",
        "Ranking Complete": "🔎",
        "Evidence Extraction Complete": "🧬",
        "Review Complete": "✍",
        "Visualization Complete": "📊"
    }

    for step in status:

        st.success(f"{icons.get(step,'✔')} {step}")