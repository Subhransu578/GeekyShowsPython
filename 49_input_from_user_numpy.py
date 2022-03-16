from numpy import *
num = int(input('Enter number of elements: '))
a = zeros(num,dtype=int)
for i in range(num):
    a[i] = int(input('Enter elements: '))

for i in range(num):
    print(a[i])