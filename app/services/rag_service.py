"""
rag_service.py

Gemini RAG Service

Author: Riya Saroj
Project: BioResearch AI
"""

from google import genai


def configure_gemini(api_key: str):

    client = genai.Client(
        api_key=api_key
    )

    return client


def build_context(papers):

    context = ""

    for i, paper in enumerate(papers, start=1):

        context += f"""
Paper {i}

Title:
{paper["title"]}

Abstract:
{paper["abstract"]}

PMID:
{paper["pmid"]}

----------------------------------------
"""

    return context


def generate_literature_review(
    client,
    query,
    papers
):

    context = build_context(papers)

    prompt = f"""
You are an expert biomedical research assistant.

Use ONLY the evidence provided below.

Research Question:
{query}

Scientific Papers:
{context}

Generate a structured literature review.

Include:

1. Overview
2. Major Findings
3. Biological Mechanisms
4. Important Genes
5. Important Drugs / Compounds
6. Contradictory Evidence
7. Research Gaps
8. Future Directions
9. References (PMIDs)
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text