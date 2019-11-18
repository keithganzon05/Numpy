import numpy as np
X = np.random.random((5,5))
S = X.std()
M = X.mean()
Z = (X - M)/S
print('The value of the normalized X: ')
print(Z)