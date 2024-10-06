print('----1')

try:
	print('----2a')
	z=12/0
	print('----2b')
except ZeroDivisionError:
	print('----3')
else:
	print('----4')
finally:
	print('----5')

print('----6')