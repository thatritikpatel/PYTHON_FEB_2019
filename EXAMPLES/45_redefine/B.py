class A:
	def __init__(self):
		self.a=45

class B(A):
	def setVal(self):
		self.a=34

x=B()
print(x.a)
x.setVal()
print(x.a)
