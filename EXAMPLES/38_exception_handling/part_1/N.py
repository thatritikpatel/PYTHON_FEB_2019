#2 0 3 two

x=[12,13,14]

print('start')

try:
	print('----1')
	i=int(input('Enter Index: '))
	print('----2')
	y=12/i
	print('----3')
	print(x[i])
	print('----4')
except BaseException:
	print('Invalid Input Value','----5')

print('OK','----8')