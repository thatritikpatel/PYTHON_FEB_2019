class A:
	@classmethod
	def aaa(cls):
		print('hello')

class B(A):
	@classmethod
	def aaa(cls):
		print('hi')
		super().aaa()

	def bbb(self):
		print('GM')
		super().aaa()

B().bbb()