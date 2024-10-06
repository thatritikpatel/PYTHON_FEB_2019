from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def aaa(self):
		pass

class B:
	def aaa(self):
		print('aaa method from B')

class C(A,B):
	pass

x=C()
