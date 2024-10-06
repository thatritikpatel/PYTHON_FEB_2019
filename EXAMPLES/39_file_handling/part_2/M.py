import os

for pdirpath,subdirnms,subflnms in os.walk('.'):
	print('Folder Path: ',pdirpath)
	print('\tSub Folder Names: ',subdirnms)
	print('\tSub File Names: ',subflnms)
	print()

