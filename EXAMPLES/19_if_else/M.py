val=int(input('Enter a number: '))

#print('even' if val%2==0 else 'odd')

#print(('%d is even' if val%2==0 else '%d is odd') %val)

#print(('{0} is even' if val%2==0 else '{0} is odd').format(val))

print(('{x} is even' if val%2==0 else '{x} is odd').format(x=val))