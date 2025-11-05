"""
momentum_strategy.py
--------------------
Simple momentum strategy:
- Buy when short MA crosses above long MA
- Sell when it crosses below
"""

import pandas as pd

def momentum_strategy(data, short_window=10, long_window=30):
    """Returns signals and performance metrics for a simple MA crossover."""
    df = data.copy()
    df['MA_short'] = df['close'].rolling(window=short_window).mean()
    df['MA_long'] = df['close'].rolling(window=long_window).mean()

    df['signal'] = 0
    df.loc[df['MA_short'] > df['MA_long'], 'signal'] = 1  # buy
    df.loc[df['MA_short'] < df['MA_long'], 'signal'] = -1  # sell

    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['signal'].shift(1) * df['returns']

    performance = {
        'Total Return (%)': df['strategy_returns'].sum() * 100,
        'Sharpe Ratio': df['strategy_returns'].mean() / df['strategy_returns'].std() * (252 ** 0.5)
    }

    return df, performance

# Test run example
if __name__ == "__main__":
    df = pd.read_csv("datahub/output/BTC_USDT.csv")
    results, perf = momentum_strategy(df)
    print("📊 Strategy Performance:")
    print(perf)

