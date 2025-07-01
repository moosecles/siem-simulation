from kafka import KafkaConsumer
import requests
import json
import os

while True:
    try:
        consumer = KafkaConsumer(
            os.getenv("KAFKA_TOPIC_NAME", "logs"),
            bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP", "kafka:9092"),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
        )
        break  # On Success
    except Exception as e:
        print(f"Kafka not ready yet: {e}")

for msg in consumer:
    payload = {"event": json.loads(msg.value), "sourcetype": "_json"}
    headers = {
        "Authorization": f"Splunk {os.getenv('SPLUNK_TOKEN', 'ffd507e4-1257-4cf8-be93-4b9387b6a9ba')}"
    }
    requests.post(
        os.getenv("SPLUNK_HEC_LINK", "http://splunk:8088/services/collector"),
        json=payload,
        headers=headers,
        verify=False,
    )
