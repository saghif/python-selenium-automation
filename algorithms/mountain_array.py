# Given an array of integers, return true if the following conditions are fulfilled:
# - length of the array is bigger than or equal to 3
# - there exists some index i such that:
# a[0] < a[1] < ... < a[i]
# a[i] > a[i+1] > ... > a[a.size-1]
#
# Basically, find if there is an increasing subarray followed by a decreasing subarray
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true


# O(N)
def is_mountain(array):
    if len(array) < 3:
        return False

    i = 1
    while i < len(array) and array[i] > array[i - 1]:
        i += 1
    if i == 1 or i == len(array):
        return False
    while i < len(array) and array[i] < array[i - 1]:
        i += 1

    return i == len(array)


test_data_pos = [1, 4, 7, 9, 5, 2]  # True
test_data_neg = [1, 4, 7, 9, 5, 6]  # False

print(is_mountain(test_data_pos))
print(is_mountain(test_data_neg))
