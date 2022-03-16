# Ex-1:
# from numpy import *
# number = logspace(1,3)
# for i in range(len(number)):
#     print(number[i])

# Ex-2:
# from numpy import *
# number = logspace(1,3,5)
# for i in range(len(number)):
#     print(number[i])

# Ex-3:
# from numpy import *
# number = logspace(1,3,5,base=12.0)
# for i in range(len(number)):
#     print(number[i])

# Ex-4:
# from numpy import *
# number = logspace(1.2,3,5)
# for i in range(len(number)):
#     print(number[i])

# Ex-5:
# from numpy import *
# number = logspace(1.2,3.5,5)
# for i in range(len(number)):
#     print(number[i])

# Ex-6: TypeError: 'float' object cannot be interpreted as an integer
from numpy import *
number = logspace(1.2,3.5,5.3)
for i in range(len(number)):
    print(number[i])