class Account:
	def __init__(self,balance):
		self.balance=balance

	def __add__(self,other,someother):
		return self.balance+other.balance+someother.balance

a=Account(10000)
b=Account(30000)
c=Account(15000)

print(a+b+c)