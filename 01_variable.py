a = 10
b = 10
print(type(a)) # here type is used to know the variable data type.
print(id(a)) # id is used to know the variable address.
print(id(b)) # But in python variable have no address, value have the address.
a = 20
print(id(a))
y = a
print(a)
print(y)