#default except must be last
#3

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
except:
	print('Some Problem Sorry!','----6')
except ZeroDivisionError:
	print('Can\'t devide by zero','----6')


print('OK','----8')