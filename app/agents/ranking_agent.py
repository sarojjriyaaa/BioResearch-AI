"""
ranking_agent.py

Semantic Ranking Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from services.embedding_service import (
    load_embedding_model,
    create_embeddings,
    build_faiss_index,
    semantic_search
)


class RankingAgent:

    def __init__(self):

        self.model = load_embedding_model()

    def rank(
        self,
        query,
        papers,
        top_k
    ):

        print("=" * 60)
        print("Papers received:", len(papers))

        embeddings, valid_papers = create_embeddings(
            papers,
            self.model
        )

        print("Valid papers:", len(valid_papers))
        print("Embeddings type:", type(embeddings))

        if hasattr(embeddings, "shape"):
            print("Embeddings shape:", embeddings.shape)

        if len(valid_papers) == 0:
            print("No valid papers.")
            return []

        index = build_faiss_index(
            embeddings
        )


        return semantic_search(
            query=query,
            model=self.model,
            index=index,
            papers=valid_papers,
            top_k=top_k
        )