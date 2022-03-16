# Without user input:
# from array import *
# roll = array('i',[10,20,30,40,50])
# print('Before insert:')
# for i in range(len(roll)):
#     print('Index:',i,'Roll:',roll[i])
# print('After insert:')
# roll.insert(2,25)
# for i in range(len(roll)):
#     print('Index:',i,'Roll:',roll[i])

# With user input:
from array import *
roll = array('i',[])
num = int(input('How many number of input you want: '))
for i in range(num):
    roll.append(int(input('Enter your number: ')))
print('***** Your Numbers *****')
for i in range(num):
    print('Position:',i+1,'Roll:',roll[i])
pos = int(input('In which position you want to add new number: '))
ele = int(input('Enter the new number: '))
print('***** After Insert new number *****')
roll.insert(pos-1,ele)
for i in range(len(roll)):
    print('Position:',i+1,'Roll:',roll[i])