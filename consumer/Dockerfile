FROM python:3.9-slim
WORKDIR /consumer

COPY consumer.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "consumer.py"]
