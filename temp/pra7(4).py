import pandas as pd
import numpy as np 
ipl={'team':['RCB','CSK','MI','LSG'],
     'Point':[18,16,14,12]}
df= pd.DataFrame(ipl,columns=['team','Point'])
print("orignal data frame ",df)
df.to_csv('ipl team.csv',sep=' \t')
new=pd.read_csv('ipl team.csv')
print("data from ipl team")
print(new) 