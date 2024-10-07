import yfinance as yf
from kafka import KafkaProducer
import json
import time
import warnings
import os

warnings.filterwarnings("ignore", category=FutureWarning)

KAFKA_TOPIC = 'stock-data'
KAFKA_SERVER = 'kafka:9092'

def get_stock_data(stock_symbol):
    """Fetch the latest stock data for a given symbol."""
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(period="1d")
    latest_data = data.tail(1)
    
    # Handle case where no data is returned
    if latest_data.empty:
        print(f"No data found for {stock_symbol}.")
        return None
    
    return {
        "symbol": stock_symbol,
        "date": latest_data.index[0].strftime("%Y-%m-%d"),
        "open": latest_data["Open"].values[0],
        "high": latest_data["High"].values[0],
        "low": latest_data["Low"].values[0],
        "close": latest_data["Close"].values[0],
        "volume": int(latest_data["Volume"].values[0])
    }

def send_stock_data(producer, stock_symbol):
    """Send stock data to the Kafka topic."""
    stock_data = get_stock_data(stock_symbol)
    
    if stock_data: 
        producer.send(KAFKA_TOPIC, value=stock_data)
        print(f"Sent data: {stock_data}")
    else:
        print(f"Skipping sending data for {stock_symbol} due to no available data.")

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        send_stock_data(producer, 'AAPL')  # Sending Apple stock data
        time.sleep(60)  # Run every 60 seconds
