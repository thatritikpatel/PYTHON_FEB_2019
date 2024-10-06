f=open('abc.txt','r')

#f.seek(<offset>,<start-point>)
#start-point->0,1,2

s=f.read(2)
print(s)

f.seek(4,1)

c=f.read(1)
print(c)

print(f.tell())
