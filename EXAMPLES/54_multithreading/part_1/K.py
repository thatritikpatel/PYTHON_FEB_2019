from threading import *

def aaa():
	print('aaa()',current_thread().getName())

t=Thread(target=aaa,name='ganesh')
t.start()

print('$$$$$$$$$$$$$$$$$$$')
aaa()