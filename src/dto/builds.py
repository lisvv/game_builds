from pydantic import BaseModel


class BuildDTO(BaseModel):
    name: str
    tasks: list[str]
