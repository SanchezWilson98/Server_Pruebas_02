from pydantic import BaseModel

class Data(BaseModel):
    id: str and None
    name: str
    data: list

