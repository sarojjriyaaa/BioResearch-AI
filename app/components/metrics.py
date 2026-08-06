import streamlit as st


def show_metrics(
    papers,
    embedding_size,
    elapsed_time
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📚 Papers",
            len(papers)
        )

    with col2:

        st.metric(
            "🧬 Embedding",
            embedding_size
        )

    with col3:

        st.metric(
            "⏱ Time",
            f"{elapsed_time:.2f}s"
        )

    with col4:

        st.metric(
            "🤖 Status",
            "Ready"
        )