n=int(input('Enter a number: '))

for i in range(n):
	print(' '*(n-i-1)+str(i+1)*(i+1))
	#print(' '*(n-i-1)+('%d' %(i+1))*(i+1))
	#print(' '*(n-i-1)+('{}'.format(i+1))*(i+1))


