# Logical and :
# a = 5
# b = 3
# c = 4
# print(a>b and a>c) # True
# print(a>b and a<c) # False
# print(a<b and a>c) # False
# print(a<b and a<c) # False
# print(a>b and c) # c
# print(a>b and c and b) # b always last expression
# print(a<b and c) # False
# print(a<c and c and a) # False


# Logical or :
# a = 5
# b = 3
# c = 4
# print(a>b or a>c) # True
# print(a>b or a<c) # True
# print(a<b or a>c) # True
# print(a<b or a<c) # False
# print(a>b or c) # True
# print(a>b or c or b) # True
# print(a<b or c) # c
# print(a<c or c or a) # c always expression1

# Logical not :
a = 5
b = 3
# print(not(a>b)) # False
print(not(a<b)) # True