from sklearn.preprocessing import OneHotEncoder, StandardScaler
from scipy.sparse import hstack
import numpy as np


def preprocess_data(df, encoder=None, scaler=None, categorical_cols=None):
    """Предобработка данных"""
    # Если категориальные колонки не заданы — определяем их автоматически
    if categorical_cols is None:
        categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Заполняем пропуски и приводим к строке
    df[categorical_cols] = df[categorical_cols].fillna("MISSING").astype(str)

    # Кодируем категориальные признаки
    if encoder is None:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=True)
        X_cat = encoder.fit_transform(df[categorical_cols])
    else:
        X_cat = encoder.transform(df[categorical_cols])

    # Обрабатываем числовые признаки
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    X_num = df[numeric_cols].fillna(0)

    if scaler is None:
        scaler = StandardScaler()
        X_num_scaled = scaler.fit_transform(X_num)
    else:
        X_num_scaled = scaler.transform(X_num)

    # Склеиваем всё в один массив
    X = hstack([X_num_scaled, X_cat])
    return X, encoder, scaler
