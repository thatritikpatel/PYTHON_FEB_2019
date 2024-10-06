class A:
	@classmethod
	def aaa(cls):
		print('good morning')

class B(A):
	pass

B.aaa()