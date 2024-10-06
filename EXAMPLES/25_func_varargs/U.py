def info(**a):
	#print(a)
	for k,v in a.items():
		print(k,'---->',v)

info(name='ganesh',degree='BE',branch='CS',sem='1st')
info(empno=2345,salary=34000,designation='manager')