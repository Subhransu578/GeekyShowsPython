# one type:
# import array
# roll = array.array('i',[10,20,30,40,50])
# for i in range(len(roll)):
#     print('Index:',i,'Roll:',roll[i])

# import array
# roll = array.array('i',[10,20,30,40,50])
# i = 0
# while i<len(roll):
#     print('Index:',i,'Roll:',roll[i])
#     i+=1


# Second type:
# from array import *
# roll = array('i',[10,20,30,40,50])
# for i in range(len(roll)):
#     print('Index:',i,'Roll:',roll[i])

# from array import *
# roll = array('i',[10,20,30,40,50])
# i=0
# while i<len(roll):
#     print('Index:',i,'Roll:',roll[i])
#     i+=1


# Getting input from user:
# in for loop:
# from array import *
# num = int(input('Enter the number of students: '))
# roll = array('i',[])
# for i in range(num):
#     roll.append(int(input('Enter the student roll numbers: ')))
# for i in range(num):
#     print('Student:',i+1,'Rollno:',roll[i])

# in while loop:
from array import *
num = int(input('Enter the number of students: '))
roll = array('i',[])
i=0
while i<num:
    roll.append(int(input('Enter the student roll numbers: ')))
    i+=1
i=0
while i<num:
    print('Student:',i+1,'Rollno:',roll[i])
    i+=1