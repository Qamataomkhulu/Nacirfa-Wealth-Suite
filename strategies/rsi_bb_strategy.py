"""
rsi_bb_strategy.py
------------------
RSI + Bollinger Bands combo strategy.
"""

import pandas as pd

def rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def bollinger_bands(series, window=20, num_std=2):
    ma = series.rolling(window).mean()
    std = series.rolling(window).std()
    upper = ma + (std * num_std)
    lower = ma - (std * num_std)
    return ma, upper, lower

def rsi_bb_strategy(data):
    df = data.copy()
    df['RSI'] = rsi(df['close'])
    df['MA'], df['Upper'], df['Lower'] = bollinger_bands(df['close'])

    df['signal'] = 0
    df.loc[(df['RSI'] < 30) & (df['close'] < df['Lower']), 'signal'] = 1   # Buy
    df.loc[(df['RSI'] > 70) & (df['close'] > df['Upper']), 'signal'] = -1  # Sell

    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']

    performance = {
        'Total Return (%)': df['strategy_returns'].sum() * 100,
        'Sharpe Ratio': df['strategy_returns'].mean() / df['strategy_returns'].std() * (252 ** 0.5)
    }

    return df, performance

if __name__ == "__main__":
    df = pd.read_csv("datahub/output/ETH_USDT.csv")
    results, perf = rsi_bb_strategy(df)
    print("📊 RSI + Bollinger Bands Performance:")
    print(perf)

