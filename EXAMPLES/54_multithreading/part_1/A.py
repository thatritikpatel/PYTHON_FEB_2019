def a1():
	print('--------- a1()--------- start')
	a2()
	print('--------- a1()--------- end')

def a2():
	print('--------- a2()--------- start')
	a3()
	print('--------- a2()--------- end')

def a3():
	print('--------- a3()--------- start')
	print('hello')
	print('--------- a3()--------- end')

a1()
