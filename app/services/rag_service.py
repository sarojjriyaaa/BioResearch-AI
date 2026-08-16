"""
rag_service.py

OpenRouter Literature Review Service

Author: Riya Saroj
Project: BioResearch AI
"""

import os
import requests


API_URL = "https://openrouter.ai/api/v1/chat/completions"


def configure_gemini(api_key=None):
    """
    Kept for compatibility.
    We simply return the OpenRouter key.
    """
    return os.getenv("OPENROUTER_API_KEY")


def build_context(papers):

    context = ""

    for i, paper in enumerate(papers, start=1):

        context += f"""

Paper {i}

Title:
{paper.get("title","")}

Journal:
{paper.get("journal","")}

Year:
{paper.get("year","")}

PMID:
{paper.get("pmid","")}

Abstract:
{paper.get("abstract","")[:1200]}

----------------------------------------
"""

    return context


def generate_literature_review(
    api_key,
    query,
    papers
):

    papers = papers[:6]

    context = build_context(papers)

    prompt = f"""
You are a senior biomedical scientist.

Write a professional literature review.

Rules:

- Use ONLY the provided papers.
- Never invent facts.
- Mention PMIDs.
- Use markdown headings.

Research Question:

{query}

Scientific Papers:

{context}

Write:

# Executive Summary

# Major Findings

# Biological Mechanisms

# Important Genes

# Therapeutic Targets

# Research Gaps

# Future Directions

# References
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openrouter/auto",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"]