#Single Inheritance

class A:
	def aaa(self):
		print('aaa method')

class B(A):
	def bbb(self):
		print('bbb method')

x=B()
x.aaa()
x.bbb()