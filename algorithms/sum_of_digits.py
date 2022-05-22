# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

#O(n)
n_number = int(input('Enter your number: '))

i = 1
num_1 = 1
num_2 = 2
result = 0

while i <= n_number:
    result += i
    i = i + 1
print(result)
