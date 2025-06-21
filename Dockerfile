# Базовый образ Python
FROM python:3.9-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем все файлы из текущей папки в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запуск приложения
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]