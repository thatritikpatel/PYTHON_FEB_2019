from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def aaa(self):
		pass

class B(ABC):
	@abstractmethod
	def bbb(self):
		pass

#Case 3:
'''
class C(A,B):
	def aaa(self):
		print('aaa method')

	def bbb(self):
		print('bbb method')
	
x=C()
'''

#Case 2:
'''
class C(A,B):
	def aaa(self):
		print('aaa method')
	
x=C()
'''

#Case 1:
'''
class C(A,B):
	pass
'''

x=C()
