from fastapi import FastAPI
from catboost import CatBoostClassifier
import pandas as pd
from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    income: float
    # добавь остальные поля из твоего датасета

app = FastAPI()

# Загружаем модель
model = CatBoostClassifier()
model.load_model('models/catboost_model.cbm')  # проверь имя файла

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}