class Cat:
	def makeSound(self):
		print('Cat Sound')

class Dog:
	def createSound(self):
		print('Dog Sound')

class Cow:
	def makeSound(self):
		print('Cow Sound')

def playSound(x):
	if hasattr(x,'makeSound'):
		x.makeSound()
	elif hasattr(x,'createSound'):
		x.createSound()


a=Cat()
b=Cow()
c=Dog()

playSound(a)
playSound(b)
playSound(c)