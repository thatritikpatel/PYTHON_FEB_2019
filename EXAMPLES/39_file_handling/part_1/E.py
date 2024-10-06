f=open('abc.txt','w')

print(f.name)
print(f.mode)


print(f.closed)

f.close()

print(f.closed)