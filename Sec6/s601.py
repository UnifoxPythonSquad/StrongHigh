#glob & os
import os.path
import glob

path = 'C:\*'
files = glob.glob(path) 

for x in files:
    if os.path.isdir(x):
        print('%s <DIR>' % x)
    else:
        print(x)
