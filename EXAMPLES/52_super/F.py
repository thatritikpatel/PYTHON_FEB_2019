class A:
	def aaa(self):
		print('aaa() in A')

class B(A):
	def aaa(self):
		print('aaa() in B')

class C(B):
	def aaa(self):
		print('aaa() in C')

class D(C):
	def aaa(self):
		print('aaa() in D')
	
	def yyy(self):
		self.aaa()

x=D()
x.yyy()





