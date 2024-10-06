print('----1')

try:
	print('----2a')
except ValueError:
	print('----3')
	z=12/0
else:
	print('----4')
finally:
	print('----5')

print('----6')