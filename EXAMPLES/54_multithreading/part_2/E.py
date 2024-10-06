from threading import *
import time

def bbb():
	x=current_thread()
	print('bbb() thread name:',x.name,'is daemon:',x.daemon)

def aaa():
	x=current_thread()
	print('aaa() thread name:',x.name,'is daemon:',x.daemon)
	t=Thread(target=bbb,name='suresh')
	t.start()
	

t=Thread(target=aaa,name='ganesh')
t.setDaemon(True)
t.start()

time.sleep(5)