class A:
	@classmethod
	def aaa(cls):
		print(id(cls),'#######')
		print('hello')

class B(A):
	@classmethod
	def aaa(cls):
		print(id(cls))
		print('hi')
		super().aaa()

	def bbb(self):
		print(id(self))
		print('GM')
		super().aaa()

print(id(B),'~~~~~~')
B().bbb()





