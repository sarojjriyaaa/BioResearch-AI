import streamlit as st

def render_metrics(stats, elapsed):

    st.write("TYPE:", type(stats))
    st.write("VALUE:", stats)

    st.stop()