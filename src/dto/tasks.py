from pydantic import BaseModel


class InputTaskDTO(BaseModel):
    name: str
    dependencies: list[str]
