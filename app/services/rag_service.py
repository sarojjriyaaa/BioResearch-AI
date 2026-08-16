"""
rag_service.py

Gemini RAG Service

Author: Riya Saroj
Project: BioResearch AI
"""

import time
from google import genai


def configure_gemini(api_key: str):
    """
    Configure Gemini client.
    """

    client = genai.Client(
        api_key=api_key
    )

    return client


def build_context(papers):
    """
    Builds prompt context using the retrieved papers.

    Long abstracts are truncated to avoid Gemini
    server errors caused by very large prompts.
    """

    context = ""

    for i, paper in enumerate(papers, start=1):

        title = paper.get("title", "Unknown")

        abstract = paper.get("abstract", "")

        pmid = paper.get("pmid", "Unknown")

        # Prevent extremely large prompts
        if len(abstract) > 1200:
            abstract = abstract[:1200] + "..."

        context += f"""
Paper {i}

Title:
{title}

Abstract:
{abstract}

PMID:
{pmid}

----------------------------------------
"""

    return context


def generate_literature_review(
    client,
    query,
    papers
):
    """
    Generates an evidence-based literature review.

    Automatically retries if Gemini temporarily
    returns a server error.
    """

    # Send only top papers to Gemini
    papers = papers[:6]

    context = build_context(papers)

    prompt = f"""
You are an expert biomedical researcher.

Your job is to write a professional scientific literature review.

IMPORTANT RULES

- Use ONLY the provided papers.
- Do NOT hallucinate.
- Mention PMID wherever appropriate.
- Be concise.
- Use scientific language.

Research Question

{query}

Scientific Papers

{context}

Generate the report using the following headings.

# Overview

# Major Findings

# Biological Mechanisms

# Important Genes

# Important Drugs / Compounds

# Contradictory Evidence

# Research Gaps

# Future Directions

# References (PMIDs)
"""

    last_error = None

    for attempt in range(3):

        try:

            response = client.models.generate_content(

                model="gemini-2.5-flash-lite",

                contents=prompt

            )

            return response.text

        except Exception as e:

            last_error = e

            print(f"Gemini Attempt {attempt+1} Failed")

            print(e)

            time.sleep(5)

    return f"""
# AI Literature Review

⚠️ Gemini could not generate the literature review.

Reason

{last_error}

The scientific papers were retrieved successfully.

Please try again after a few seconds.
"""