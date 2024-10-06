#Case 1:
'''
f=open('abc.txt','w')

f.write('12')

f.close()
'''

#Case 2:

with open('abc.txt','r') as f:
	s=f.read()
	print(s)
	print(f.closed)

print('#######')
print(f.closed)
