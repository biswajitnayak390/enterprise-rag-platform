from fastapi import FastAPI
from pydantic import BaseModel

from app.services.rag_service import EnterpriseRAGService

app = FastAPI(title="Enterprise RAG Platform")

rag_service = EnterpriseRAGService()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "enterprise-rag-platform"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return rag_service.answer_question(request.question)
