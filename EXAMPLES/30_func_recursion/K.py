def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

'''
def fact(n):
	res=1	

	for i in range(1,n+1):
		res=res*i
	
	return res
'''

print(fact(5))
print(fact(6))
print(fact(7))
