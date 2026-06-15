from fastapi import APIRouter
from app.schemas.request import AgentRequest
from app.schemas.response import AgentResponse

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/run", response_model=AgentResponse)
def run_agent(payload: AgentRequest):
    return AgentResponse(
        status="success",
        task=payload.task,
        result=f"Mock agent processed task: {payload.task}",
        trace=["planner", "writer", "reviewer"]
    )
