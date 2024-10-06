#2 0 3 two

x=[12,13,14]

print('start')


try:
	print('----1')
	i=int(input('Enter Index: '))
except ValueError:
	print('Invalid Input Value','----5')

print('------xyz')
print('------xyz')
print('------xyz')
print('------xyz')

try:
	print('----2')
	y=12/i
except ZeroDivisionError:
	print('Can\'t devide by zero','----6')

print('------mno')
print('------mno')
print('------mno')
print('------mno')

try:
	print('----3')
	print(x[i])
	print('----4')
except IndexError:
	print('Invalid Index','----7')

print('OK','----8')



	
	