from pathlib import Path

from app.services.pubmed_service import (
    search_pubmed,
    fetch_articles,
    parse_articles,
    save_json
)

from app.services.embedding_service import (
    load_embedding_model,
    load_papers,
    create_embeddings,
    build_faiss_index,
    semantic_search
)

import os
from dotenv import load_dotenv

load_dotenv()

from app.services.rag_service import (
    configure_gemini,
    generate_literature_review
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data" / "raw"

OUTPUT_FILE = DATA_DIR / "dnmt1_colorectal_cancer.json"


def main():

    print("Searching PubMed...")

    pmids = search_pubmed(
        query="DNMT1 colorectal cancer",
        max_results=10
    )

    print(f"Found {len(pmids)} papers")

    print("Fetching article metadata...")

    root = fetch_articles(pmids)

    print("Parsing articles...")

    papers = parse_articles(root)

    print(f"Parsed {len(papers)} papers")

    save_json(
        papers,
        OUTPUT_FILE
    )

    print("\nLoading embedding model...")

    model = load_embedding_model()

    print("Loading papers...")

    papers = load_papers(OUTPUT_FILE)

    print(f"Loaded {len(papers)} papers")

    print("Creating embeddings...")

    embeddings, papers = create_embeddings(
        papers,
        model
    )

    print("Embedding Shape:")
    print(embeddings.shape)

    print("\nBuilding FAISS Index...")

    index = build_faiss_index(
        embeddings
    )

    print("FAISS Index Ready!")

    query = "Plant-derived DNMT1 inhibitors"

    print(f"\nQuery: {query}")

    results = semantic_search(
        query=query,
        model=model,
        index=index,
        papers=papers,
        top_k=5
    )

    print("\nTop Relevant Papers\n")

    print("\nLoading Gemini...")

    gemini = configure_gemini(
        os.getenv("GEMINI_API_KEY")
    )

    print("Generating Literature Review...\n")

    review = generate_literature_review(
        gemini,
        query,
        results
    )

    print(review)

if __name__ == "__main__":
    main()