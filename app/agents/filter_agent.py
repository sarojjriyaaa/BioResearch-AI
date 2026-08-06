"""
filter_agent.py

Paper Filtering Agent

Author: Riya Saroj
Project: BioResearch AI
"""


class FilterAgent:

    def filter(self, papers):

        filtered = []

        seen = set()

        for paper in papers:

            pmid = paper.get("pmid")

            if pmid in seen:
                continue

            seen.add(pmid)

            title = paper.get("title", "")
            abstract = paper.get("abstract", "")

            if title == "":
                continue

            if abstract == "":
                continue

            if len(abstract) < 100:
                continue

            filtered.append(paper)

        return filtered