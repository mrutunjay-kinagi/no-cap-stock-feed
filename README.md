# Project Overview: 

## no-cap-stock-feed

A data pipeline to process real-time stock market data using Kafka, Spark, and Apache Iceberg with dbt for transformations and Prefect for orchestration.


Idea is to build a real-time stock market data pipeline that streams live stock price data, processes it for analytics (e.g., calculating moving averages, identifying trends), and stores it for reporting and analysis. This project will integrate tools like Kafka, Spark, Airbyte, dbt, and more.

## High-Level Architecture:
1. Data Ingestion (Kafka): Stream live stock market data.
2. Data Processing (Spark): Real-time data processing (e.g., compute moving averages, aggregate data).
3. Data Storage (Iceberg): Store the processed data in a data lake.
4. ETL/ELT (Airbyte or Fivetran): Bring in external datasets (e.g., company info, historical stock data).
5. Data Transformation (dbt): Transform raw data into analytical models.
6. Orchestration (Prefect or Dagster): Manage and schedule data pipeline workflows.
7. Data Validation (Great Expectations): Ensure data quality at each stage.



## Testing the Project
- Start the services with `docker-compose up --build`.
- Run docker exec -it kafka-producer-1 /bin/bash python /app/producer.py - to see sent data
- Run docker exec -it kafka-consumer-1 /bin/bash python /app/consumer.py - to see recieved data

