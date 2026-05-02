from pydantic import BaseModel, field_validator
from typing import Literal, Optional, Dict, Any

class AgentOutput(BaseModel):
    action: Literal["tool", "final"]
    tool_name: Optional[str] = None
    tool_args: Optional[Dict[str, Any]] = None
    response: Optional[str] = None

    @field_validator("tool_args", mode="before")
    @classmethod
    def default_tool_args(cls, v):
        return v or {}