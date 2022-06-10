# Write a function to check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.
# simple way:
# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     return sorted(str1) == sorted(str2)
#
#
# str_1 = 'abc'
# str_2 = 'bcds'
# print(is_anagram(str_1, str_2))

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}  # {"key_1": "value_1", "key_2": "value_2"}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


tests1_pos = 'abcd'
tests2_pos = 'badc'
tests1_neg = 'abcd'
tests2_neg = 'abca'
print(is_anagram(tests1_pos, tests2_pos))
print(is_anagram(tests1_neg, tests2_neg))


# tests1_neg = 'abcd'
# tests2_neg = 'abca'

# count{}
# a = 1 -1 = 0 - 1 = -1
# b = 1 -1 = 0
# c = 1 -1 = 0
# d = 1
