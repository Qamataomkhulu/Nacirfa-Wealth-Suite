"""
fetch_fx_data.py
----------------
Fetches forex data (USD/ZAR, EUR/USD, GBP/USD) from Yahoo Finance.
Saves as CSV for later analysis.
"""

import yfinance as yf
import pandas as pd
import os

PAIRS = ['USDZAR=X', 'EURUSD=X', 'GBPUSD=X']
PERIOD = '1mo'  # 1d, 5d, 1mo, 3mo, 6mo, 1y
INTERVAL = '1h'

def fetch_fx(pair):
    print(f"Fetching FX pair: {pair}")
    data = yf.download(pair, period=PERIOD, interval=INTERVAL, progress=False)
    data.reset_index(inplace=True)
    data['symbol'] = pair
    return data

def save_to_csv(df, pair):
    os.makedirs('datahub/output', exist_ok=True)
    filename = f"datahub/output/{pair.replace('=X','')}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved {pair} data to {filename}")

def main():
    all_pairs = []
    for pair in PAIRS:
        df = fetch_fx(pair)
        save_to_csv(df, pair)
        all_pairs.append(df)
    combined = pd.concat(all_pairs)
    print("\n--- FX Summary ---")
    print(combined.groupby('symbol')['Close'].describe())

if __name__ == "__main__":
    main()

