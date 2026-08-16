"""
rag_service.py

Gemini RAG Service

Author: Riya Saroj
Project: BioResearch AI
"""

import time
from google import genai


def configure_gemini(api_key):
    client = genai.Client(api_key=api_key)

    print("AVAILABLE MODELS")

    for model in client.models.list():
        print(model.name)

    return client

def build_context(papers):
    """
    Build prompt context from retrieved papers.
    """

    context = ""

    for i, paper in enumerate(papers, start=1):

        title = paper.get("title", "Unknown")

        abstract = paper.get("abstract", "")

        pmid = paper.get("pmid", "Unknown")

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

    papers = papers[:6]

    context = build_context(papers)

    prompt = f"""
You are a senior biomedical researcher.

Write a professional evidence-based literature review.

IMPORTANT

- Use ONLY the papers below.
- Never invent facts.
- Mention PMID whenever making scientific claims.
- Write in Markdown.

Research Question

{query}

Scientific Papers

{context}

Return the report with these headings.

# Executive Summary

# Background

# Major Findings

# Molecular Mechanisms

# Important Genes

# Therapeutic Targets

# Limitations

# Future Directions

# References (PMIDs)
"""

    last_error = None

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            if response.text:
                return response.text

            return "# No review generated."

        except Exception as e:

            last_error = e

            print(f"Attempt {attempt+1} failed")

            print(e)

            time.sleep(3)

    return f"""
# AI Literature Review

⚠️ Gemini could not generate the literature review.

Reason

{last_error}

The scientific papers were retrieved successfully.

Please try again later.
"""