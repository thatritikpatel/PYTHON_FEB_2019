from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def mno(self):pass

class B(A):
	pass

x=B()

