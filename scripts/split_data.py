import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("uv/data/data.csv")
print(df.head())

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

# target column label
X_train = df_train.drop(columns=['Label']).values
y_train = df_train['Label'].values

X_val = df_val.drop(columns=['Label']).values
y_val = df_val['Label'].values

X_test = df_test.drop(columns=['Label']).values
y_test = df_test['Label'].values

# <Visualisation> why not
plt.hist(y_train, bins=10, alpha=0.7, label='train')
plt.hist(y_val, bins=10, alpha=0.7, label='val')
plt.hist(y_test, bins=10, alpha=0.7, label='test')
plt.legend()
plt.title("Label distribution across splits")
plt.show()

# Saving in sepreat files
df_train.to_csv("uv/data/train.csv", index=False)
df_val.to_csv("uv/data/val.csv", index=False)
df_test.to_csv("uv/data/test.csv", index=False)
