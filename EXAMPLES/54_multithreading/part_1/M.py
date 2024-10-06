from threading import *
import time

def aaa():
	x=current_thread()
	print('aaa() ',x.name,x.ident,' ~~~~~~~~~~~~~~~~start')
	time.sleep(3)
	print('aaa() ',x.name,x.ident,' ~~~~~~~~~~~~~~~~end')

t=Thread(target=aaa,name='mohan')
print(t.isAlive())

t.start()

print(t.isAlive())

time.sleep(5)

print(t.isAlive())
