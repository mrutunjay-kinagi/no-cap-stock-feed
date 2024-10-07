#!/bin/bash

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
sleep 5

# Create a Kafka topic named 'stock-data'
kafka-topics --create --topic stock-data --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1

echo "Kafka topic 'stock-data' created."
