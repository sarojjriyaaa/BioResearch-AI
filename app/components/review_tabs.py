import streamlit as st


def show_review(review):

    overview, findings, gaps, refs = st.tabs(
        [
            "Overview",
            "Findings",
            "Research Gaps",
            "References"
        ]
    )

    with overview:

        st.markdown(review)

    with findings:

        st.info(
            "Evidence extraction agent coming soon."
        )

    with gaps:

        st.info(
            "Research gap analysis coming soon."
        )

    with refs:

        st.info(
            "Automatic reference extraction coming soon."
        )