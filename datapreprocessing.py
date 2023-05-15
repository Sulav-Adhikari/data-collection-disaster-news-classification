import pandas as pd
import csv
import re
from itertools import groupby

# Read the CSV file into a pandas DataFrame disaster
df = pd.read_csv('twt.csv')
df["Tweet"] = df["Tweet"].str.replace(" ", "").str.lower()
df["Tweet"] = df["Tweet"].apply(lambda x: re.sub(r"[^\w\s]", "", x))
df["Tweet"] = df.drop_duplicates(subset="Tweet")
df.to_csv("modified_tweets.csv", index=False)










