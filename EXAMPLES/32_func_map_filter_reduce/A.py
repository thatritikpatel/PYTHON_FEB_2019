def even(n):
	return n%2==0

#print(even(12))
#print(even(21))
#print(even(73))

x=[34,67,89,23,44,12,90]

y=filter(even,x)

print(y)
print(type(y))
#print(len(y))
'''
for i in y:
	print(i)
'''