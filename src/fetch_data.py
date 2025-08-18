from pathlib import Path
import os, io
import pandas as pd
import requests, certifi

DATA_DIR = Path("data"); DATA_DIR.mkdir(parents=True, exist_ok=True)
OUT = DATA_DIR / "diabetes.csv"
URL = os.environ.get(
    "DIABETES_CSV_URL",
    "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
)

def main():
    if OUT.exists():
        print("Data already present:", OUT)
        return
    try:
        print(f"Downloading CSV from: {URL}")
        r = requests.get(URL, timeout=30, verify=certifi.where())
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        df.to_csv(OUT, index=False)
        print(f"Saved {OUT} ({len(df)} rows)")
    except Exception as e:
        print("\nAuto-download failed. Options:")
        print("  A) Set DIABETES_CSV_URL to a direct CSV link and re-run.")
        print("  B) Manually download the CSV and place it at data/diabetes.csv")
        raise

if __name__ == "__main__":
    main()
