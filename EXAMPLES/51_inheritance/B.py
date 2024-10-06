#Multi-Level Inheritance

class A:
	def aaa(self):
		print('aaa method')

class B(A):
	def bbb(self):
		print('bbb method')

class C(B):
	def ccc(self):
		print('ccc method')


x=C()
x.aaa()
x.bbb()
x.ccc()