#Cyclic Inheritance


#Case 1:
'''
class A(B):
	def aaa(self):
		print('aaa method $$$$')

class B(A):
	def bbb(self):
		print('bbb method')
'''

#Case 2:
class E(E):
	pass