"""
tracker.py
-----------
Portfolio Tracker:
- Reads a CSV of trades
- Calculates PnL and exposure
- Displays basic stats
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_trades(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def analyze_portfolio(df):
    df['PnL'] = (df['sell_price'] - df['buy_price']) * df['quantity']
    total_pnl = df['PnL'].sum()
    total_invested = (df['buy_price'] * df['quantity']).sum()
    roi = (total_pnl / total_invested) * 100

    print("\n--- Portfolio Summary ---")
    print(df.groupby('symbol')['PnL'].sum())
    print(f"💰 Total PnL: ${total_pnl:.2f}")
    print(f"📈 ROI: {roi:.2f}%")

    df.groupby('symbol')['PnL'].sum().plot(kind='bar', title='PnL by Symbol')
    plt.ylabel("Profit/Loss ($)")
    plt.show()

if __name__ == "__main__":
    # Example format: date,symbol,buy_price,sell_price,quantity
    df = load_trades("portfolio/sample_trades.csv")
    analyze_portfolio(df)

