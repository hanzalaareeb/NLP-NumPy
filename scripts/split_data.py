import pandas as pd
import numpy as np

df = pd.read_csv("uv/data/data.csv")
# print(df.head())

# shuffling the data set
df = df.sample(frac=1, random_state=42).reset_index(drop=True) # rn done on every run

# Split data set 
# Traing = 70% ~ 19600
# validation = 15% ~ 4200
# Testing = 15% ~ 4200
train_frac = 0.7
val_frac = 0.15

n = len(df)
train_end = int(train_frac * n)
val_end = int((train_frac + val_frac) * n)

df_train = df.iloc[:train_end]
df_val = df.iloc[train_end:val_end]
df_test = df.iloc[val_end:]

print(len(df_train), len(df_val), len(df_test))

