#x=[23,71,35,53,61]
x=[23,72,35,53,61]

flag=False
for i in x:
	if i%2==0:
		flag=True
		break
	print('---')
else:
	print('Hello')

print('even' if flag else 'no even')