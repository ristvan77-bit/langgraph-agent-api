from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.agent import router as agent_router

app = FastAPI(
    title="LangGraph Agent API",
    version="0.1.0",
    description="Production-style multi-agent AI API built with LangGraph and FastAPI."
)

app.include_router(health_router)
app.include_router(agent_router)
