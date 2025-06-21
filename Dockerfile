# Базовый образ Python
FROM python:3.10-slim

# Рабочая директория
WORKDIR /app

# Копируем файлы
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запуск сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]