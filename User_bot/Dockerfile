FROM python:3.11 as base

WORKDIR /app

COPY User_bot/requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "User_bot/aiogrambot.py"]
