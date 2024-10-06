def odd(n):
	return n%2!=0

def even(n):
	return n%2==0

x=[34,67,89,23,44,12,90]

y=list(filter(odd,x))
z=list(filter(even,x))

print(x)
print('odd records:',y)
print('even records:',z)
