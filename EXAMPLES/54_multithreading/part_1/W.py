from threading import *

def job(*a):
	print(current_thread().getName())
	for i in a:
		print(i,'~~~~')

t=Thread(target=job,name='vidyut',args=(12,13,14,15))
t.start()


'''
y=(12,)
print(type(y))
'''