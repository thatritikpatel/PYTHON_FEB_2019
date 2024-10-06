#ten

x=[12,13,14]

print('start')

print('----1')
i=int(input('Enter Index: '))

try:	
	print('----2')
	y=12/i
	print('----3')
	print(x[i])
	print('----4')
except ValueError:
	print('Invalid Input Value','----5')
except ZeroDivisionError:
	print('Can\'t devide by zero','----6')
finally:
	print('essential code')

print('OK','----8')