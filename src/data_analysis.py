# src/data_analysis.py
import pandas as pd
import os


def calculate_moving_average(df, window):
    # Changed 'Close' to 'Adj Close'
    return df['Adj Close'].rolling(window=window).mean()


def calculate_volatility(df, window):
    return df['Adj Close'].rolling(window=window).std()


def analyze_data(symbol):
    df = pd.read_csv(f"data/processed/{symbol}_processed.csv", index_col=0)
    df['MA_50'] = calculate_moving_average(df, 50)

    # Example calculation of volatility
    df['Volatility_20'] = df['Adj Close'].rolling(window=20).std()

    return df


def save_analysis(symbol):
    df = analyze_data(symbol)
    df.to_csv(f"data/processed/{symbol}_analysis.csv")


def run_analysis():
    for filename in os.listdir("data/processed"):
        if "processed" in filename:
            symbol = filename.split("_")[0]
            save_analysis(symbol)
