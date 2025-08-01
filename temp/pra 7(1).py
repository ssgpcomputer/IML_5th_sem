import pandas as pd 
d={
    'Name ':['DEEP','JAY','RONAK','JD'],
    ' t ':[18,19,35,25],
    'Team':['RCB','RCB','CSK','RCB'], # type: ignore
}
df=pd.DataFrame(d)
print(df)