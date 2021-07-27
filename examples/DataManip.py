import pandas as pd

df = pd.read_csv("merged.csv")
df = df.iloc[: , 1:]
print(df.head())