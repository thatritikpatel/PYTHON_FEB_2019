import os,sys

fnm=input('Enter file name: ')

if os.path.isfile(fnm):
	print('file exists')
	f=open(fnm,'r')
else:
	print('file does not exists')
	sys.exit(0)

for line in f:
	print(line,end='')

f.close()