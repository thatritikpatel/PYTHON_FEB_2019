from threading import *
import time

l=Lock()

def aaa(a):	
	for i in range(5):
		l.acquire()
		print(current_thread().getName(),end=' ')
		time.sleep(1)
		print(a)
		l.release()
	

t1=Thread(target=aaa,name='ganesh',args=('hi',))
t2=Thread(target=aaa,name='ravan',args=('bye',))

t1.start()
t2.start()