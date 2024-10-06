from threading import *
import time

def aaa():
	x=current_thread()
	for i in range(7):
		print(i,'aaa() ',x.name,' ~~~~~~~~~~~~~~~~')
		time.sleep(1)

t=Thread(target=aaa,name='ganesh')
t.start()

t.join(3)

for i in range(10):
	print(i,'aaa() ',current_thread().getName(),' ~~~~~~~~~~~~~~~~')