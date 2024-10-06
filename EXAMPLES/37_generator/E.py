def aaa():
	for i in range(100000000):
		yield i

x=aaa()

print(type(x))


print(next(x))
print(next(x))
print(next(x))
print(next(x))
