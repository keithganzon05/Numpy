import numpy as np
A = np.arange(1,101).reshape(10,10)
B = A**2
DivI = B % 3
DivF = B[DivI == 0]
print(B)
print("The elements that are divisible by 3: ")
print(DivF)