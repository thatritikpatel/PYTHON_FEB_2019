class A:
	def __init__(self):
		self.a=345
		print(self)

class B(A):
	def aaa(self):
		print(self.a)
		print(self)

x=B()
x.aaa()
print(x)