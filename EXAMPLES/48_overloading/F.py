class Account:
	def __init__(self,balance):
		self.balance=balance

	def __add__(self,other):
		return self.balance+other.balance

a=Account(10000)
b=Account(50000)

print(a+b)
