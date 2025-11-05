"""
pnl_analysis.py
---------------
Loads multiple strategy results and compares their performance.
"""

import pandas as pd
import matplotlib.pyplot as plt

def compare_strategies(files):
    summary = []
    for f in files:
        df = pd.read_csv(f)
        total_return = df['strategy_returns'].sum() * 100
        sharpe = df['strategy_returns'].mean() / df['strategy_returns'].std() * (252 ** 0.5)
        summary.append({'strategy': f, 'Total Return (%)': total_return, 'Sharpe': sharpe})

    result = pd.DataFrame(summary)
    print(result)
    result.plot(x='strategy', y='Total Return (%)', kind='bar', title='Strategy Comparison')
    plt.show()

if __name__ == "__main__":
    compare_strategies([
        "datahub/output/BTC_USDT.csv",
        "datahub/output/ETH_USDT.csv"
    ])

