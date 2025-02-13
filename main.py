import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
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
    
    # Print the last few rows of data
    print(df[['Close', 'SMA_20', 'RSI_14']].tail())
    
    # Plot Close and SMA
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close', color='blue')
    plt.plot(df.index, df['SMA_20'], label='SMA 20', color='orange')
    plt.title('AAPL Close Price & 20-Day SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Optionally, plot RSI in a separate figure
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df['RSI_14'], label='RSI 14', color='purple')
    plt.title('AAPL 14-Day RSI')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.axhline(70, color='red', linestyle='--', linewidth=1)
    plt.axhline(30, color='green', linestyle='--', linewidth=1)
    plt.legend()
    plt.grid(True)
    plt.show()

