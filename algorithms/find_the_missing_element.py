# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# [1,2,3,4,5,6,7], [3,7,2,1,4,6]
#
# Output:
# 5 is the missing number


# [2,1,3,7,5,6,4], [3,7,2,1,4,6] -> 5

# SORTED: [1,2,3,4,5,6,7], [1,2,3,4,5,6]
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7

# O(N)
# def find_missing_number(arr1, arr2):
#     arr1.sort()  # O(N * logN)
#     arr2.sort()
#
#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1
#
#     return arr1[-1]

import collections


# {key1: value1, key2: value2}
# O(N)
def find_missing_number(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


test_arr1 = [1, 2, 3, 4, 5, 6, 7]
test_arr2 = [3, 7, 2, 1, 4, 6]

print(find_missing_number(test_arr1, test_arr2))  # 5
