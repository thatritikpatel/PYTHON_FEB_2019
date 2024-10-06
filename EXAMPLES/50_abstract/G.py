from abc import abstractmethod,ABC

class A(ABC):
	def mno(self):
		print('hello')


x=A()

x.mno()