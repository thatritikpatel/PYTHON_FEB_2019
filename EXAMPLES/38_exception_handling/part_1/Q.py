print('---1')

x=[12,13,14]
i=int(input('Enter index: '))

try:
	print(x[i])
except IndexError as info:
	print('some problem: ',info)

print('----2')