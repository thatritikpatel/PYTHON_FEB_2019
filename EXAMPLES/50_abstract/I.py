from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def mno(self):pass

class B(A):
	def mno(self):
		print('inside MNO')

x=B()
x.mno()
