from fastapi import APIRouter, status
from datetime import datetime
from pydantic import BaseModel
from pytz import timezone
import pytz
from app.db.client import db_client
from app.db.models.data import Data, Name
from app.db.schemas.Data import data_schemas

router = APIRouter(prefix="/Data",
                   tags=["Data"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})




@router.get("/")
async def hello():
    return {"Hello": "Activate"}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def receive(data: Name):

    Data_Dict = dict(data)
    Data_Dict2 = dict(Data_Dict["DATA"])
    now_utc = datetime.now(timezone('UTC'))
    now_Bogota = now_utc.astimezone(pytz.timezone('America/Bogota'))
    Data_Dict2["time"] = str(now_Bogota)

    id = db_client.local.Data.insert_one(Data_Dict2).inserted_id

