'''
def odd(n):
	return n%2!=0

def even(n):
	return n%2==0
'''

x=[34,67,89,23,44,12,90]

y=list(filter(lambda n:n%2!=0,x))
z=list(filter(lambda n:n%2==0,x))

print(x)
print('odd records:',y)
print('even records:',z)
