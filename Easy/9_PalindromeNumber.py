def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if (x < 0):
        return False
    #               reverse the string
    return str(x) == str(x)[::-1]

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(135797531))