def info(*b,**a):
	#print(a)
	for i in b:
		print(i)
	for k,v in a.items():
		print(k,'---->',v)

info(12,34,67,name='ganesh',degree='BE',branch='CS',sem='1st')
