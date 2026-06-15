# LangGraph Agent API

Production-style multi-agent AI API built with LangGraph and FastAPI.

## Overview
This project exposes a graph-based AI agent through a FastAPI backend.
The workflow processes a task through multiple nodes such as planning, research, writing, and review.

## Why this project
This repository is designed to demonstrate:
- agent orchestration with LangGraph
- clean FastAPI backend structure
- schema validation with Pydantic
- reproducible local setup
- basic evaluation and testing

## Planned features
- Multi-step graph workflow
- Task execution trace
- Modular tool integration
- Evaluation endpoint
- Docker-based local run

## Project structure
```text
app/
tests/
scripts/
Dockerfile
docker-compose.yml
requirements.txt
README.md
```

## Quickstart
```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

## Roadmap
- FastAPI skeleton
- LangGraph workflow
- Evaluation endpoint
- Docker support
- Tests
- README improvements