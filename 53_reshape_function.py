# converting 1D to 2D array:
# from numpy import *
# a = array([1,2,3,4,5,6])
# b = reshape(a,(3,2)) # here 3 is no of row & 2 is column
# print(a)
# print(b)

# coverting 1D to 3D array:
# ex-1:
# from numpy import *
# a = array([1,2,3,4,5,6,7,8,9,10,11,12])
# b = reshape(a,(3,2,2)) # here 3 is no of array, 2 is no of row & 2 is no of column
# print(a)
# print(b)

# ex-2:
# from numpy import *
# a = array([1,2,3,4,5,6,7,8,9,10,11,12])
# b = reshape(a,(2,3,2)) # here 2 is no of array, 3 is no of row & 2 is no of column
# print(a)
# print(b)

# converting 2D to 1D array:
from numpy import *
a = array([[1,2,3],[4,5,6]])
b = reshape(a,(6))
print(a)
print(b)