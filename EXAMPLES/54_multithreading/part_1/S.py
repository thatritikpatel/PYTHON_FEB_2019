from threading import *
import time

def aaa():
	for i in range(3):
		print(i,current_thread().getName(),'a')
		time.sleep(1)

def bbb():
	for i in range(3):
		print(i,current_thread().getName(),'b')
		time.sleep(1)



print(time.time())

'''
t1=Thread(target=aaa,name='mohan')
t2=Thread(target=bbb,name='sohan')

x=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
y=time.time()

print(y-x)
'''