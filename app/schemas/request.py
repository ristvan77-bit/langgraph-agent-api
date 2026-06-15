from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    task: str = Field(..., min_length=3, description="Task for the agent to process")
