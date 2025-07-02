from kafka import KafkaConsumer
import requests
import json
import os
import time

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
    print("🔄 Received from Kafka:", msg.value)
    time.sleep(0.01)
    payload = {"event": json.loads(msg.value), "sourcetype": "_json"}
    headers = {"Authorization": f"Splunk {os.getenv('SPLUNK_TOKEN', 'tokenhere')}"}
    requests.post(
        os.getenv("SPLUNK_HEC_LINK", "http://splunk:8088/services/collector"),
        json=payload,
        headers=headers,
        verify=False,
        timeout=5,
    )
