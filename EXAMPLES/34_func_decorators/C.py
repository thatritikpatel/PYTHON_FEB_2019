def dfunc(func):
	def xgreet(name):
		if name=='ganesh':
			print('Hello',name)
			print('How are you',name)
		else:
			print('Hello',name)
	return xgreet	

@dfunc
def greet(name):
	print('Hello',name)

greet('mohan')
greet('sohan')
greet('ganesh')
greet('ratnesh')