class A:
	def __init__(self):
		print('in A init function')
		self.a=12

	def aaa(self):
		print('in A inst method')
	
	@classmethod
	def bbb(cls):
		print('in A class method')

	@staticmethod
	def ccc():
		print('In A static method')

class B(A):
	@classmethod
	def ddd(cls):
		print('in B')
		super(B,cls).__init__(cls)
		super(B,cls).aaa(cls)
		super().bbb()
		super().ccc()


B.ddd()
#print(B.__dict__)
#print(dir(B))