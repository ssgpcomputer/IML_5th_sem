import numpy as np 
import pandas as pd

lists = [1,2,3,4,5]

array = np.array(lists)

print("Numpy array is :")
print(array)

# converting the NumPy array 
# to a Pandas series
series = pd.Series(array) 

# displaying the Pandas series
print("Pandas Series : ")
print(series)