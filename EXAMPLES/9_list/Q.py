x=[12,23,45]
y=[12,23,45]

z=x.copy()  #Deep copy
#z=x   #shalow copy

print(id(x))
print(id(y))
print(id(z))

print(x is z)

#print(x)
#print(y)
#print(z)