from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    build: str = Field(example="forward_interest")
