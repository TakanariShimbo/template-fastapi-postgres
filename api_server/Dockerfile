FROM python:3.11-slim

WORKDIR /work

COPY . .

RUN export $(grep -v '^#' .env | xargs)

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]