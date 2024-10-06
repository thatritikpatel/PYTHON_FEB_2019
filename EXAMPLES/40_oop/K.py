class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def setsem(self,sem):
		self.sem=sem


x=student('vikram',23)
y=student('betal',89)

x.setsem('1st')
y.degree='BE'

print(x.__dict__)
print(y.__dict__)