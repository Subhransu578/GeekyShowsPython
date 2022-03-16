from numpy import *
row = int(input('Enter rows: '))
col = int(input('Enter columns: '))
a = zeros((row,col), dtype=int)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(input('Enter element: '))

print('2D array')
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

print('3D array')
arr = int(input('Enter no of array: '))
row1 = int(input('Enter row for 3D array: '))
col1 = int(input('Enter column for 3D array: '))
b = reshape(a,(arr,row1,col1))
print(b)