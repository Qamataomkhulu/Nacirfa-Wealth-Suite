"""
fetch_crypto_data.py
---------------------
Fetches crypto data (BTC, ETH, SOL) from Binance using CCXT.
Saves data as CSV for backtesting or visualization.
"""

import ccxt
import pandas as pd
from datetime import datetime
import os

# Exchange setup
exchange = ccxt.binance({
    'enableRateLimit': True
})

# Coins and timeframe
SYMBOLS = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
TIMEFRAME = '1h'  # 1h, 4h, 1d, etc
LIMIT = 100  # number of candles to fetch

def fetch_ohlcv(symbol):
    """Fetch OHLCV (Open, High, Low, Close, Volume) data for a crypto pair."""
    print(f"Fetching {symbol} data...")
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=TIMEFRAME, limit=LIMIT)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['symbol'] = symbol
    return df

def save_to_csv(df, symbol):
    """Save the DataFrame to CSV in /datahub/output."""
    os.makedirs('datahub/output', exist_ok=True)
    filename = f"datahub/output/{symbol.replace('/', '_')}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved {symbol} data to {filename}")

def main():
    all_data = []
    for sym in SYMBOLS:
        df = fetch_ohlcv(sym)
        save_to_csv(df, sym)
        all_data.append(df)
    
    # Print summary
    combined = pd.concat(all_data)
    print("\n--- SUMMARY ---")
    print(combined.groupby('symbol')['close'].describe())

if __name__ == "__main__":
    main()

