class A:
	def __init__(self):
		print('in A init function')

	def aaa(self):
		print('in A inst method')
	
	@classmethod
	def bbb(cls):
		print('in A class method')

	@staticmethod
	def ccc():
		print('In A static method')

class B(A):
	def ddd(self):
		print('in B')
		super().__init__()
		super().aaa()
		super().bbb()
		super().ccc()

x=B()
x.ddd()
