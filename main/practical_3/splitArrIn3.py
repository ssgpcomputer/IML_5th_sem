import numpy as np 

Arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

NpArr = np.array(Arr)

NpSplit1 = np.array_split(NpArr,(2,6))

print(NpSplit1)



