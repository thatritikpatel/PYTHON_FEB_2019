from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def aaa(self):
		pass

	def mno(self):
		print('hello')


x=A()