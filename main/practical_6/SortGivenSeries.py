import pandas as pd 

lists = [99,55,35,48,5]

series = pd.Series(lists) 
print("Before Sorting:")
print(series)

sort = series.sort_values()
print("After Sorting:")
print(sort)