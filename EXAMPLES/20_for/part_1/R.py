x=int(input('Enter a number: '))

#Case 1:
#print('*'*x)

#Case 2:
'''
for i in range(x):
	print('*'*x)
'''

#Case 3:
'''
for i in range(x):
	for j in range(x):
		print('*',end='')
	print()
'''

#Case 4:
'''
for i in range(x):
	for j in range(x):
		print('{}-{}'.format(i,j),end='\t')
	print()
'''