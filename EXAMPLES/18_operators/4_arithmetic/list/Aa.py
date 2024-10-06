x=[12,34,56]
y=[1,2,3]

print(id(x))


z=x.extend(y)

print(id(x))

print(y)
print(z)