def aaa():
	print('-----E')
	bbb()
	print('-----X')

def bbb():
	print('-----R')

def ccc():
	print('-----S')
	aaa()
	print('-----J')

ccc()