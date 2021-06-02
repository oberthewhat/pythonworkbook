parrot = "Norwegian Blue"

# print('using indexs.... def has to be an easier way to do this')

# print(parrot)
# print(parrot[3])
# print(parrot[4])
# print()
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print('using negative indexs')

# print(parrot[-11])
# print(parrot[-1])
# print()
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print(parrot[:6])
# print(parrot[3:5])

print(parrot[0:6:2]) 
print(parrot[0:6:3])

number = '9,223 372;376.854:777'

seperators = number[1::4]



print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])