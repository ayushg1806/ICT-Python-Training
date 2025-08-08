#Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome('madam'))