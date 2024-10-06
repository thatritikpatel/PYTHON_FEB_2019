#0

print('start')

i=int(input('Enter a number: '))

try:
	print('----1')	
	y=12/i
	print('----3')
except IndexError:
	print('Invalid Input Value','----5')
except ZeroDivisionError:
	print('Can\'t devide by zero','----6')	
except ValueError:
	print('Invalid Input###@@!!!','----6')	



print('OK','----8')