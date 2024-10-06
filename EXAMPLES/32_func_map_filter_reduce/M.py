from functools import reduce

x=[10,20,30,40]

'''
def add(a,b):
	return a+b
'''

y=reduce(lambda a,b:a+b,x)

print(y)
