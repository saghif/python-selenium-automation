fibonacci = int(input('Enter your number here '))

index = 3
fib_1 = 1
fib_2 = 1
result = [fib_1, fib_2]
while index <= fibonacci:
    result.append(fib_1 +  fib_2)
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index = index + 1  # index += 1

print(result)

# O(n)