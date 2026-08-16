import streamlit as st

def render_metrics(stats, elapsed):

    st.subheader("📈 Research Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Retrieved", stats.get("retrieved", 0))
    c2.metric("Filtered", stats.get("filtered", 0))
    c3.metric("Ranked", stats.get("ranked", 0))
    c4.metric("Execution Time", f"{elapsed:.2f} sec")