# src/data_analysis.py
import pandas as pd
import os


def load_processed_data(symbol):
    """Load processed stock data for a specific symbol."""
    return pd.read_csv(f"data/processed/{symbol}_processed.csv", parse_dates=["Date"], index_col="Date")


def analyze_trend(df):
    """Analyze trends using moving averages."""
    # Define trend based on 50-day moving average
    df['Trend'] = df['Adj Close'] > df['MA_50']
    trend_periods = df['Trend'].value_counts()
    trend_changes = df['Trend'].astype(int).diff(
    ).abs().sum() / 2  # Counts change in trends

    trend_summary = {
        "Total Uptrend Days": trend_periods.get(True, 0),
        "Total Downtrend Days": trend_periods.get(False, 0),
        "Trend Changes": int(trend_changes)
    }
    return trend_summary


def analyze_volatility(df):
    """Analyze periods of high volatility using the 20-day rolling standard deviation."""
    high_volatility_threshold = df['Volatility_20'].mean(
    ) + df['Volatility_20'].std()
    high_volatility_periods = df[df['Volatility_20']
                                 > high_volatility_threshold]

    volatility_summary = {
        "High Volatility Days": high_volatility_periods.shape[0],
        "Max Volatility": high_volatility_periods['Volatility_20'].max(),
        "Average Volatility": df['Volatility_20'].mean()
    }
    return volatility_summary


def analyze_data(symbol):
    """Run analysis for a given stock symbol."""
    df = load_processed_data(symbol)

    trend_summary = analyze_trend(df)
    volatility_summary = analyze_volatility(df)

    # Combine the results
    analysis_summary = {
        "Symbol": symbol,
        "Trend Analysis": trend_summary,
        "Volatility Analysis": volatility_summary
    }

    # Print findings
    print(f"Analysis for {symbol}:")
    print("Trend Summary:", trend_summary)
    print("Volatility Summary:", volatility_summary)
    print("=" * 50)
    return analysis_summary


def analyze_all():
    """Run analysis for all processed stock data files."""
    for filename in os.listdir("data/processed"):
        symbol = filename.split("_")[0]
        analyze_data(symbol)


if __name__ == "__main__":
    analyze_all()
