#Python is a class based object oriented language

class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age


x=Student('mohan',12)
print(x.name)
print(x.age)