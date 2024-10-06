f=open('abc.txt','r')

#f.seek(<offset>,<start-point>)
#start-point->0,1,2

f.seek(2)

c=f.read(1)
print(c)
print(f.tell())
