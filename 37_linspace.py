# Ex-1:
# from numpy import *
# number = linspace(1,8)
# for i in range(len(number)):
#     print(number[i])

# Ex-2:
# from numpy import *
# number = linspace(1,8,5)
# for i in range(len(number)):
#     print(number[i])

# Ex-3:
# from numpy import *
# number = linspace(1,8,5,endpoint=False)
# for i in range(len(number)):
#     print(number[i])

# Ex-4:
# from numpy import *
# number = linspace(1.3,8.2,5)
# for i in range(len(number)):
#     print(number[i])

# Ex-5: TypeError
from numpy import *
number = linspace('a','e')
for i in range(len(number)):
    print(number[i])