# Your input is an array of integers, and you have
# to reorder its entries so that the even entries
# appear first. You are required to solve it without allocating
# additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
# input_num = input('enter an array of integers: ')
# result = list(input_num)
#
#
# def even_first(arr):
#     for i in arr:
#         x = int(i)
#         if (x % 2) != 0:
#             y = str(x)
#             arr.append(arr.pop(arr.index(y)))
#
#     return arr
#
#
# print(even_first(result))


#Increment a Number
#Write a program that takes as input an array of digits
# represent the integer D + 1.
#For example, if the input is [1, 2, 9]
# then you should update the array to [1, 3, 0].
input_num = int(input('enter 3 digits: '))
#result = list(input_num)
x = (input_num)  + 1
string_num = str(x)
list_num = list(string_num)
print(list_num)




