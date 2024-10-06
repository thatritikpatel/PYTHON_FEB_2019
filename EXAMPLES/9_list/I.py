#extend vs append

x=[12,13,14]
y=[1,2]

#adds one record at a time
#x.append(12)
x.append(y)  #NOT OK

print(type(x[0]))
print(type(x[1]))
print(type(x[2]))
print(type(x[3]))

z=[1,2]

print(y is x[3])

#adds all records of a given sequence
#x.extend(12) #NOT OK
#x.extend(12)

#print(x)
