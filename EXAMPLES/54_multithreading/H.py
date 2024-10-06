from threading import *
import time

a=Semaphore(2)

def aaa():	
	for i in range(3):
		a.acquire()
		print(current_thread().getName())
		time.sleep(1)
		a.release()

t1=Thread(target=aaa,name='a1')
t2=Thread(target=aaa,name='a2')
t3=Thread(target=aaa,name='a3')
t4=Thread(target=aaa,name='a4')
t5=Thread(target=aaa,name='a5')
t6=Thread(target=aaa,name='a6')

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()