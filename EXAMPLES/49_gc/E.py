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
x=None
time.sleep(3)

print('second reference deleted')
y=None
time.sleep(3)

print('third reference deleted')
z=None
time.sleep(5)

print('the end')