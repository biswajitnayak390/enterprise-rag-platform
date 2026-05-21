# Enterprise RAG Platform

Enterprise RAG Platform is a Python-first AI engineering project that demonstrates a production-style Retrieval-Augmented Generation architecture for enterprise knowledge search.

The project is designed to showcase practical AI engineering skills using FastAPI, semantic retrieval, document indexing, enterprise knowledge workflows, and API-driven architecture.

## Features

- FastAPI backend
- Enterprise knowledge indexing
- RAG-style retrieval pipeline
- Semantic search simulation
- AI response orchestration
- CMS and DXP-focused sample knowledge base
- Clean service-based backend architecture
- Unit-test-ready Python modules
- Docker-ready structure

## Use Cases

- Enterprise knowledge assistant
- CMS documentation assistant
- Sitecore XM Cloud knowledge search
- Internal support bot
- AI-powered content operations
- Semantic enterprise search

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Docker

## Project Structure

```txt
enterprise-rag-platform
├── app
│   ├── main.py
│   ├── models.py
│   ├── services
│   │   ├── knowledge_base.py
│   │   ├── retriever.py
│   │   └── rag_service.py
│   └── data
│       └── knowledge_documents.py
├── tests
│   └── test_rag_service.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```txt
http://localhost:8000/docs
```

## Example API

```txt
POST /ask
```

Request:

```json
{
  "question": "How does RAG help enterprise CMS teams?"
}
```

## Why This Project Matters

This repository is designed to demonstrate modern AI engineering, enterprise architecture thinking, and AI + CMS integration skills.
