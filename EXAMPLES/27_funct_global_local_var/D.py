a=12

def aaa():
	global a
	a=56
	print(a)

def bbb():
	print(a)


bbb()
aaa()


'''
aaa()
bbb()
'''
