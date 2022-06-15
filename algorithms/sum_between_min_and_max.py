# Find a sum of elements between min and max elements.
# Min and max elements are not included.
# All numbers are unique.

def sum_between_min_and_max(arr):
    if len(arr) < 2:
        return

    min_item = max_item = arr[0]
    min_index = max_index = i = 0
    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


print(sum_between_min_and_max([6, 3, 5, 1]))
