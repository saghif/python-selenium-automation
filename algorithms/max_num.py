# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# O(1)

num_1 = int(input('Enter the 1st number: '))
num_2 = int(input('Enter the 2nd number: '))
num_3 = int(input('Enter the 3rd number: '))
n_number = [num_1,  num_2,  num_3]
result = max(n_number)

print(result)