import numpy as np
A = np.arange(1,101).reshape(10,10)
B = A**2
C = B % 3
D = B[C == 0]
print(B)
print("The elements that are divisible by 3: ")
print(D)