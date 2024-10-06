x=[42,78,21,33,90,24]

i=len(x)

while i:
	i=i-1
	if x[i]%2!=0:
		continue
	print(x[i],'is even')