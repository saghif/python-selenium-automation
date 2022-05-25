# When User enters a number, its factorial is displayed.

import math

number = int(input('Input a number: '))
# result = 1

# O(n)
# for i in range(1, number + 1):
#     result = result * i  # result *= i

result = math.factorial(number)

print(f'Result: {result}')

