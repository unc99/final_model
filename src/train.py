
from catboost import CatBoostClassifier
import os
from sklearn.model_selection import train_test_split  # <-- добавлено
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from scipy.sparse import hstack
import numpy as np
def train_model(
    df, target_col="1.9", model_path="models/catboost_model.cbm"
):
    """Обучает модель и сохраняет её"""
    if target_col not in df.columns:
        raise ValueError(f"Целевая колонка '{target_col}' не найдена в датасете")

    # Предобработка: заполнение пропусков, преобразование типов
    categorical_cols = df.drop(columns=[target_col]).select_dtypes(include=["object"]).columns.tolist()
    df[categorical_cols] = df[categorical_cols].fillna("MISSING").astype(str)

    # Разделяем признаки и целевую переменную
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Определяем категориальные признаки
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

    # Разбиваем на трейн/тест
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Обучаем модель с указанием категориальных признаков
    model = CatBoostClassifier(
        iterations=100,
        depth=5,
        learning_rate=0.1,
        verbose=0,
        cat_features=categorical_cols
    )
    model.fit(X_train, y_train)

    # Сохраняем модель
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    model.save_model(model_path)
    print(f"✅ Модель сохранена в {model_path}")
    return model
