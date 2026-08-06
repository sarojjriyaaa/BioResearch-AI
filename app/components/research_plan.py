import streamlit as st


def render_plan(plan):

    st.subheader("🧠 Research Plan")

    st.write(
        f"**Main Topic:** {plan['main_topic']}"
    )

    st.write("### Search Queries")

    for q in plan["queries"]:

        st.write("•", q)