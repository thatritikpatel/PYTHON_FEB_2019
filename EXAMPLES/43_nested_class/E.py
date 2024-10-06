class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.address=student.address('54','lemon street','shivnagar','482002')

	class address:
		def __init__(self,house,street,locality,pin):
			self.house=house
			self.street=street
			self.locality=locality
			self.pin=pin
		
s1=student('mohan',34)
s2=student('ganesh',23)
#print('name:',s1.name,'age:',s1.age,'address:',s1.address)
print('name:',s1.name,'age:',s1.age,'address:','houseno:',s1.address.house,'street:',s1.address.street)
print('name:',s2.name,'age:',s2.age,'address:','houseno:',s2.address.house,'street:',s2.address.street)