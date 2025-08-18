from pathlib import Path
import pandas as pd

DATA_DIR = Path("data"); DATA_DIR.mkdir(parents=True, exist_ok=True)
URL = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
out = DATA_DIR / "diabetes.csv"
if not out.exists():
    df = pd.read_csv(URL)
    df.to_csv(out, index=False)
    print("Saved", out)
else:
    print("Data already present:", out)
