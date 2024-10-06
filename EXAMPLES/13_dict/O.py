x={'Manager':8989674534,'CEO':7845123423}

print(x)

key=input('Enter key: ')

if key in x:
	y=x.pop(key)
	print(y)
	print(x)
else:
	print('Invalid Key')