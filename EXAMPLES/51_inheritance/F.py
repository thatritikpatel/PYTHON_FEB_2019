#Hybrid Inheritance

class E:
	def eee(self):
		print('eee method')

class F:
	def fff(self):
		print('fff method')


class A(E,F):
	def aaa(self):
		print('aaa method')

class B(A):
	def bbb(self):
		print('bbb method')

class C(B):
	def ccc(self):
		print('ccc method')

class D(B):
	def ddd(self):
		print('ddd method')