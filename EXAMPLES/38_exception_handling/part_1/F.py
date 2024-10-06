print('---1')

x=[12,13,14]
i=int(input('Enter index'))

try:
	print(x[i])
except IndexError:
	print('index out of range')

print('----2')