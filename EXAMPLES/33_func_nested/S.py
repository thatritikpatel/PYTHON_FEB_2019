def outer():
	print('------ outer func -----start')
	def inner():
		print('----- inner func -----')
	print('------ ######### -------')
	print('------ outer func -----end')
	return inner

x=outer()
#print(x)
#print(type(x))

x()
