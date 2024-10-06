n=int(input('Enter a number: '))

a=65

for i in range(n):
	for j in range(i+1):
		print('{}-{}'.format(i,j),end='\t')
	print()
