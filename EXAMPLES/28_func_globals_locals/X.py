a=23
def outer():
	x=12
	print('------ outer func -----start')
	def inner():
		print('----- inner func -----')
	print('------ ######### -------')
	inner()
	print('------ outer func -----end')
	print(locals())

#x=outer

outer()
print('$$$$$$$$$$$$$$$$$$$$$$')
#x()
print(globals())