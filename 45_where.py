# In where() supose your array name is a and b, if a>b if this condition is True means 1st element of a is greater than 1st element of b then it give a's value else it give b's value.

# Ex-1:
# from numpy import *
# a = array([10,20,30,40])
# b = array([10,2,50,55])
# c = where(a>b,a,b)
# print(c)

# Ex-2:
# from numpy import *
# a = array([10,20,30,40])
# b = array([10,2,50,55])
# c = where(a==b,a,b)
# print(c)

# Ex-3:
# from numpy import *
# a = array([10,2,30,40])
# b = array([1,20,5,55])
# c = where(a<b,a,b)
# print(c)

# Ex-4:
# from numpy import *
# a = array([10,2,30,40])
# b = array([1,20,30,55])
# c = where(a<=b,a,b)
# print(c)

# Ex-5:
# from numpy import *
# a = array([10,2,30,40])
# b = array([1,20,30,55])
# c = where(a>=b,a,b)
# print(c)

# Ex-6:
from numpy import *
a = array([10,2,30,40])
b = array([1,20,30,55])
c = where(a!=b,a,b)
print(c)