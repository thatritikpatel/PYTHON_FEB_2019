gen=input('Enter gender(m/f): ')
age=int(input('Enter age: '))
chq=input('Do you want cheque book(y/n): ')

if (gen=='m' or gen=='f') and (age>0 and age<=100):
	if gen=='m':
		if age>=60:
			print('MB:',2000+(500 if chq=='y' else 0),' and RI:',11)
		elif age<=22:
			print('MB:',500+(500 if chq=='y' else 0),' and RI: ',2)
		else:
			print('MB:',5000+(500 if chq=='y' else 0),' and RI: ',6)
	else:
		if age>=60:
			print('MB:',0+(500 if chq=='y' else 0),' and RI: ',12)
		elif age<=22:
			print('MB:',0+(500 if chq=='y' else 0),' and RI: ',4)
		else:
			print('MB:',2000+(500 if chq=='y' else 0),' and RI: ',8)
elif gen!='m' and gen!='f':
	print('Invalid Gender')
else:
	print('Invalid Age')






