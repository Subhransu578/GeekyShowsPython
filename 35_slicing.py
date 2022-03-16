# Without user input:
# from array import *
# roll = array('i',[11,12,13,14,15])
# # slc_roll = roll[0:4:]
# slc_roll = roll[:4:]
# # slc_roll = roll[0:4:2]
# for i in range(len(slc_roll)):
#     print(slc_roll[i])

# With user input:
from array import *
roll = array('i',[])
num = int(input('Enter the size: '))
for i in range(num):
    roll.append(int(input('Enter element: ')))
print('***** Your Element *****')
for i in range(num):
    print('Index:',i,'Roll:',roll[i])
fst_pos = int(input('Enter the starting position you want to display: '))
lst_pos = int(input('Enter the ending position you want to stop display: '))
step = int(input('Enter the step size: '))
slc_roll = roll[fst_pos:lst_pos:step]
print('***** After Slicing *****')
for i in range(len(slc_roll)):
    print('Index:',i,'Roll:',slc_roll[i])