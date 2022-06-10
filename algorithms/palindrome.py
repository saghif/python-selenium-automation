# Given a string, write a python function to check if it is palindrome or not.
# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.


def is_palindrome(s):
    return s == s[::-1]


test_s_pos = 'radar'
test_s_neg = 'radax'

print(is_palindrome(test_s_pos))
print(is_palindrome(test_s_neg))

# string[start:stop:-1]
