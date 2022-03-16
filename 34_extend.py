# Without user input:
# from array import *
# roll = array('i',[5,3,9,4,8])
# roll2 = array('i',[1,7,2])
# roll.extend(roll2)
# for i in range(len(roll)):
#     print(roll[i])

# With user input:
from array import *
roll = array('i',[])
num = int(input('Enter size of 1st array: '))
for i in range(num):
    roll.append(int(input('Enter element of 1st array: ')))
print('***** 1st array *****')
for i in range(num):
    print(roll[i])

roll2 = array('i',[])
num2 = int(input('Enter size of 2nd array: '))
for i in range(num2):
    roll2.append(int(input('Enter element of 2nd array: ')))
print('***** 2nd array *****')
for i in range(num2):
    print(roll2[i])

print('****** After Extend ******')
roll.extend(roll2)
for i in range(len(roll)):
    print(roll[i])