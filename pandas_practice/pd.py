import pandas as pd
import numpy as np
import time, math
from datetime import datetime

import matplotlib.pyplot as plt


d = [
        {'a':1, 'b':2, 'c':3},
        {'a':1, 'b':2, 'c':3},
        {'a':1, 'b':2, 'c':3},
        {'a':1, 'b':3, 'c':2}
    ]

df = pd.DataFrame(d)

print(df)

df2 = df[['a', 'b']]

print(df2)

df[['d', 'e']] = df[['b', 'c']] + [1, 2]

df[ 'f' ] = [1,2,3,4]
print(df)


a = [[1,2,3], [4,5,6], [6,7,8]]
a = np.vstack(a)

print(a[1, :])
print(a[:, 1])

df2 = df.loc[df['b'] == 2]
print(df2)



ld = [{'time':None, 'value':None, 'channel':None}]*10
ld[4] = {'time':datetime.now(), 'value':12.3113, 'channel':'201', 'extra':0}
df = pd.DataFrame(ld)
print(df)

dfs = []
for d in ld:
    df = pd.DataFrame([d])
    print(df.columns)
    dfs.append(df)

dfs = pd.concat(dfs)
print("#"*80)
print(dfs)
print("#"*80)
