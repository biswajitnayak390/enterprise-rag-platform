from app.services.rag_service import EnterpriseRAGService


def test_rag_service_returns_answer_for_sitecore_query():
    service = EnterpriseRAGService()

    response = service.answer_question("What is Sitecore XM Cloud?")

    assert response["answer"] != "No enterprise knowledge found."
    assert len(response["sources"]) > 0


def test_rag_service_handles_unknown_query():
    service = EnterpriseRAGService()

    response = service.answer_question("unknown random query")

    assert response["answer"] == "No enterprise knowledge found."
    assert response["sources"] == []
