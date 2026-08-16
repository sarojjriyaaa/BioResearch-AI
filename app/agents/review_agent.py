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

        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY not found in environment variables."
            )

        self.client = configure_gemini(api_key)

    def review(self, query, papers):

        return generate_literature_review(
            self.client,
            query,
            papers
        )