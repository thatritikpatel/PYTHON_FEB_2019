print('---1')

try:
	print('---2')	
	try:
		print('---3')
	except IndexError:
		print('---4')
	finally:
		print('---5')
		x=12/0
	print('---6')
except ValueError:
	print('---7')
finally:
	print('---8')

print('---9')