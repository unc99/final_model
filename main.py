from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from src.predict import predict

app = FastAPI(title="Credit Scoring API")


class ClientData(BaseModel):
    data: Dict[str, str]


@app.post("/predict/")
async def api_predict(client_data: ClientData):
    result = predict(client_data.data)
    return result
