class A:
	def aaa(self):
		print('hello')

class B(A):
	@classmethod
	def bbb(cls):
		print('hi')
		#super().aaa()   #NOT OK
		super().aaa(12)

B.bbb()