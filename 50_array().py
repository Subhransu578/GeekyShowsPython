# 2D Array
# With Index:
# from numpy import * 
# a = array([[10,20,30],[40,50,60]])
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()

# Without index:
# from numpy import *
# a = array([[10,20],[30,40]])
# for i in a:
#     for j in i:
#         print(j)
#     print()

# While loop :
from numpy import *
a = array([[10,20],[30,40]])
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j+=1
    i+=1