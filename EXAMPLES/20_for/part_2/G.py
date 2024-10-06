x=[67,32,91,42,29,78,13]

print(x)

flag=False

print('------1')


#Case 2:
for i in x:
	if i%2==0:
		flag=True
		break
	print('---')


#Case 1:
'''
for i in x:
	if i%2==0:		
		flag=True
	print('---')
'''

print('even number exists' if flag else 'no even number')






