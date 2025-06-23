from catboost import CatBoostClassifier
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class DataLoader:
    def __init__(self):
        self.expected_columns = [
            "1", "C", "5", "Web", "0", "1.1", "F", "6", "1.2", "0.1",
            "RN", "Assu", "1.3", "RN.1", "Santana do Matos", "Centro", "Y",
            "105", "1.4", "15", "N", "1.5", "900", "0.2", "1.6", "1.7",
            "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "N.1", " ",
            "NULL", "NULL.1", "N.2", " .1", "0.10", "9", "4", "NULL.2",
            "NULL.3", "0.11", "0.12", "0.13", "0.14", "1.8", "N.3", "32",
            "595", "595.1", "1.9"
        ]
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=True)
        self.model = self._load_model()

    def _load_model(self):
        model = CatBoostClassifier()
        model.load_model("models/catboost_credit_scoring_model.cbm")
        return model

    def preprocess(self, data):
        input_df = pd.DataFrame([data])

        missing_cols = set(self.expected_columns) - set(input_df.columns)
        if missing_cols:
            raise ValueError(f"Отсутствуют колонки: {missing_cols}")

        input_df = input_df[self.expected_columns]

        categorical_cols = input_df.select_dtypes(include=["object"]).columns.tolist()
        input_df[categorical_cols] = input_df[categorical_cols].fillna("MISSING").astype(str)

        X_cat = self.encoder.fit_transform(input_df[categorical_cols])
        return X_cat

    def get_model(self):
        return self.model
