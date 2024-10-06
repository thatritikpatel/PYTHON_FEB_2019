import time

class Student:
	def __init__(self):
		print('instance created')

	def __del__(self):
		print('going to delete the instance')

x=Student()

time.sleep(5)

#x=None