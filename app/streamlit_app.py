import os
import time

import streamlit as st
from dotenv import load_dotenv

from services.pubmed_service import (
    search_pubmed,
    fetch_articles,
    parse_articles,
)

from services.embedding_service import (
    load_embedding_model,
    create_embeddings,
    build_faiss_index,
    semantic_search,
)

from services.rag_service import (
    configure_gemini,
    generate_literature_review,
)

load_dotenv()

st.set_page_config(
    page_title="BioResearch AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:

    st.title("🧬 BioResearch AI")

    st.markdown("---")

    st.subheader("Project")

    st.write("Version : 1.0")

    st.write("LLM : Gemini Flash")

    st.write("Vector DB : FAISS")

    st.write("Embedding : all-MiniLM-L6-v2")

    st.markdown("---")

    st.subheader("Developer")

    st.write("Riya Saroj")

    st.markdown("---")

    st.caption("AI-powered Biomedical Literature Assistant")

    
st.markdown(
    """
# 🧬 BioResearch AI

### AI-powered Biomedical Research Assistant
"""
)

st.markdown(
"""
Search PubMed, retrieve the most relevant scientific papers,
and generate an evidence-based literature review using AI.
"""
)

st.divider()


query = st.text_input(
    "🔍 Enter Research Question",
    placeholder="Example: HIV-1 protease inhibitors"
)

top_k = st.slider(
    "Number of Relevant Papers",
    5,
    20,
    5
)


if st.button("Generate Literature Review"):

    if query.strip() == "":
        st.warning("Please enter a research question.")
        st.stop()

    with st.spinner("Searching PubMed..."):

        pmids = search_pubmed(
            query=query,
            max_results=20
        )

        root = fetch_articles(pmids)
        start_time = time.time()
        papers = parse_articles(root)

    with st.spinner("Creating embeddings..."):

        model = load_embedding_model()

        embeddings, papers = create_embeddings(
            papers,
            model
        )

        index = build_faiss_index(
            embeddings
        )

    with st.spinner("Retrieving relevant papers..."):

        retrieved = semantic_search(
            query=query,
            model=model,
            index=index,
            papers=papers,
            top_k=top_k
        )

    with st.spinner("Generating AI review..."):

        gemini = configure_gemini(
            os.getenv("GEMINI_API_KEY")
        )

        review = generate_literature_review(
            gemini,
            query,
            retrieved
        )

    elapsed = round(
        time.time() - start_time,
        2
    )

    st.success("Done!")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Retrieved Papers",
            len(retrieved)
        )

    with c2:
        st.metric(
            "Embedding Size",
            384
        )

    with c3:
        st.metric(
            "Time",
            f"{elapsed} sec"
        )

    st.subheader("📚 Retrieved Papers")

    for i, paper in enumerate(retrieved, start=1):

        st.markdown(f"### {i}. {paper['title']}")

        st.write(f"**Journal:** {paper['journal']}")

        st.write(f"**Year:** {paper['year']}")

        st.write(f"**PMID:** {paper['pmid']}")

        st.write("---")

        


    