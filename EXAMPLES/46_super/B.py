class A:
	@classmethod
	def aaa(cls):
		print(id(cls))
		print('hello')

class B(A):
	@classmethod
	def aaa(cls):
		print(id(cls))
		print('hi')
		super().aaa()

#print(id(B))
#print(id(A))

B.aaa()
#super().aaa()