class A:
	def __init__(self):
		print(id(self))
		print('hi')
		print(self.a)
		#self.a=34

class B(A):
	def __init__(self):
		self.a=55
	
	def aaa(self):
		print(id(self))
		print(self.a)
		super().__init__()
		print(self.a)

x=B()
print(id(x))
x.aaa()
