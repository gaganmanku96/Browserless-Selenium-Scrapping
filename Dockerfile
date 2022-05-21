FROM python:3.9.6-slim-buster

WORKDIR /scrapper

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "main.py"]
