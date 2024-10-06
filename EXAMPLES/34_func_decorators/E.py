def greet(name):
	print('Hello',name)

def dfunc(a):
	def xgreet(name):
		if name=='ganesh':
			print('Hello',name)
			print('How are you',name)
		else:
			print('Hi',name)
	return xgreet	

y=dfunc(greet)

greet('mohan')
y('ganesh')