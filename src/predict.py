from catboost import CatBoostClassifier
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.preprocessing import OneHotEncoder


def predict(data):
    """Предсказывает вероятность дефолта по данным клиента"""
    try:
        # Преобразуем входные данные в DataFrame
        input_df = pd.DataFrame([data])

        # Список всех колонок (в нужном порядке!)
        expected_columns = [
            "1", "C", "5", "Web", "0", "1.1", "F", "6", "1.2", "0.1",
            "RN", "Assu", "1.3", "RN.1", "Santana do Matos", "Centro", "Y",
            "105", "1.4", "15", "N", "1.5", "900", "0.2", "1.6", "1.7",
            "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "N.1", " ",
            "NULL", "NULL.1", "N.2", " .1", "0.10", "9", "4", "NULL.2",
            "NULL.3", "0.11", "0.12", "0.13", "0.14", "1.8", "N.3", "32",
            "595", "595.1", "1.9"
        ]

        # Проверяем наличие всех нужных колонок
        missing_cols = set(expected_columns) - set(input_df.columns)
        if missing_cols:
            raise ValueError(f"Отсутствуют колонки: {missing_cols}")

        # Упорядочиваем колонки как в обучении
        input_df = input_df[expected_columns]

        # Определяем категориальные признаки
        categorical_cols = input_df.select_dtypes(include=["object"]).columns.tolist()

        # Заполняем пропуски и приводим к строке
        input_df[categorical_cols] = input_df[categorical_cols].fillna("MISSING").astype(str)

        # Кодируем категориальные признаки
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=True)
        X_cat = encoder.fit_transform(input_df[categorical_cols])

        # ВСЕГДА передавай категориальные признаки как есть, без числовых
        X = X_cat

        # Загружаем модель
        model = CatBoostClassifier()
        model.load_model("models/catboost_credit_scoring_model.cbm")

        # Предсказываем
        proba = model.predict_proba(X)[0][1]
        return {"probability": float(np.round(proba, 4))}

    except Exception as e:
        return {"error": f"Ошибка предсказания: {str(e)}"}
