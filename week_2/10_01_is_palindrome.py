input = "abcba"


def is_palindrome(string):
    avg = len(string) // 2
    for i in range(avg):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


print(is_palindrome(input))