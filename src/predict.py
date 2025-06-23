import numpy as np
from src.data.data_loader import DataLoader

def predict(data):
    """Предсказывает вероятность дефолта по данным клиента"""
    try:
        loader = DataLoader()
        X = loader.preprocess(data)
        model = loader.get_model()
        proba = model.predict_proba(X)[0][1]
        return {"probability": float(np.round(proba, 4))}
    except Exception as e:
        return {"error": f"Ошибка предсказания: {str(e)}"}
