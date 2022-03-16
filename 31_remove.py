# Without user input:
# from array import *
# number = array('i',[1,2,3,4,5])
# for i in range(len(number)):
#     print(number[i])
# print('After remove')
# number.remove(3)
# for i in range(len(number)):
#     print(number[i])

# With user input:
from array import *
roll = array('i',[])
num = int(input('How many number of input you want: '))
for i in range(num):
    roll.append(int(input('Enter your number: ')))
print('***** Your Numbers *****')
for i in range(num):
    print('Position:',i+1,'Roll:',roll[i])
ele = int(input('which number you want to remove: '))
print('***** After delete number *****')
roll.remove(ele)
for i in range(len(roll)):
    print('Position:',i+1,'Roll:',roll[i])