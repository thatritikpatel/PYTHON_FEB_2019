def aaa():
	global a
	a=12
	print(a)

def bbb():
	global a
	a=34
	print(a)


bbb()
aaa()

'''
aaa()
bbb()
'''