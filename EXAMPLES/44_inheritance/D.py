class A:
	def __init__(self):
		self.a=345

class B(A):
	def aaa(self):
		print(self.a)

x=B()
x.aaa()