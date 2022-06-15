# Given an array of integers. Calculate sum and multiplication of elements.
# Return the list, calculated sum, and multiplication of elements
# Example: [1, 7, 3] Return: [11, 21]


def sum_and_mult(arr):
    sum_of_list = 0
    mult_of_list = 1
    for i in arr:
        sum_of_list += i
        mult_of_list *= i

    return [sum_of_list, mult_of_list]


print(sum_and_mult([1, 7, 3]))
