rows=int(input('Enter number of Rows: '))
cols=int(input('Enter number of columns: '))

#Case 1:
'''
a=65
for i in range(rows):
	for j in range(cols):
		print(chr(a),end=' ')
	a=a+1
	print()
'''

#Case 2:
'''
a=65
for i in range(rows):
	for j in range(cols):
		print(chr(a+i),end=' ')			
	print()
'''