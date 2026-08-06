"""
orchestrator.py

Multi-Agent Workflow

Author: Riya Saroj
Project: BioResearch AI
"""

from agents.planner_agent import ResearchPlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.filter_agent import FilterAgent
from agents.ranking_agent import RankingAgent
from agents.evidence_agent import EvidenceAgent
from agents.review_agent import ReviewAgent
from agents.visualization_agent import VisualizationAgent


class AgentOrchestrator:

    def __init__(self):

        self.planner = ResearchPlannerAgent()
        self.retriever = RetrievalAgent()
        self.filter = FilterAgent()
        self.ranker = RankingAgent()
        self.evidence = EvidenceAgent()
        self.reviewer = ReviewAgent()
        self.visualizer = VisualizationAgent()

    def run(self, query, top_k):

        plan = self.planner.plan(query)

        papers = self.retriever.retrieve(
            plan["queries"]
        )

        filtered = self.filter.filter(
            papers
        )

        ranked = self.ranker.rank(
            query,
            filtered,
            top_k
        )

        evidence = self.evidence.extract(
            ranked
        )

        review = self.reviewer.review(
            query,
            ranked
        )

        visuals = self.visualizer.prepare(
            evidence
        )

        status = []
        status.append("Planner Complete")
        status.append("Retrieval Complete")
        status.append("Filtering Complete")
        status.append("Rankking Complete")
        status.append("Evidence Extraction Complete")
        status.append("Review Complete")
        status.append("Visualization Complete")

        return {

            "plan": plan,

            "papers": ranked,

            "review": review,

            "evidence": evidence,

            "visuals": visuals,

            "status": status,

            "stats": {

                "retrieved": len(papers),
                "filtered": len(filtered),
                "ranked": len(ranked)
            }

        }