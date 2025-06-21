import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # Пример загрузки модели
    model_url = "https://drive.google.com/drive/folders/1kA2PSwoDWcG8XYN204ReaVAYT9sRtSj2?hl=ru"
    
    print("Загружаем модель...")
    download_file(model_url, "models/catboost_model.cbm")

    print("Готово!")