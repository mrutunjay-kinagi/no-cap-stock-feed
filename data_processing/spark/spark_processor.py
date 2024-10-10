from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, avg, window
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

# Initialize Spark session
spark = SparkSession \
    .builder \
    .appName("StockDataProcessor") \
    .getOrCreate()

# Define Kafka server and topic
kafka_brokers = "kafka:9092"
topic = "stock-data"

# Define the schema of the incoming data
stock_schema = StructType() \
    .add("symbol", StringType()) \
    .add("price", DoubleType()) \
    .add("timestamp", TimestampType())

# Read data from Kafka as a streaming DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", topic) \
    .option("startingOffsets", "latest") \
    .load()

# Convert the Kafka message value from bytes to string and parse it using the schema
stock_data = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), stock_schema).alias("data")) \
    .select("data.*")

# Compute a 5-minute moving average of the stock prices, grouped by stock symbol
moving_avg = stock_data \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window(col("timestamp"), "5 minutes"),
        col("symbol")
    ) \
    .agg(avg("price").alias("moving_average_price"))

# Function to log processed data
def log_data(batch_df, batch_id):
    print(f"Batch ID: {batch_id}")
    batch_df.show(truncate=False)  # Show the DataFrame contents

# Start the streaming query to continuously process the data
query = moving_avg \
    .select("window", "symbol", "moving_average_price") \
    .writeStream \
    .outputMode("update") \
    .foreachBatch(log_data).start()

# Await termination of the streaming query
query.awaitTermination()
