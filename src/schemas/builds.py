from pydantic import BaseModel


class InputSchema(BaseModel):
    build: str
