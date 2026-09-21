import pandas as pd
from config import CSV_FILE


def extract_data():
    df = pd.read_csv(CSV_FILE)

    print("Data extracted successfully")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    return df