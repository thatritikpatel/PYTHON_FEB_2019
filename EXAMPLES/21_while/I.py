x=[42,78,21,32,93,21]

flag=False

i=len(x)

while i:
	i=i-1
	if x[i]%2==0:
		flag=True
		break
	print('----')

print('even' if flag else 'no even',x[i])