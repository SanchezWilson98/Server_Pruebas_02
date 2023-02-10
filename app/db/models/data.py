from pydantic import BaseModel

class Data(BaseModel):
    id: str or None
    name: str
    data: list

