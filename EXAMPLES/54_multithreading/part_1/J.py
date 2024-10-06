from threading import *

class MyThread(Thread):
	def run(self):
		for i in range(10):
			print(i,current_thread().getName())

t=MyThread()
t.setName('mohan')
t.start()

print('######################################')
for i in range(10):
	print(i,current_thread().getName())





