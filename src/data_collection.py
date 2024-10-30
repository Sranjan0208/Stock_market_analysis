import yfinance as yf
import os
import pandas as pd
from config import STOCK_SYMBOLS


def fetch_stock_data(symbol, start=None, end=None):
    df = yf.download(symbol, start=start, end=end)
    return df


def save_data(symbol, df):
    df.reset_index(inplace=True)
    df.rename(columns={"Date": "Date"}, inplace=True)
    df.to_csv(f"data/raw/{symbol}.csv", index=False)
    print(f"Data for {symbol} saved successfully.")


def collect_data(start=None, end=None):
    os.makedirs("data/raw", exist_ok=True)
    for symbol in STOCK_SYMBOLS:
        df = fetch_stock_data(symbol, start=start, end=end)
        if df.empty:
            print(f"No data found for {symbol}.")
            continue
        save_data(symbol, df)
