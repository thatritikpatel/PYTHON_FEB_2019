x=int(input('Enter First Number: '))
y=int(input('Enter Second Number: '))
z=int(input('Enter Third Number: '))

#a=x if x>y>z else y if y>z else z


a=x if x>y and x>z else y if y>z else z

print(a)