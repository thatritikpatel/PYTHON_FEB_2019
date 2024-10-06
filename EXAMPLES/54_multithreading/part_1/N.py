from threading import *
import time

def aaa():
	x=current_thread()
	print('aaa() ',x.name,x.ident,' ~~~~~~~~~~~~~~~~start')
	time.sleep(3)
	print('aaa() ',x.name,x.ident,' ~~~~~~~~~~~~~~~~end')

t1=Thread(target=aaa,name='a1')
t2=Thread(target=aaa,name='a2')
t3=Thread(target=aaa,name='a3')

t1.start()
t2.start()
t3.start()

print(active_count())

time.sleep(10)

print(active_count())