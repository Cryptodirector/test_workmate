FROM python:3.11-slim

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN alembic upgrade head

COPY . .

# Запуск парсера
RUN python app/utils/parser.py

# Запуск FastAPI приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
