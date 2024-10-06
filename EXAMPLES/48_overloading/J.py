class Account:
	def __init__(self,balance):
		self.balance=balance

	def __add__(self,other):
		return Account(self.balance+other.balance)
	
	def __str__(self):
		return self.balance

a=Account(10000)
b=Account(30000)
c=Account(15000)

print(a+b+c)
