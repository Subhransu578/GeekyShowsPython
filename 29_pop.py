# Without user input:
# from array import *
# number = array('i',[1,2,3,4,5])
# for i in range(len(number)):
#     print(number[i])
# print('After pop')
# number.pop()
# for i in range(len(number)):
#     print(number[i])

# With user input:
from array import *
arr = array('i',[])
num = int(input('Enter the size of array: '))
for i in range(num):
    arr.append(int(input('Enter the number: ')))
for i in range(num):
    print(arr[i])
print('After pop')
arr.pop()
for i in range(len(arr)):
    print(arr[i])