class A:
	def aaa(self,a):
		print('hello########')

class B(A):
	def aaa(self):
		print('hi')
		super().aaa(12)

x=B()
#x.aaa(12)
x.aaa()

print(B.__dict__)
print(A.__dict__)

y=A()
y.aaa(12)