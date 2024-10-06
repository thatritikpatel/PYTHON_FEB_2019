import os,sys

fnm=input('Enter file name: ')
if os.path.isfile(fnm):
	print('file exists:',fnm)
	f=open(fnm,'r')
else:
	print('file does not exists')
	sys.exit(0)

lc=wc=cc=0
for line in f:
	lc=lc+1
	arr=line.split()
	wc=wc+len(arr)
	cc=cc+len(line)

print('lines count:',lc)
print('words count:',wc)
print('characters count:',cc)