class C:
	def aaa(self,a=None,b=None,c=None):
		if a != None and b != None and c != None:
			print(a+b+c)
		elif a != None and b != None:
			print(a+b)
		else:
			print('at least 2 and at max 3 arguments required...')

x=C()

#x.aaa(10,20,30)
#x.aaa(10,20)
#x.aaa(10)
#x.aaa()

x.aaa(10,20,30,40)
		