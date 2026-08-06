"""
visualization_agent.py

Visualization Preparation Agent

Author: Riya Saroj
Project: BioResearch AI
"""

from collections import Counter


class VisualizationAgent:

    def prepare(self, evidence):

        years = []
        journals = []

        for paper in evidence:

            if paper["year"]:
                years.append(paper["year"])

            if paper["journal"]:
                journals.append(paper["journal"])

        return {

            "paper_count": len(evidence),

            "years": Counter(years),

            "journals": Counter(journals)

        }