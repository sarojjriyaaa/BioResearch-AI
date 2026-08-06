"""
evidence_agent.py

Evidence Extraction Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from typing import List, Dict


class EvidenceAgent:

    def extract(self, papers: List[Dict]):

        evidence = []

        for paper in papers:

            item = {

                "pmid": paper.get("pmid"),

                "title": paper.get("title"),

                "journal": paper.get("journal"),

                "year": paper.get("year"),

                "abstract": paper.get("abstract"),

                "study_type": "Unknown",

                "genes": [],

                "proteins": [],

                "drugs": [],

                "diseases": [],

                "pathways": [],

                "biomarkers": [],

                "key_findings": ""

            }

            evidence.append(item)

        return evidence