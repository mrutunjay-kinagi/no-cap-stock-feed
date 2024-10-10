FROM openjdk:8

# Install PySpark
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


# Copy the Spark processor script into the container
COPY spark_processor.py /app/spark_processor.py

WORKDIR /app

# Run the Spark processing script with Spark-Kafka package
CMD ["/usr/local/bin/spark-submit", \
     "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0", \
     "spark_processor.py"]
