rows=int(input('Enter number of Rows: '))
cols=int(input('Enter number of columns: '))
step=int(input('Enter Step: '))


a=65
for i in range(rows):
	for j in range(cols):
		print(chr(a),end=' ')
		a=a+step
	print()
