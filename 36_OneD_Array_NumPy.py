# One way:
# import numpy
# roll = numpy.array([10,20,30,40,50])
# print(roll)

# Another way:
# from numpy import *
# roll = array([1,2,3,4,5])
# print(roll)
# print(type(roll))
# print(roll.dtype)

# Ex-1:
# from numpy import *
# # roll = array([1,2,3,4,5],int)
# roll = array([1,2,3,4,5],dtype=int)
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])

# Ex-2:
# from numpy import *
# name = array(['Ducati','Kawasaki','Honda','Yamaha'])
# print(name)
# print(name.dtype)

# Ex-3 :
# from numpy import *
# name = array(['Ducati','Kawasaki','Honda','Yamaha'])
# for i in range(len(name)):
#     print(name[i])

# Ex-4 :
from numpy import *
name = array(['Ducati','Kawasaki','Honda','Yamaha'])
i=0
while i<len(name):
    print(name[i])
    i+=1