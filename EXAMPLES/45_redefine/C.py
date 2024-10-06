class A:
	def aaa(self):
		print('hello')

class B(A):
	def aaa(self):
		print('hi')

x=B()
x.aaa()