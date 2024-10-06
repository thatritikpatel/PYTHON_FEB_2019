from threading import *

def aaa():
	x=current_thread()
	for i in range(10):
		print(i,'aaa() ',x.name,' ~~~~~~~~~~~~~~~~')

t=Thread(target=aaa,name='ganesh')
t.start()

t.join()

for i in range(10):
	print(i,'aaa() ',current_thread().getName(),' ~~~~~~~~~~~~~~~~')