import pandas as pd
import zipfile


def load_data(zip_path="data/PAKDD2010.zip"):
    """Загружает обучающий датасет"""
    with zipfile.ZipFile(zip_path, "r") as outer_zip:
        inner_zip_path = "PAKDD 2010/PAKDD-2010 training data.zip"
        with outer_zip.open(inner_zip_path) as inner_zip_file:
            inner_zip = zipfile.ZipFile(inner_zip_file)
            with inner_zip.open("PAKDD2010_Modeling_Data.txt") as file:
                df = pd.read_csv(file, sep="\t", encoding="latin1", low_memory=False)
    return df


if __name__ == "__main__":
    df = load_data()
    print("Форма датасета:", df.shape)
