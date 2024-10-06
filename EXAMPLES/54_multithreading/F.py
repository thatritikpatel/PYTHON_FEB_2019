from threading import *

a=Lock()

def fact(n):
	a.acquire()
	if n==1:
		val=1
	else:
		val=n*fact(n-1)
	a.release()

	return val

def callFact(n):
	print(current_thread().getName(),"factorial of {} is {}".format(n,fact(n)))

t1=Thread(target=callFact,name='abc',args=(5,))
t2=Thread(target=callFact,name='mno',args=(6,))

t1.start()
t2.start()

