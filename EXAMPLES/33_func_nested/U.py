def outer():
	print('------ outer func -----start')
	def inner():
		print('----- inner func -----')
		return 123
	print('------ ######### -------')
	print('------ outer func -----end')
	return inner()

x=outer()
print(x)
