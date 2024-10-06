#Case 1:
#import xyz.B
#import xyz.mno.C

#Case 2:
#from xyz.B import f1
#from xyz.mno.C import f1

#Case 3:
#from xyz.B import f1 as a
#from xyz.mno.C import f1 as b

print('--- in A')

#Case 3:
#a()
#b()

#Case 2:
#f1()
#f1()

#Case 1:
#xyz.B.f1()
#xyz.mno.C.f1()