class student:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	class address:
		def __init__(self,house,street,locality,pin):
			self.house=house
			self.street=street
			self.locality=locality
			self.pin=pin
		
s=student('mohan',34)
print('name:',s.name,'age:',s.age)
#print('address:',s.address)
a=s.address('54','mahanlal','nehru','482002')
print('address:',a.house,a.street,a.locality,a.pin)

print(student.__dict__)

print(s.__dict__)