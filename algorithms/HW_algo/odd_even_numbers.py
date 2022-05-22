# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5)

# O(n)
n_number = input('Enter a number:' '')
n_number = int(n_number)

even_num = 0
odd_num = 0

while n_number > 0:
    if n_number % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    n_number = n_number // 10

print("Even:% d, odd:% d" % (even_num, odd_num))