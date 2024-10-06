#x=[47,71,21,35,93,21]
x=[47,71,21,32,93,21]

flag=False

i=len(x)

while i:
	i=i-1
	if x[i]%2==0:
		flag=True
		break
	print('----')
else:
	print('Hello')

print('even - {}'.format(x[i]) if flag else 'no even')