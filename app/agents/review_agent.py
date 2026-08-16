"""
review_agent.py

AI Literature Review Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from services.rag_service import (
    configure_gemini,
    generate_literature_review,
)


class ReviewAgent:

    def __init__(self):
        self.client = configure_gemini()

    def review(self, query, papers):

        try:
            return generate_literature_review(
                self.client,
                query,
                papers
            )

        except Exception as e:

            print(f"Gemini Error: {e}")

            return f"""
# AI Literature Review

⚠️ Gemini is temporarily unavailable.

Reason:

{str(e)}

The literature search completed successfully.

Retrieved **{len(papers)}** relevant papers.

Please review the retrieved evidence below.
"""