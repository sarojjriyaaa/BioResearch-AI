"""
embedding_service.py

Creates vector embeddings and manages the FAISS vector database.

Author: Riya Saroj
Project: BioResearch AI
"""

import json
from pathlib import Path
from typing import List, Dict

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def load_papers(json_path: Path) -> List[Dict]:
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_embeddings(
    papers,
    model
):
    texts = []
    valid_papers = []

    for paper in papers:

        title = paper.get("title", "")
        abstract = paper.get("abstract", "")

        if not title and not abstract:
            continue

        texts.append(f"{title}\n\n{abstract}")
        valid_papers.append(paper)

    if len(texts) == 0:
        return np.empty((0, 384), dtype=np.float32), []

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )

    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    return embeddings.astype(np.float32), valid_papers


def build_faiss_index(embeddings):

    if embeddings.shape[0] == 0:
        raise ValueError("No embeddings generated.")
    
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def semantic_search(
    query: str,
    model,
    index,
    papers,
    top_k: int = 5
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    ).astype(np.float32)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(papers[idx])

    return results