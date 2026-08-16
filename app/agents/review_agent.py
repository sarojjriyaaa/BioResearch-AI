"""
review_agent.py

AI Literature Review Agent

Author: Riya Saroj
Project: BioResearch AI
"""

import os
from dotenv import load_dotenv

from services.rag_service import (
    configure_gemini,
    generate_literature_review
)

load_dotenv()


class ReviewAgent:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        self.client = configure_gemini(os.getenv("GEMINI_API_KEY"))

    def review(self, query, papers):

        return generate_literature_review(
            self.client,
            query,
            papers
        )