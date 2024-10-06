def aaa():
	yield 'A'
	yield 'B'
	yield 'C'
	yield 'D'

x=aaa()

print(type(x))

print(next(x))
print(next(x))
print(next(x))
print(next(x))