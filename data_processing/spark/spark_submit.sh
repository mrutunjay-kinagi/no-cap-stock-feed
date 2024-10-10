#!/bin/bash
# Submit the Spark job
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 /app/data_processing/spark_processor.py
