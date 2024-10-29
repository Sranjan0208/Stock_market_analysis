# src/data_processing.py
import pandas as pd
import os


def load_data(symbol):
    # Load the data and specify that the 'Date' column should be treated as the index
    df = pd.read_csv(f"data/raw/{symbol}.csv", parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return df


def preprocess_data(df):
    df.columns = df.columns.str.strip()  # Remove any whitespace around column names
    # Convert index to datetime
    df.index = pd.to_datetime(df.index, errors='coerce')
    # Convert all other data to numeric
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.sort_index()  # Sort by date
    return df


def process_and_save(symbol):
    df = load_data(symbol)
    df = preprocess_data(df)

    # Ensure you're keeping relevant columns
    df = df[['Adj Close', 'Volume']]  # Keep only relevant columns

    # If you need to compute volatility, do so here.
    df['MA_50'] = df['Adj Close'].rolling(window=50).mean()
    df['Volatility_20'] = df['Adj Close'].rolling(window=20).std()

    df.to_csv(f"data/processed/{symbol}_processed.csv")


def process_all():
    os.makedirs("data/processed", exist_ok=True)
    for filename in os.listdir("data/raw"):
        symbol = filename.split(".")[0]
        df = load_data(symbol)
        print(df.head())
        process_and_save(symbol)
