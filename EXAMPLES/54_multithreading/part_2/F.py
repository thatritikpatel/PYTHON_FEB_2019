from threading import *
import time

def aaa():
	x=current_thread()
	for i in range(5):
		print(i,'thread name:',x.name,'is daemon:',x.daemon)
		time.sleep(1)

t=Thread(target=aaa,name='ganehs')
t.setDaemon(True)
t.start()

time.sleep(3)

x=current_thread()
print('thread name:',x.name,'is daemon:',x.daemon)

