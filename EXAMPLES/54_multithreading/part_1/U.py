from threading import *

def job(a):
	print(current_thread().getName())
	print(a)

t=Thread(target=job,name='vidyut',args=(12,13))
t.start()


'''
y=(12,)
print(type(y))
'''