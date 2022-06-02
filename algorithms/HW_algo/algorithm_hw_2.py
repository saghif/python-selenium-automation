# HW-SPLIT IN HALF
# Result = ‘aaaaabbbbbc’
# string_s = 'bbbbbcaaaaa'
# if len(string_s)%2 == 0:
#     s1 = string_s[:len(string_s) // 2]
#     s2 = string_s[len(string_s) // 2:]
#     print(s2 + s1)
# if len(string_s) % 2 != 0:
#     s1 = string_s[:len(string_s) // 2 + 1]
#     s2 = string_s[len(string_s) // 2 + 1:]
#     print(s2 + s1)


# HW2-Unique Characters in String
string_d = 'apple'
new_set = set(string_d)
def no_dups(s):
    if len(s) == len(new_set):
        return True
    else:
        return False

print(no_dups(string_d))