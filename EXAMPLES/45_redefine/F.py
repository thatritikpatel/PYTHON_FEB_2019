class A:
	@classmethod
	def aaa(cls):
		print('hello')

class B(A):
	@classmethod
	def aaa(cls):
		print('hi')
		super().aaa()

	@classmethod
	def bbb(cls):
		print('GM')
		#cls.aaa()
		super().aaa()

#B.aaa()
#super().aaa()

B.bbb()