from pydantic import BaseModel
from typing import Union

class Data(BaseModel):
    name : str
    data0: str
    data1: str
    data2: str
    data3: str
        
class Name(BaseModel):
    DATA: (Union[Data, None]) = None

