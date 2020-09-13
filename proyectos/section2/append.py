# -*- coding: utf-8 -*-

import pandas as pd
from glob import glob

if __name__=="__main__":
    files = glob("../../datasets/symbols/*.csv")
    full_df = None
    for f in files:
        print(f)
        df = pd.read_csv(f)
        symbol = f.split("/")[1].split(".")[0]
        df["Name"] = symbol
        if full_df is None:
            full_df = df
        else:
            full_df = full_df.append(df, ignore_index=True)
    full_df.to_csv("../../datasets/sp500full.csv", index=False)


