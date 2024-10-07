from kafka import KafkaConsumer
import json

KAFKA_TOPIC = 'stock-data'
KAFKA_SERVER = 'kafka:9092'

def consume_stock_data():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest', 
        enable_auto_commit=True
    )

    print("Listening for messages...")
    for message in consumer:
        print(f"Received message: {message.value}")

if __name__ == "__main__":
    consume_stock_data()
