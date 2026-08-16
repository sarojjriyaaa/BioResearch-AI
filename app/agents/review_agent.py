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


def review(self, query, papers):

    try:
        return generate_literature_review(
            self.client,
            query,
            papers
        )

    except Exception as e:

        print(e)

        return f"""
# AI Literature Review

⚠️ Gemini is temporarily unavailable.

Reason:

{str(e)}

The literature search completed successfully.

Retrieved {len(papers)} relevant papers.

Please review the evidence below.
"""