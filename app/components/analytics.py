import streamlit as st
import pandas as pd


def render_analytics(visuals):

    st.subheader("📊 Analytics")

    years = visuals["years"]

    if years:

        df = pd.DataFrame({

            "Year": list(years.keys()),

            "Publications": list(years.values())

        })

        st.bar_chart(
            df.set_index("Year")
        )

    journals = visuals["journals"]

    if journals:

        st.write("### Top Journals")

        st.dataframe(

            pd.DataFrame({

                "Journal": journals.keys(),

                "Count": journals.values()

            })

        )