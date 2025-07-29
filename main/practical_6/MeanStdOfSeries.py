import pandas as pd

lists = [1,2,3,4,5]

series = pd.Series(lists) 

mean = series.mean()
std = series.std()

print("Pandas Series : ")
print(series)

print(f"mean and standerd deviation is {mean} and {std}")