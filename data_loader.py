import pandas as pd

def load_data(path):
    print("📥 Loading data...")
    return pd.read_csv(path)

def save_results(df, path):
    df.to_csv(path, index=False)
    print(f"💾 Results saved to: {path}")
