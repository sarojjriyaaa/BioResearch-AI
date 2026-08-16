import streamlit as st
import pandas as pd


def render_analytics(visuals):

    st.subheader("📊 Research Analytics")

    years = visuals.get("years", {})

    if years:

        st.markdown("### Publication Trend")

        df = pd.DataFrame({

            "Year": list(years.keys()),
            "Count": list(years.values())

        }).sort_values("Year")

        st.line_chart(df.set_index("Year"))

    journals = visuals.get("journals", {})

    if journals:

        st.markdown("### Top Journals")

        journal_df = pd.DataFrame({

            "Journal": list(journals.keys()),
            "Publications": list(journals.values())

        }).sort_values("Publications", ascending=False)

        st.bar_chart(journal_df.set_index("Journal"))

    authors = visuals.get("authors", [])

    if authors:

        st.markdown("### Top Authors")

        st.dataframe(
            pd.DataFrame(
                authors,
                columns=["Author", "Papers"]
            ),
            use_container_width=True
        )

    keywords = visuals.get("keywords", [])

    if keywords:

        st.markdown("### Frequent Keywords")

        st.dataframe(
            pd.DataFrame(
                keywords,
                columns=["Keyword", "Frequency"]
            ),
            use_container_width=True
        )