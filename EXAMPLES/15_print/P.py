name=input('Enter your name: ')
age=int(input('Enter your Age: '))
marks=float(input('Enter Marks: '))

#print('{a} is a good student and he is {b} and he scored {c}'.format(a=name,b=age,c=marks))
print('{a} is a good student and he is {b} and he scored {c}'.format(c=marks,b=age,a=name))