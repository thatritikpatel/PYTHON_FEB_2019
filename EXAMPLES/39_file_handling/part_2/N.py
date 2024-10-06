import os
from datetime import *

x=os.stat('A.py')
#print(x)


print(x.st_size)
print(datetime.fromtimestamp(x.st_ctime))
print(datetime.fromtimestamp(x.st_mtime))
print(datetime.fromtimestamp(x.st_atime))


##############################################
