# 🧬 BioResearch AI

> AI-powered Biomedical Literature Research Assistant built using RAG (Retrieval-Augmented Generation), FAISS, PubMed, and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Live Demo

👉 **Try the application here**
(https://bioresearch-ai.streamlit.app/)

---

# Overview

BioResearch AI is an AI-powered biomedical literature assistant that automatically retrieves scientific publications from PubMed, performs semantic search using FAISS embeddings, and generates structured literature reviews using Google's Gemini model.

Instead of manually reading dozens of research papers, researchers can ask a biological question and receive an evidence-based literature review in seconds.

---

# Features

✅ PubMed Literature Retrieval

✅ Semantic Search using Sentence Transformers

✅ FAISS Vector Database

✅ Retrieval-Augmented Generation (RAG)

✅ AI Literature Review Generation

✅ Biological Research Assistant

---

# Project Architecture

```

User Query
│
▼
PubMed Search
│
▼
Paper Collection
│
▼
Sentence Embeddings
│
▼
FAISS Vector Search
│
▼
Relevant Papers
│
▼
Gemini AI
│
▼
Structured Literature Review

```

---

# Tech Stack

- Python
- Streamlit
- PubMed API
- Sentence Transformers
- FAISS
- Google Gemini
- NumPy

---

# Folder Structure

```

BioResearch-AI
│
├── app
│ ├── agents
│ ├── services
│ ├── utils
│ ├── streamlit_app.py
│ └── main.py
│
├── data
│ ├── raw
│ └── processed
│
├── README.md
├── requirements.txt
└── LICENSE

```

---

# Installation

```bash
git clone https://github.com/sarojjriyaaa/BioResearch-AI.git

cd BioResearch-AI

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

---

# Example Query

```
DNMT1 inhibitors in colorectal cancer
HIV-1 protease drug discovery
```

---

# Example Output

The application generates:

- Overview
- Major Findings
- Biological Mechanisms
- Important Genes
- Important Drugs
- Contradictory Evidence
- Research Gaps
- Future Directions
- References (PMIDs)

---

# Future Improvements

- Multi-Agent Research System
- PDF Literature Review Export
- Chat History
- ChromaDB Support
- Citation Network Visualization
- Paper Recommendation Engine
- Full-text Paper Retrieval (PMC)

---

# Author

**Riya Saroj**

B.Tech Biotechnology

Interested in Computational Biology • Bioinformatics • AI for Healthcare

---

# License

MIT License
