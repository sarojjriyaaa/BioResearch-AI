"""
pubmed_service.py

Handles communication with the PubMed API.

Author: Riya Saroj
Project: BioResearch AI
"""

import json
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict

# PubMed API endpoints
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query: str, max_results: int = 100) -> List[str]:
    """
    Search PubMed and return a list of PMIDs.

    Parameters
    ----------
    query : str
        Search query.
    max_results : int
        Maximum number of papers to retrieve.

    Returns
    -------
    List[str]
        List of PubMed IDs (PMIDs).
    """

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(ESEARCH_URL, params=params)

    response.raise_for_status()

    data = response.json()

    pmids = data["esearchresult"]["idlist"]

    return pmids

def fetch_articles(pmids):

    if not pmids:
        return ET.Element("PubmedArticleSet")

    params = {
        "db": "pubmed",
        "id": ",".join(pmids[:100]),   # limit request size
        "retmode": "xml"
    }

    try:

        response = requests.get(
            EFETCH_URL,
            params=params,
            timeout=30,
            headers={
                "User-Agent":"BioResearchAI/1.0"
            }
        )

        response.raise_for_status()

        return ET.fromstring(response.text)

    except requests.exceptions.RequestException as e:

        print("PubMed fetch failed:", e)

        return ET.Element("PubmedArticleSet")

def extract_paper(pubmed_article) -> Dict:
    """
    Extract metadata from a single PubMed article.

    Parameters
    ----------
    pubmed_article : ET.Element
        XML element representing one PubMed article.

    Returns
    -------
    Dict
        Dictionary containing paper metadata.
    """

    medline = pubmed_article.find("MedlineCitation")
    article = medline.find("Article")

    # PMID
    pmid = medline.find("PMID").text

    # Title
    title_element = article.find("ArticleTitle")
    title = title_element.text if title_element is not None else ""

    # Abstract
    abstract = ""

    abstract_element = article.find("Abstract")

    if abstract_element is not None:

        texts = []

        for item in abstract_element.findall("AbstractText"):

            if item.text:
                texts.append(item.text)

        abstract = " ".join(texts)

    # Journal
    journal_element = article.find("Journal/Title")
    journal = journal_element.text if journal_element is not None else ""

    # Year
    year = ""

    year_element = article.find("Journal/JournalIssue/PubDate/Year")

    if year_element is not None:
        year = year_element.text

    # Authors
    authors = []

    author_list = article.find("AuthorList")

    if author_list is not None:

        for author in author_list:

            first = author.find("ForeName")
            last = author.find("LastName")

            if first is not None and last is not None:

                full_name = f"{first.text} {last.text}"

                if full_name not in authors:
                    authors.append(full_name)

    return {
        "pmid": pmid,
        "title": title,
        "abstract": abstract,
        "journal": journal,
        "year": year,
        "authors": authors
    }

def parse_articles(root: ET.Element) -> List[Dict]:
    """
    Parse all PubMed articles from XML.

    Parameters
    ----------
    root : ET.Element

    Returns
    -------
    List[Dict]
    """

    papers = []

    for article in root.findall("PubmedArticle"):

        paper = extract_paper(article)

        papers.append(paper)

    return papers

def save_json(data: List[Dict], output_path: Path) -> None:
    """
    Save paper metadata to JSON.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved {len(data)} papers to:")
    print(output_path)