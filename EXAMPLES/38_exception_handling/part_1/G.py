print('---1')

x=[12,13,14]
i=int(input('Enter index : '))

try:
	print('----2')
	print(x[i])
	print('-----3')
except IndexError:
	print('index out of range','----4')

print('----5')