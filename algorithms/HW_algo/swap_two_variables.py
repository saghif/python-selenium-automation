# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.


# O(1)
a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a}, b = {b}')

# temp = a
# a = b
# b = temp

# a, b = b, a

a = a + b  # 10 + 5 = 15
b = a - b  # 15 - 5 = 10
a = a - b  # 15 - 10 = 5

print(f'a = {a}, b = {b}')
