import os

fnm=input('Enter file name: ')

if os.path.isfile(fnm):
	print('file exists')
else:
	print('file does not exists')