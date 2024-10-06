from threading import *

a=Lock()

def aaa():
	#a.acquire()
	x=current_thread()
	print(x.name)
	a.release()

t1=Thread(target=aaa,name='ganesh')
t2=Thread(target=aaa,name='suresh')

t1.start()
t2.start()

