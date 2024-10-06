def info(value,*b,**a):
	print(value,'~~~')
	for i in b:
		print(i)
	for k,v in a.items():
		print(k,'---->',v)

#info(12,34,67,name='ganesh',degree='BE',branch='CS',sem='1st',value=23)
#info(12,34,67,name='ganesh',degree='BE',branch='CS',sem='1st')
#info(name='ganesh',degree='BE',branch='CS',sem='1st')
#info(name='ganesh',degree='BE',branch='CS',sem='1st',value=14)
#info(name='ganesh',degree='BE',value=14,branch='CS',sem='1st')
info(123,45,78)

