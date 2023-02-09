from pydantic import BaseModel

class Data(BaseModel):
    id: str | None
    name: str
    data: list

