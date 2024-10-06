def aaa():
	a=int(input('Enter a number: '))
	b=int(input('Enter Another Number: '))

	w=a+b
	x=a-b
	y=a*b
	z=a/b

	return w,x,y,z


t,u,v,w=aaa()
print('#############')
print(type(t),t)
print(type(u),u)
print(type(v),v)
print(type(w),w)