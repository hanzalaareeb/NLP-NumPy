import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# specifying data as pandas

data = pd.read_csv('uv/data/train.csv')
# print(data.head())

# creat numpy array

data = np.array(data)
m, n = data.shape
print(m, n)
np.random.shuffle(data)

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_dev[0]
X_train = data_dev[1:n]

print(Y_train, X_train[:, 0].shape)

# setting up all the parameter