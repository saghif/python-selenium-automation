# Given an array of integers (positive and negative) find the largest continuous sum.


# O(N)
def find_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    print(max_sum)


test_data = [1, 2, -1, 3, 4, 10, 10, -10, -1]  # 29
find_sum(test_data)
