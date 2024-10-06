class A:
	def aaa(self):
		print('hello')

class B(A):	
	def bbb(self):
		print('hi')
		super().aaa()

#print(B.__dict__)
#print(A.__dict__)

#B().aaa()

B().bbb()