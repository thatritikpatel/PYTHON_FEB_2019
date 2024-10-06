score=int(input('Enter your score(%): '))

if score>=75:
	print('D')
elif score>=60:
	print('F')
elif score>=45:
	print('S')
elif score>=33:
	print('T')
else:
	print('Fail')