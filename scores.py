import os
import pandas as pd


def save_score(model, mae, r2, csv_path):
    """Add or update model accuracy in the file given by csv_path."""
    cols = ["mae", "r2"]
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, index_col=0)
    else:
        df = pd.DataFrame(columns=cols)

    if model in df.index:
        df.loc[model][cols] = [round(mae, 12), round(r2, 12)]
    else:
        df1 = pd.DataFrame.from_dict({model: [round(mae, 12), round(r2, 12)]}, orient="index", columns=cols)
        df = df.append(df1)

    df.index.name = "model"
    df.to_csv(csv_path)
