FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8001
ENV ALLOWED_HOSTS="*"
ENV MAX_WORKERS=4

CMD uvicorn api:app --host 0.0.0.0 --port ${PORT} --workers ${MAX_WORKERS} --proxy-headers --forwarded-allow-ips "*"