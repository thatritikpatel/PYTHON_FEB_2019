from threading import *

class A:
	def job(self):
		for i in range(10):
			print(i,current_thread().getName())

a=A()

t=Thread(target=a.job)
t.name='vikram'

t.start()

for i in range(10):
	print(i,current_thread().getName())
