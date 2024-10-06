for i in range(5):
	for j in range(i+1):
		if j%2!=0:
			print('---',i,j)
			break
	else:
		print('bye')
	print()
	if i%2==0:
		break
else:
	print('hello')