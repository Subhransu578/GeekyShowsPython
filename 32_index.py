# without user input:
# from array import *
# roll = array('i',[10,20,30,40,50])
# print(roll.index(30))

# With user input:
from array import *
roll = array('i',[])
num = int(input('Enter the size: '))
for i in range(num):
    roll.append(int(input('Enter number: ')))
print('**** Your numbers ****')
for i in range(num):
    print('Roll:',roll[i])
ele = int(input('Which number index you want to know: '))
print('Index of',ele,'is:',roll.index(ele))