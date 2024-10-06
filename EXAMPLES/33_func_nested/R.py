def outer():
	x=12
	print('------ outer func -----start')
	def inner():
		print('----- inner func -----')
	print('------ ######### -------')
	print('------ outer func -----end')


outer()


#print(x)
#inner()