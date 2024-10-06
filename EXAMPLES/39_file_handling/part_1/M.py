f=open('abc.txt','r')

l=f.readlines()

print(type(l))

print(l)


for line in l:
	print(line,end='')
