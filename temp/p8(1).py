import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Stk.csv')
print(df)
sd=pd.to_datetime('07/20/2025')
ed=pd.to_datetime('07/14/2025')

df['Date']=pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

fd=df.loc[sd:ed]
plt.figure(figsize=(15,10))
plt.scatter(fd.index,fd['Open'],label='Opening',marker='o',color='Green')
plt.scatter(fd.index,fd['Close'],label='Closing',marker='x',color='Red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show() 