import streamlit as st


def render_metrics(stats, elapsed):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Retrieved",
        stats["retrieved"]
    )

    c2.metric(
        "Filtered",
        stats["filtered"]
    )

    c3.metric(
        "Ranked",
        stats["ranked"]
    )

    c4.metric(
        "Time",
        f"{elapsed}s"
    )