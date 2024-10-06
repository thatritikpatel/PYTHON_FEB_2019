def process(*a,name):
	print("Name:",name)
	for i in a:
		print(i,'-')
	
#process('mohan',34,56,12,78,90,23)
#process('mohan','sohan',34,56,12,78,90,23)
#process(34,56,12,78,90,23,'mohan','sohan')
process(34,56,12,78,90,23,name='sohan')