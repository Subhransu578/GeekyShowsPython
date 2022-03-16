# Without user input:
# from array import *
# roll = array('i',[15,23,25,14,65])
# for i in range(len(roll)):
#     print(roll[i])
# print('**** After Reverse ****')
# roll.reverse()
# for i in range(len(roll)):
#     print(roll[i])

# With user input:
from array import *
roll = array('i',[])
num = int(input('Enter the size: '))
for i in range(num):
    roll.append(int(input('Enter element: ')))
print('**** Your Elements ****')
for i in range(num):
    print(roll[i])
print('**** After Reverse ****')
roll.reverse()
for i in range(num):
    print(roll[i])