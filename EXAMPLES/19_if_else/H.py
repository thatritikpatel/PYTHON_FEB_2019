gen=input('Enter gender(m/f): ')
age=int(input('Enter age: '))


if gen=='m':
	if age>=60:
		print('MB:',2000,' and RI:',11)
	elif age<=22:
		print('MB:',500,' and RI: ',2)
	else:
		print('MB:',5000,' and RI: ',6)
elif gen=='f':
	if age>=60:
		print('MB:',0,' and RI: ',12)
	elif age<=22:
		print('MB:',0,' and RI: ',4)
	else:
		print('MB:',2000,' and RI: ',8)
else:
	print('Invalid Input')
