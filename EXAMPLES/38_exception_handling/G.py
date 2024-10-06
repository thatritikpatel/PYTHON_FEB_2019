print('---1')

try:
	print('---2')	
	try:
		print('---3')	
		x=12/0
	except ValueError:
		print('---4')
	finally:
		print('---5')
	print('---6')
except ZeroDivisionError:
	print('---7')
finally:
	print('---8')

print('---9')