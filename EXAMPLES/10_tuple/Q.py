x=(12,34,[100,200],45)

print(id(x))
print(x[0])
print(x[1])
print(x[2][0])
print(x[2][1])
print(x[3])

#x[0]=34
x[2][0]=300
#x[2].append(400)
#x[2][2]=400
#x.append(23)

print(id(x))
print(x)