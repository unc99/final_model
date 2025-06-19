# src/monitor.py
import pandas as pd


def check_data_drift(train_df, new_df):
    """Проверяет средние значения признаков на сдвиг"""
    drift_report = {}
    for col in train_df.select_dtypes(include=[pd.np.number]).columns.tolist():
        mean_train = train_df[col].mean()
        mean_new = new_df[col].mean()
        drift_report[col] = {"train_mean": mean_train, "new_mean": mean_new}

    print("📊 Отчет по дрейфу данных:")
    for col, vals in drift_report.items():
        print(f"{col}: {vals}")


if __name__ == "__main__":
    from data_loader import load_data

    df = load_data()
    print("Форма датасета:", df.shape)
