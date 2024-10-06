from threading import *

def aaa():
	for i in range(20):
		print(i,current_thread().getName())

def bbb():
	for i in range(20):
		print(i,current_thread().getName(),' #######')


bbb()
aaa()