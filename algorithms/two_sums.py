# Given an array of integers nums and an integer target.
# Return two numbers from the array such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# O(N)
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    sum_set = set()

    for num in arr:
        target_value = k - num
        if target_value not in sum_set:
            sum_set.add(num)
        else:
            return [target_value, num]


test_data = [3, 7, 5, 9, 15, 3]
test_target = 16

print(pair_sum(test_data, test_target))  # [3, 3]
