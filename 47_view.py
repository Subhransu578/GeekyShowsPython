from numpy import *
a = array([10,20,30,40])
b = a.view()
print(a)
print(b)
print(id(a))
print(id(b))
a[1]=25
b[2]=35
print(a)
print(b)