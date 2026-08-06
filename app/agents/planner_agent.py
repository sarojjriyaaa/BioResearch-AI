"""
planner_agent.py

Research Planning Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from typing import Dict, List


class ResearchPlannerAgent:

    def plan(self, query: str) -> Dict:

        query = query.strip()

        keywords = [
            query,
            f"{query} genetics",
            f"{query} biomarkers",
            f"{query} treatment",
            f"{query} molecular mechanisms",
            f"{query} drug therapy",
            f"{query} pathways",
            f"{query} disease mechanisms"
        ]

        search_queries = [
            query,
            f"{query} insulin resistance",
            f"{query} biomarkers",
            f"{query} genomics",
            f"{query} transcriptomics",
            f"{query} therapeutic targets",
            f"{query} signaling pathways"
        ]

        return {

            "main_topic": query,

            "keywords": keywords,

            "queries": search_queries,

            "synonyms": [
                query,
                query.lower(),
                query.upper()
            ]

        }