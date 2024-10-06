class A:
	def aaa(self):
		print('hello')

class B(A):
	
	def bbb(self):
		print('hi')
		super().aaa()
	
B().bbb()