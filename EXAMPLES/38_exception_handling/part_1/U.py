#ten

import os

x=[12,13,14]

print('start')

try:
	print('----1')
	i=int(input('Enter Index: '))
	print('----2')
	os._exit(0)
except ValueError:
	print('Invalid Input Value','----5')
finally:
	print('essential code')

print('OK','----8')