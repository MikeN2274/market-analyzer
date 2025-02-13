import pandas as pd
import yfinance as yf
from indicators import compute_sma, compute_rsi

def fetch_data(ticker):
    # Fetch one month of data for the given ticker
    data = yf.download(ticker, period="1mo")
    return data

if __name__ == "__main__":
    df = fetch_data("AAPL")
    
    # Compute the 20-day Simple Moving Average and 14-day RSI
    df['SMA_20'] = compute_sma(df, window=20)
    df['RSI_14'] = compute_rsi(df, window=14)
    
    # Print the closing prices along with computed indicators
    print(df[['Close', 'SMA_20', 'RSI_14']].tail())

