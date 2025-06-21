from fastapi import FastAPI
from catboost import CatBoostClassifier
import pandas as pd
from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    income: float
    # добавь остальные поля из твоего датасета

app = FastAPI()

model = CatBoostClassifier()
model.load_model('models/catboost_model.cbm')

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])

    # Печатаем список всех признаков, которые модель ожидает
    print("Ожидаемые признаки:", model.feature_names_)

    # Проверяем, есть ли все нужные колонки
    missing = set(model.feature_names_) - set(df.columns)
    if missing:
        return {"error": f"Отсутствуют колонки: {missing}"}

    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
