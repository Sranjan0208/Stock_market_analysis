import yfinance as yf
import os
import pandas as pd
from config import STOCK_SYMBOLS


def fetch_stock_data(symbol, start=None, end=None):
    # Fetch data using yfinance
    df = yf.download(symbol, start=start, end=end)
    return df


def save_data(symbol, df):
    # Reset the index to avoid saving 'Ticker' as a row
    df.reset_index(inplace=True)
    # Ensure columns have correct names
    df.rename(columns={"Date": "Date"}, inplace=True)
    df.to_csv(f"data/raw/{symbol}.csv", index=False)  # Save without index
    print(f"Data for {symbol} saved successfully.")


def collect_data(start=None, end=None):
    os.makedirs("data/raw", exist_ok=True)
    for symbol in STOCK_SYMBOLS:
        df = fetch_stock_data(symbol, start=start, end=end)
        if df.empty:
            print(f"No data found for {symbol}.")
            continue
        save_data(symbol, df)
