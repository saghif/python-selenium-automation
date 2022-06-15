# Write a program that takes as input a sorted array and updates it so that all duplicates
# have been removed and the remaining elements have been shifted left to fill the emptied indices.
# Fill the remaining indices with zeroes.
# Return the number of valid elements.
# You cannot use sets for this coding challenge.


def delete_duplicates(arr):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    for i in range(write_index, len(arr)):
        arr[i] = 0
    return write_index


test_array = [2, 3, 5, 7, 7, 11, 11, 11, 13]
print(test_array)
print(delete_duplicates(test_array))
print(test_array)
