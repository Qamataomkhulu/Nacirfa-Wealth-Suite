"""
fetch_jse_data.py
-----------------
Fetches data for selected JSE-listed stocks via Yahoo Finance.
"""

import yfinance as yf
import pandas as pd
import os

# Example tickers (add more later)
JSE_TICKERS = {
    "Naspers": "NPN.JO",
    "Sasol": "SOL.JO",
    "Standard Bank": "SBK.JO"
}

PERIOD = "1mo"
INTERVAL = "1d"

def fetch_jse_data(ticker):
    print(f"Fetching JSE stock: {ticker}")
    data = yf.download(ticker, period=PERIOD, interval=INTERVAL, progress=False)
    data.reset_index(inplace=True)
    data['symbol'] = ticker
    return data

def save_to_csv(df, ticker):
    os.makedirs("datahub/output", exist_ok=True)
    filename = f"datahub/output/{ticker}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved {ticker} data to {filename}")

def main():
    all_stocks = []
    for name, ticker in JSE_TICKERS.items():
        df = fetch_jse_data(ticker)
        save_to_csv(df, ticker)
        all_stocks.append(df)
    combined = pd.concat(all_stocks)
    print("\n--- JSE Summary ---")
    print(combined.groupby('symbol')['Close'].describe())

if __name__ == "__main__":
    main()

