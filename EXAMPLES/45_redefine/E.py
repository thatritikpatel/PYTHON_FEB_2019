class A:
	@classmethod
	def aaa(cls):
		print('hello')

class B(A):
	@classmethod
	def aaa(cls):
		print('hi')
		super().aaa()

B.aaa()
super().aaa()