import pandas as pd
import numpy as np 
ipl={'team':['RCB','CSK','MI','LSG'],
     'Point':[18,16,14,12]}
df=pd.DataFrame(ipl)
print(df.drop(['Point'],axis=1))