
#Case 2:
class A:	
	def aaa(self):
		print('aaa method in A')

class B(A):
	pass

x=B()
x.aaa()

#Case 1:
'''
class A:	
	def aaa(self):
		print('aaa method in A')

class B(A):
	def aaa(self):
		print('aaa method in B')

x=B()
x.aaa()
'''