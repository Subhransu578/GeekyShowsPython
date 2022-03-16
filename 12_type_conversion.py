# implicit type conversion :
# ex1:
# a = 10 # int type
# b = 4 # int type
# value = a/b
# print(value)
# print(type(value)) # Float type

# ex2:
# a = 10
# b = '10'
# value = a+b
# print(value) # you can not add int and string

# explicit type conversion :
# ex1:
# a = 10
# b = 4
# value = int(a/b)
# print(value)
# print(type(value))

# ex2:
a = 10
b = '10'
value = a+int(b) # here you type cast the variable b string to int, but not add string to int
print(value)
print(type(value))