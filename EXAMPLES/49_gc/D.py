import time

class Student:
	def __init__(self):
		print('instance created')

	def __del__(self):
		print('going to delete the instance')

Student()



time.sleep(5)

print('the end')