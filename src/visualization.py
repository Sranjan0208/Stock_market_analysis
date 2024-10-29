# src/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_stock(symbol):
    # Load your data
    df = pd.read_csv(f"data/processed/{symbol}_processed.csv", index_col=0)
    # Ensure the index is datetime
    df.index = pd.to_datetime(df.index, errors='coerce')
    df = df.dropna()  # Drop NaT if any exist

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Adj Close'], label="Adjusted Closing Price")
    plt.title(f'Stock Prices for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def visualize_all():
    for filename in os.listdir("data/processed"):
        if "analysis" in filename:
            symbol = filename.split("_")[0]
            plot_stock(symbol)
