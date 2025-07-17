import numpy as np

Arr = [4.2, 94.3, 6.4, 0.6, 8.9, 7.7]

y = np.array(Arr)
print("Original array:", end=" ")
print(y)


y = np.rint(y)
print("After rounding off:", end=" ")
print(y)