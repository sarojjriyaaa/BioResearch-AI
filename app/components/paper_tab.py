"""
paper_tab.py

Displays retrieved research papers.

Author: Riya Saroj
Project: BioResearch AI
"""

import streamlit as st


def render_papers(papers):

    st.subheader("📚 Retrieved Papers")

    if not papers:

        st.info("No papers found.")

        return

    for i, paper in enumerate(papers, start=1):

        with st.expander(f"{i}. {paper['title']}", expanded=False):

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Journal:** {paper.get('journal','N/A')}")

                st.write(f"**Year:** {paper.get('year','N/A')}")

            with col2:

                st.write(f"**PMID:** {paper.get('pmid','N/A')}")

            st.markdown("### Abstract")

            st.write(
                paper.get(
                    "abstract",
                    "No abstract available."
                )
            )