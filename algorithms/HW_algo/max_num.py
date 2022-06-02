# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# O(1)

num_1 = int(input('Enter the 1st number: '))
num_2 = int(input('Enter the 2nd number: '))
num_3 = int(input('Enter the 3rd number: '))
n_number = [num_1,  num_2,  num_3]
result = max(n_number)

print(result)

#manual way:
# def find_max(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         return n1
#     if n2 > n1 and n2 >n3:
#         return n2
#     return n3
# print(find_max(num_1, num_2, num_3))