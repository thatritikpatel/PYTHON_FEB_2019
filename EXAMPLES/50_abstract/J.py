from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def aaa(self):
		pass

	@abstractmethod
	def bbb(self):
		pass

class B(A):
	def aaa(self):
		print('hello')

x=B()
x.aaa()