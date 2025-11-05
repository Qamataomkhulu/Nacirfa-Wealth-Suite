"""
visualizer.py
--------------
Generic visualization helper for Nacirfa Wealth Suite.
"""

import pandas as pd
import plotly.express as px

def plot_price(df, title="Price Chart"):
    fig = px.line(df, x='timestamp', y='close', title=title)
    fig.show()

def plot_rsi(df):
    if 'RSI' in df.columns:
        fig = px.line(df, x='timestamp', y='RSI', title="RSI Indicator")
        fig.show()
    else:
        print("⚠️ RSI not found in DataFrame.")

if __name__ == "__main__":
    df = pd.read_csv("datahub/output/BTC_USDT.csv")
    plot_price(df, "BTC/USD 1h Chart")

