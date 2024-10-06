def outer():
	print('------ outer func -----start')
	def inner():
		print('----- inner func -----')
	print('------ ######### -------')
	inner()
	print('------ outer func -----end')


outer()