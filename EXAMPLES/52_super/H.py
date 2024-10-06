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
		#super().aaa()
		#super().super().aaa()
		#super(C,self).aaa()
		super(B,self).aaa()

x=D()
x.yyy()





