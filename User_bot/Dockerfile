# Используем базовый образ Python 3.11
FROM python:3.11 as base

WORKDIR /app

# Копируем файл зависимостей и устанавливаем зависимости
COPY User_bot/requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Устанавливаем команду запуска контейнера
CMD ["python", "User_bot/aiogrambot.py"]
