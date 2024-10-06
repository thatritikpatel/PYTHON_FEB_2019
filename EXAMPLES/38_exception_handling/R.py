class LowExperienceError(Exception):
	def __init__(self,arg):
		self.msg=arg

ex=int(input('Enter experience:'))

if ex<3:
	raise LowExperienceError('Your experience is below 3 years ... you are rejected')
else:
	print('you can visit us')
