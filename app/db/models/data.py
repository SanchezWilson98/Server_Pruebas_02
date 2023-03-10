from pydantic import BaseModel
from typing import Union

class Data(BaseModel):
    name : str
    node : str
    data: str

class Name(BaseModel):
    DATA: (Union[Data, None]) = None

