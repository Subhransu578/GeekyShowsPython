# Operator Precedence :
# value = (1+1)*2**4//3+4-1 
# print(value)
# 2*2**4//3+4-1 --> parentheses
# 2*16//3+4-1 --> exponent
# 32//3+4-1 --> multiplication
# 10+4-1 --> floor division
# 14-1 --> addition
# 13 --> subtraction

value = 1+3*(2+8)**3-2//4 
print(value)
# 1+3*10**3-2//4 --> parentheses
# 1+3*1000-2//4 --> exponent
# 1+3000-2//4 --> multiplication
# 1+3000-0 --> floor division
# 3001-0 --> addition
# 3001 --> subtraction