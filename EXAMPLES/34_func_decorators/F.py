def dfunc(func):
	def xgreet(name):
		if name=='ganesh':
			func(name)
			print('How are you',name)
		else:
			func(name)
	return xgreet	

@dfunc
def greet(name):
	print('Hello',name)

greet('mohan')
greet('sohan')
greet('ganesh')
greet('ratnesh')