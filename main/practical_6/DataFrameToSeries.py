import pandas as pd

lists = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}

df = pd.DataFrame(lists)

series = df['A']

print(df)
print()
print(series)
