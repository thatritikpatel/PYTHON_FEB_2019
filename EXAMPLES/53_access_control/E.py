class E:
	a=67

	def __init__(self):
		self.a=89

class W(E):
	def aaa():
		print(W.a)
		x=W()
		print(x.a)
		print(W.a)

W.aaa()