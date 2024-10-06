f=open('abc.txt','r')

c=f.tell()

print(c)

s=f.read(2)

print(s)

print('#####')

c=f.tell()
print(c)
