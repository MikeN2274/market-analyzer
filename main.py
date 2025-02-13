import pandas as pd
import yfinance as yf

def fetch_data(ticker):
    # Fetch one month of data for the given ticker
    data = yf.download(ticker, period="1mo")
    return data

if __name__ == "__main__":
    df = fetch_data("AAPL")
    print(df.head())

