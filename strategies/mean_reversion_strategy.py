"""
mean_reversion_strategy.py
--------------------------
Simple mean reversion:
- Buy when price < MA
- Sell when price > MA
"""

import pandas as pd

def mean_reversion(data, window=20):
    df = data.copy()
    df['MA'] = df['close'].rolling(window=window).mean()
    df['signal'] = 0
    df.loc[df['close'] < df['MA'], 'signal'] = 1   # buy
    df.loc[df['close'] > df['MA'], 'signal'] = -1  # sell

    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']

    performance = {
        'Total Return (%)': df['strategy_returns'].sum() * 100,
        'Sharpe Ratio': df['strategy_returns'].mean() / df['strategy_returns'].std() * (252 ** 0.5)
    }

    return df, performance

if __name__ == "__main__":
    df = pd.read_csv("datahub/output/BTC_USDT.csv")
    results, perf = mean_reversion(df)
    print("📊 Mean Reversion Performance:")
    print(perf)

