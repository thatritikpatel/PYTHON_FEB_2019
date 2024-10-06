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
except ValueError:
	print('Invalid Input Value','----5')
except ZeroDivisionError:
	print('Can\'t divide by zero','----6')
except IndexError:
	print('Invalid Index','----7')

print('OK','----8')