#x=[i*i for i in range(7)]
x=(i*i for i in range(7))

print(x)
print(type(x))


print(next(x),end='-')
print(next(x),end='-')
print(next(x),end='-')
print(next(x),end='-')
print(next(x),end='-')
print(next(x),end='-')
print(next(x),end='-')


for i in x:
	print(i,end=' ')




