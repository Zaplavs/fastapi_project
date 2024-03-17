FROM python:3.11-slim

COPY . .

RUN pip instal -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]