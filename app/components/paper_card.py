import streamlit as st


def display_paper(paper, index):

    with st.container(border=True):

        st.subheader(f"📄 Paper {index}")

        st.markdown(
            f"### {paper['title']}"
        )

        c1, c2, c3 = st.columns(3)

        c1.write(f"**Journal**  \n{paper['journal']}")

        c2.write(f"**Year**  \n{paper['year']}")

        c3.write(f"**PMID**  \n{paper['pmid']}")

        with st.expander("Abstract"):

            st.write(paper["abstract"])