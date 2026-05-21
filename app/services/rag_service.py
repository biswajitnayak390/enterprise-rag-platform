from app.services.retriever import EnterpriseRetriever


class EnterpriseRAGService:
    def __init__(self):
        self.retriever = EnterpriseRetriever()

    def answer_question(self, question: str):
        results = self.retriever.retrieve(question)

        if not results:
            return {
                "question": question,
                "answer": "No enterprise knowledge found.",
                "sources": []
            }

        context = " ".join([
            result["content"] for result in results
        ])

        return {
            "question": question,
            "answer": f"Enterprise AI Response: {context}",
            "sources": [
                result["title"] for result in results
            ]
        }
