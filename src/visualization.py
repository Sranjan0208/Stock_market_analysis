# src/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_stock(symbol):
    # Load processed data
    df = pd.read_csv(
        f"data/processed/{symbol}_processed.csv", index_col="Date", parse_dates=True)
    df = df.dropna()  # Drop rows with NaT if any exist

    plt.figure(figsize=(12, 6))

    # Plot adjusted closing price
    plt.plot(df.index, df['Adj Close'],
             label="Adjusted Close", color="blue", linewidth=1.5)

    # Plot 50-day moving average
    plt.plot(df.index, df['MA_50'], label="50-Day Moving Average",
             color="orange", linestyle="--")

    # Plot 20-day rolling volatility
    plt.plot(df.index, df['Volatility_20'],
             label="20-Day Volatility", color="red", linestyle="-.")

    # Add titles and labels
    plt.title(f'Stock Analysis for {symbol}', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price and Volatility', fontsize=12)
    plt.legend()

    # Show the plot
    plt.show()


def visualize_all():
    # Go through each processed stock data file and plot
    for filename in os.listdir("data/processed"):
        if filename.endswith("_processed.csv"):
            symbol = filename.split("_")[0]
            plot_stock(symbol)


if __name__ == "__main__":
    visualize_all()
