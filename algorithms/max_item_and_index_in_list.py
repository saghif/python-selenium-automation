# Given a list of random numbers.
# Find and return the max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10], print [3, 76]


def find_max_item_and_its_index_in_list(arr):
    max_num = arr[0]
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    print([max_index, max_num])


find_max_item_and_its_index_in_list([1, 45, 33, 76, 9, 10])
