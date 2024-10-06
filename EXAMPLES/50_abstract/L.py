from abc import abstractmethod,ABC

class A(ABC):
	@abstractmethod
	def aaa(self):
		pass

	def ccc(self):
		print('ccc method')

class B(ABC):
	@abstractmethod
	def bbb(self):
		pass


class C(A,B):
	def aaa(self):
		print('aaa method')

	def bbb(self):
		print('bbb method')
	
x=C()
x.aaa()
x.bbb()
x.ccc()
