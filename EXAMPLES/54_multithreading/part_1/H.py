from threading import *

def aaa():
	for i in range(20):
		print(i,current_thread().getName())

def bbb():
	for i in range(20):
		print(i,current_thread().getName(),' #######')


t1=Thread(target=aaa,name='mohan')
t2=Thread(target=bbb,name='man')

t1.start()
t2.start()

#bbb()
#aaa()