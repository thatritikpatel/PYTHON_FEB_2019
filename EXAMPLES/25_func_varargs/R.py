def process(*a,name):
	print("Name:",name)
	for i in a:
		print(i,'-')
	
#process(34,56,12,78,90,23,'mohan')
#process(name='mohan',34,56,12,78,90,23)
process(34,56,12,78,90,23,name='mohan')