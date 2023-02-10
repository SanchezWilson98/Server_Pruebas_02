from fastapi import FastAPI
from .routers import data_receive

app = FastAPI()

app.include_router(data_receive.router)

@app.get("/")
async def hola():
    return {"Wilson":"Andres"}
