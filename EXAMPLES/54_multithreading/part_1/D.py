from threading import current_thread

def a1():
	print('--------- a1()--------- start',current_thread().getName())
	a2()
	print('--------- a1()--------- end',current_thread().getName())

def a2():
	print('--------- a2()--------- start',current_thread().getName())
	a3()
	print('--------- a2()--------- end',current_thread().getName())

def a3():
	print('--------- a3()--------- start',current_thread().getName())
	print('hello')
	print('--------- a3()--------- end',current_thread().getName())

a1()
