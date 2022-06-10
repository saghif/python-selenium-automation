# Given an array of integers, write a function to move all 0's to the end
# while maintaining the relative order of the other elements.
# 0 4 0 3 12  ->  4 3 12 0 0

# O(N)
def move_zeroes(arr):
    j = 0
    # 0 4 0 3 12
    # ->>
    # 4 3 12 3 12
    # ->>
    # 4 3 12 0 0
    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1

    while j < len(arr):
        arr[j] = 0
        j += 1

    return arr


test_data = [0, 4, 0, 3, 12]
print(move_zeroes(test_data))
