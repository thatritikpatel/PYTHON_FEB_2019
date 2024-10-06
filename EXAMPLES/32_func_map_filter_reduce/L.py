from functools import reduce

x=[1,2,3,4]

def add(a,b):
	return a+b

y=reduce(add,x)

print(y)
