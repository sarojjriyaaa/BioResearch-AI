from collections import Counter


class VisualizationAgent:

    def prepare(self, evidence):

        years = []
        journals = []
        authors = []
        keywords = []

        for paper in evidence:

            if paper.get("year"):
                years.append(paper["year"])

            if paper.get("journal"):
                journals.append(paper["journal"])

            authors.extend(paper.get("authors", []))

            title = paper.get("title", "")

            for word in title.split():

                word = word.lower()

                if len(word) > 4:
                    keywords.append(word)

        return {

            "paper_count": len(evidence),

            "years": Counter(years),

            "journals": Counter(journals),

            "authors": Counter(authors).most_common(10),

            "keywords": Counter(keywords).most_common(15)

        }