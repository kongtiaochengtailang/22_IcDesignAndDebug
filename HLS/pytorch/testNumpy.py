import numpy as np

np.random.seed(1)
a = np.random.rand(6, 1, 5, 5)
print(a)
b = a.reshape(-1)
print(b)
