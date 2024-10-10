# Project Overview:

## no-cap-stock-feed

A data pipeline to process real-time stock market data using Kafka, Spark, and Apache Iceberg with dbt for transformations and Prefect for orchestration.

The idea is to build a real-time stock market data pipeline that streams live stock price data, processes it for analytics (e.g., calculating moving averages, identifying trends), and stores it for reporting and analysis. This project integrates tools like Kafka, Spark, Airbyte, dbt, and more.

## High-Level Architecture:
1. **Data Ingestion (Kafka):** Stream live stock market data.
2. **Data Processing (Spark):** Real-time data processing (e.g., compute moving averages, aggregate data).
3. **Data Storage (Iceberg):** Store the processed data in a data lake.
4. **ETL/ELT (Airbyte or Fivetran):** Bring in external datasets (e.g., company info, historical stock data).
5. **Data Transformation (dbt):** Transform raw data into analytical models.
6. **Orchestration (Prefect or Dagster):** Manage and schedule data pipeline workflows.
7. **Data Validation (Great Expectations):** Ensure data quality at each stage.

## Testing the Project

### Step 1: Create Docker Network
```bash
docker network create stock-network
```
### Step 2: Start the services
```bash
docker-compose up --build
```
### Step 3: Test Kafka Producer
To view the data being sent to Kafka:
```bash
docker exec -it kafka-producer-1 /bin/bash
python /app/producer.py
```

### Step 4: Test Kafka Consumer
To view the data being received from Kafka:
```bash
docker exec -it kafka-consumer-1 /bin/bash
python /app/consumer.py
```

### Step 5: Test Spark Processor
Check Spark logs to confirm that the streaming data is being processed correctly:
```bash
docker logs spark-processor-1
```