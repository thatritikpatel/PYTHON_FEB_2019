x=int(input('Enter a number: '))

if x<100:
	print('hello')
elif x<200:
	if x<150:
		print('hi1')
	elif x<175:
		print('hi2')
	else:
		print('hi5')
else:
	print('bye')