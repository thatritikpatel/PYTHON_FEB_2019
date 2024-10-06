flag=input('Do you want to perform some transaction (y/n): ')

while flag=='y':
	a=int(input('Enter first number: '))
	b=int(input('Enter second number: '))

	op=input('Enter +,-,*,/: ')

	if op=='+':
		print('{}+{}={}'.format(a,b,a+b))
	elif op=='-':
		print('{}-{}={}'.format(a,b,a-b))
	elif op=='*':
		print('{}*{}={}'.format(a,b,a*b))
	elif op=='/':
		print('{}/{}={}'.format(a,b,a/b))
	else:
		print('invalid operator')
	
	flag=input('Do you want to perform some transaction (y/n): ')
