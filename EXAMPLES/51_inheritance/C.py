#Multiple Inheritance

class A:
	def aaa(self):
		print('aaa method')

class B:
	def bbb(self):
		print('bbb method')

class C(A,B):
	def ccc(self):
		print('ccc method')


x=C()
x.aaa()
x.bbb()
x.ccc()