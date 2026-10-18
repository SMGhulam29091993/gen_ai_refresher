from pydantic import BaseModel, Field

class CreateAgent(BaseModel):
    model: str
    tools: list
    system_prompt: str
    

