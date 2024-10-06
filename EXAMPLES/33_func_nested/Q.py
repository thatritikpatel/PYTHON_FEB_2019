def outer():
	print('------ outer func -----start')
	
	inner()
	
	def inner():
		print('----- inner func -----')
	print('------ ######### -------')
	
	print('------ outer func -----end')


