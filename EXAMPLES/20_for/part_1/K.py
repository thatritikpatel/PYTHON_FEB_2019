x=[34,21,67,2,9,51]

print(x)

start=int(input('Enter first number: '))
end=int(input('Enter second number: '))

step=0

if start<end:
	step=1
	end=end+1
else:
	step=-1
	end=end-1

for i in range(start,end,step):
	#print(i)
	print(x[i])

