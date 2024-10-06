class A:
	a=34
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
	@staticmethod
	def ddd():
		print('in B')
		#super().__init__()
		#super().aaa()
		#super().bbb()
		super(B,B).ccc()
		print(super(B,B).a)

B.ddd()
