# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z and it's not a palindrome.


def is_almost_palindrome(s):
    for i in range(len(s)):
        temp_s = s[:i] + s[i + 1:]
        if temp_s == temp_s[::-1]:
            return True

    return False


test_s_pos = 'radkar'
test_s_neg = 'radario'
print(is_almost_palindrome(test_s_pos))  # True
print(is_almost_palindrome(test_s_neg))  # false


# radario
# adario
# rdario
# raario
# radrio
# radaio
# radaro
# radari
