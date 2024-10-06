print('---1')

try:
	print('---2')	
	try:
		print('---3')	
		x=[1,2]
		print(x[2])
	except ValueError:
		print('---4')
		x=12/0
	finally:
		print('---5')
	print('---6')
except IndexError:
	print('---7')
finally:
	print('---8')

print('---9')