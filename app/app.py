# app/app.py
from fastapi import FastAPI
from src.api.schemas import ClientData  # ← проверяем этот импорт
from src.predict import predict

app = FastAPI()

@app.post("/predict")
def predict_api(data: ClientData):
    result = predict(data.dict())
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
