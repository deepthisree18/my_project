import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from underwriting.data_loader import load_data, save_results
from underwriting.rules_engine import apply_rules
from underwriting.ml_model import train_model

def main():
    df = load_data("data/train.csv")

    df = apply_rules(df)

    print("\n📋 Sample decisions:")
    print(df[["id", "Annual_Premium", "Vehicle_Damage", "Underwriting_Decision"]].head(10))

    save_results(df, "data/underwriting_results.csv")

    model = train_model(df)

if __name__ == "__main__":
    main()
