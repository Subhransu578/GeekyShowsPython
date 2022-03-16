from array import *
roll = array('i',[10,20,30,40,50])
print('Before Append\n')
i=0
while i<len(roll):
    print(roll[i])
    i+=1

print('After Append\n')
roll.append(60)
j=0
while j<len(roll):
    print(roll[j])
    j+=1