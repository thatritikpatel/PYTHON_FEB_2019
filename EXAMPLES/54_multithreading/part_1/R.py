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

t1=time.time()
aaa()
bbb()
t2=time.time()

print(t2-t1)