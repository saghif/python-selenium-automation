from random import randint

random_number = randint(100, 999)
print(f'The random num is: {random_number}')

result = 0
for digit in str(random_number): #349 -> [3,4,9] string
    result = result + int(digit)

print(f'Result: {result}')

#method to use:
while random_number != 0:
    result = +(random_number % 10)
    random_number = random_number // 10
print(f'Result: {result}')

#O(n) n = length of random_number
