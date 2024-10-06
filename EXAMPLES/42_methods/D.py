class circle:
	pi=3.14

	def __init__(self,r):
		self.r=r
	
	def calcA(self):
		#print(pi*r*r)
		print(circle.pi * self.r * self.r)

	def calcP(self):
		print(2 * circle.pi * self.r)
	
	@classmethod
	def showPI(cls):
		print(circle.pi)
		print(cls)

	@staticmethod
	def defineCircle():
		print('Circle is a..........,.,....')
 

c1=circle(20)
c2=circle(30)


#Case 5:
print(c1.__dict__)
print(c2.__dict__)
print(circle.__dict__)

#Case 4:
'''
#defineCircle()
c1.defineCircle()
c2.defineCircle()
circle.defineCircle()
'''

#Case 3:
#showPI()
'''
c1.showPI()
c2.showPI()
circle.showPI()
'''

#Case 1:
'''
c1.calcA()
c2.calcA()

c1.calcP()
c2.calcP()
'''

#Case 2:
'''
#calcA()
#circle.calcA()
#circle.calcA(1)
'''








