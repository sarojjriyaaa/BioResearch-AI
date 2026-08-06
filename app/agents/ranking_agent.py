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

        embeddings, valid_papers = create_embeddings(
            papers,
            self.model
        )

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