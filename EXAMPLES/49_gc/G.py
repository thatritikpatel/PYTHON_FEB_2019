import time

class T:
	def __init__(self):
		print('instance created')

	def __del__(self):
		print('going to delete the object')


x=[T(),T(),T()]

time.sleep(5)

x=None

time.sleep(5)

print('the end')
