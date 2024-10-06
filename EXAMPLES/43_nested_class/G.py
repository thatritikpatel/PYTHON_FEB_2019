class student:
	def __init__(self,name,age,house,street,locality,pin):
		self.name=name
		self.age=age
		self.address=student.address(house,street,locality,pin)
	
	def showInfo(self):
		print('name:',self.name,'age:',self.age)

	class address:
		def __init__(self,house,street,locality,pin):
			self.house=house
			self.street=street
			self.locality=locality
			self.pin=pin
		
		def showInfo(self):
			print('house:',self.house,'street:',self.street,'locality:',self.locality,'pin:',self.pin)
		
s1=student('mohan',34,'112','orange street','shanti nagar','482001')
s2=student('vikram',28,'234','apple street','sanchar nagar','482003')
s1.showInfo()
s1.address.showInfo()
#print('name:',s1.name,'age:',s1.age,'address:','houseno:',s1.address.house,'street:',s1.address.street)
#print('name:',s2.name,'age:',s2.age,'address:','houseno:',s2.address.house,'street:',s2.address.street)