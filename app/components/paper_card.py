import streamlit as st


def display_paper(paper,index):

    with st.container():

        st.markdown(
            f"""
<div class="paper-card">

<h3>{index}. {paper['title']}</h3>

<b>Journal:</b> {paper['journal']}<br>

<b>Year:</b> {paper['year']}<br>

<b>PMID:</b> {paper['pmid']}

</div>
""",
            unsafe_allow_html=True
        )

        with st.expander("Abstract"):

            st.write(paper["abstract"])