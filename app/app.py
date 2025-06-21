# app.py
import sys
import os

# Добавляем src в PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fastapi import FastAPI
from src.predict import predict


app = FastAPI()

@app.post("/predict")
def predict_api(data: dict):
    result = predict(data)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
