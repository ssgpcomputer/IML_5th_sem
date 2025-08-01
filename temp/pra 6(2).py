import pandas as pd 
df=pd.DataFrame({'A' : [10,20,30],
                    'B':[40,50,60]})
f_series=df['A']
print( f_series)