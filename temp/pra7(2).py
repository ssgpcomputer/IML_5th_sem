import pandas as pd
d={'Name':['DEEP','JAY','RONAK','JD']}
df=pd.DataFrame(d)
print("before sorting ",df)
print("after sorting ",df.sort_values(by='Name',ascending=True))