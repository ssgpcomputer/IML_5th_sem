import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
a,b,c=np.split(arr,[2,6])
print("2nd element to split",a)
print("4nd element to split",b)
print("8nd element to split",c)