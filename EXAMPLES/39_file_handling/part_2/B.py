from zipfile import ZipFile,ZIP_STORED

x=ZipFile('abc.zip','r',ZIP_STORED)
l=x.namelist()
x.extractall()
#print(l)


for a in l:
	print('File: ',a)
	print('All Records:')
	f=open(a,'r')
	print(f.read())
	print()
