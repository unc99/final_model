# Используем базовый образ Python
FROM python:3.10-slim

# Установим рабочую директорию
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Устанавливаем проект как пакет
RUN pip install -e .

# Запускаем приложение
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]