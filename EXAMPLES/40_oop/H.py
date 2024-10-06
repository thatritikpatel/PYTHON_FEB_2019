class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age

x=student('mohan',12)
y=student('ganesh',14)

print(x.name,x.age)
print(y.name,y.age)

print(x.__dict__)
print(y.__dict__)

print(student.__dict__)