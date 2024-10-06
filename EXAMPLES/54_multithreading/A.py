from threading import *
import time

def aaa(a):
	for i in range(5):
		print(current_thread().getName(),end=' ')
		time.sleep(1)
		print(a)

t1=Thread(target=aaa,name='ganesh',args=('hi',))
t2=Thread(target=aaa,name='ravan',args=('bye',))

t1.start()
t2.start()