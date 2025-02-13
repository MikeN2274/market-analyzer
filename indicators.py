import pandas as pd
import numpy as np

def compute_sma(data, window=20):
    """
    Compute the Simple Moving Average (SMA) for the 'Close' prices.
    :param data: DataFrame containing a 'Close' column.
    :param window: Number of periods for the SMA.
    :return: A pandas Series containing the SMA.
    """
    return data['Close'].rolling(window=window).mean()

def compute_rsi(data, window=14):
    """
    Compute the Relative Strength Index (RSI) for the 'Close' prices.
    :param data: DataFrame containing a 'Close' column.
    :param window: Number of periods to use for RSI calculation.
    :return: A pandas Series containing the RSI.
    """
    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()
    
    # Prevent division by zero
    avg_loss.replace(0, 1e-10, inplace=True)
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

