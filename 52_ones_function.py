# 2D Array:
from numpy import *
a = ones((3,2))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])