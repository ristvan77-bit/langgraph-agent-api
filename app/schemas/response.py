from pydantic import BaseModel


class AgentResponse(BaseModel):
    status: str
    task: str
    result: str
    trace: list[str]
