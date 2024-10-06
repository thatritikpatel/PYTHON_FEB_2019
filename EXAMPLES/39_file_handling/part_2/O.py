import os
import datetime

x=os.stat('A.py')
print(datetime.datetime.fromtimestamp(x.st_ctime))