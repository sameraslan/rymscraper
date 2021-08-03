import os, glob
import pandas as pd

# Merge CSVs and then do data manipulation
'''path = "/Users/saslan.19/Desktop/Programming/Music Recommendation/RYMScraper/examples/Exports"
all_files = sorted(glob.glob(os.path.join(path, "*.csv")))
print(all_files)

df_from_each_file = (pd.read_csv(f, sep=None, engine='python') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "merged.csv")'''

df = pd.read_csv("merged.csv")
#Removes left column of unnecessary rank
df = df.iloc[: , 1:]

#Since column name RYM Rating has a space replace space with underscore
df.columns = [c.replace(' ', '_') for c in df.columns]
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfAbove1K = (df[df.Ratings >= 1000])
dfAbove1K.to_csv('Above1kRatings.csv')
print(len(dfAbove1K))