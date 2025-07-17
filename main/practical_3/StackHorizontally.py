import numpy as np

a = [2,5,7,8]
b = [4,8,1,9]

a = np.array(a)
b = np.array(b)

c = np.hstack((a,b))

print(c)