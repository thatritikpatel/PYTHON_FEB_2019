class A:
	a=12

class B(A):
	a=45

	def aaa(self):
		print(self.a)
		print(B.a)
		print(super().a)

B().aaa()