import time

class Student:
	def __init__(self):
		print('instance created')

	def __del__(self):
		print('going to delete the instance')

x=Student()
y=x
z=y

print('first reference deleted')
del x
time.sleep(3)

print('second reference deleted')
del y
time.sleep(3)

print('third reference deleted')
del z
time.sleep(5)

print('the end')