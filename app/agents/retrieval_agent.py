"""
retrieval_agent.py

Literature Retrieval Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from typing import List

from services.pubmed_service import (
    search_pubmed,
    fetch_articles,
    parse_articles
)


class RetrievalAgent:

    def retrieve(
        self,
        search_queries: List[str],
        max_results: int = 10
    ):

        all_pmids = set()

        for query in search_queries:

            try:

                pmids = search_pubmed(
                    query=query,
                    max_results=max_results
                )

                all_pmids.update(pmids)

            except Exception:

                continue

        root = fetch_articles(
            list(all_pmids)
        )

        papers = parse_articles(root)

        return papers