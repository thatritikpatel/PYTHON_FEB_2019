import time

a=time.perf_counter()

#x=[i*i for i in range(100000000)]
x=(i*i for i in range(100000000))

b=time.perf_counter()




print(b-a)