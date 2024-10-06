class Student:
	def __init__(self):
		self.name='mohan'
		self.age=12

x=Student()

print(x.name)
print(x.age)

print(x.__dict__)