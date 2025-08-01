import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv(r"D:\code\main\practical_8\GoogleStockPrices.csv", parse_dates=["Date"])
df.set_index('Date', inplace=True)

start = pd.to_datetime('2020-12-31')
end = pd.to_datetime('2023-01-10')
between = df.loc[start:end]

open_prices = between['Open']
close_prices = between['Close']

plt.figure(figsize=(16, 5)) 

plt.subplot(3,1,1)
plt.plot(close_prices, label='Close Price', color='red') 
plt.plot(open_prices, label='Open Price', color='green')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Google Stock Prices (Open & Close)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.subplot(3,1,2)
plt.plot(open_prices, label='Open Price', color='green')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Google Stock Prices (Open & Close)")
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.subplot(3,1,3)
plt.plot(close_prices, label='Close Price', color='red') 
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Google Stock Prices (Open & Close)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
