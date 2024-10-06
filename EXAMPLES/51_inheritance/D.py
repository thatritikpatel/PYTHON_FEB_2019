#Hierarchical Inheritance

class A:
	def aaa(self):
		print('aaa method $$$$')

class B(A):
	def bbb(self):
		print('bbb method')

class C(A):
	def ccc(self):
		print('ccc method')


x=C()
y=B()
x.aaa()
y.aaa()