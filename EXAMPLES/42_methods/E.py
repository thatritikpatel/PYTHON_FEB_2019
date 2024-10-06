class abcd:
	a=900
	
	def __init__(self):
		self.a=122
	
	def aaa(self):
		a=34
		print(a)
		print(self.a)
		print(abcd.a)
	
	@classmethod
	def bbb(cls):
		a=89
		print(a)
		#print(self.a)
		print(abcd.a)
		print(cls.a)
		print(id(abcd))
		print(id(cls))
		print(abcd.__dict__)
		print("################################################")
		print(cls.__dict__)

	@staticmethod
	def ccc():
		a=78
		print(a)
		#print(self.a)
		#print(cls.a)
		print(abcd.a)

a=abcd()
#a.aaa()
#abcd.bbb()
#a.bbb()
abcd.ccc()

