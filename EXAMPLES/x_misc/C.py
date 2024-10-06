class Cat:
	def makeSound(self):
		print('Cat Sound')

class Dog:
	def makeSound(self):
		print('Dog Sound')

class Cow:
	def makeSound(self):
		print('Cow Sound')

def playSound(x):
	x.makeSound()

a=Cat()
b=Cow()
c=Dog()

playSound(a)
playSound(b)
playSound(c)