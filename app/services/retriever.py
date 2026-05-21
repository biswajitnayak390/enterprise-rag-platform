from app.data.knowledge_documents import KNOWLEDGE_DOCUMENTS


class EnterpriseRetriever:
    def retrieve(self, query: str):
        query = query.lower()
        scored_results = []

        for document in KNOWLEDGE_DOCUMENTS:
            combined_text = (
                document["title"] + " " + document["content"]
            ).lower()

            score = 0

            for word in query.split():
                if word in combined_text:
                    score += 1

            if score > 0:
                scored_results.append({
                    **document,
                    "score": score
                })

        scored_results.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return scored_results[:3]
