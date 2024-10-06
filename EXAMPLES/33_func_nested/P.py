def outer():
	x=12
	y=True
	
	print(locals())
	print('##############')

	def inner():
		print('-----')
	
	print(locals())


outer()