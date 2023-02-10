from fastapi import APIRouter, status
from pydantic import BaseModel
from ..db.client import db_client
from ..db.models.data import Data
from ..db.schemas.Data import data_schemas

router = APIRouter(prefix="/Data",
                   tags=["Data"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})




@router.get("/")
async def hello():
    return {"Hello": "Activate"}


@router.post("/", response_model= Data, status_code=status.HTTP_201_CREATED)
async def receive(data: Data):

    Data_Dict = dict(data)
    del Data_Dict["id"]

    id = db_client.local.Data.insert_one(Data_Dict).inserted_id

    new_data = data_schemas(db_client.local.Data.find_one({"_id": id}))

    return Data(**new_data)

