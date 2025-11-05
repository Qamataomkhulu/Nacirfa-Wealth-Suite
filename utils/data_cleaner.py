"""
data_cleaner.py
---------------
Data cleaning and validation utilities.
"""

import pandas as pd

def clean_dataframe(df):
    df = df.dropna()
    df = df.drop_duplicates()
    if 'timestamp' in df.columns:
        df = df.sort_values('timestamp')
    return df.reset_index(drop=True)

def validate_columns(df, required_cols):
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True

if __name__ == "__main__":
    sample = pd.DataFrame({'timestamp': [1, 2, 2], 'close': [100, None, 105]})
    clean = clean_dataframe(sample)
    print(clean)

