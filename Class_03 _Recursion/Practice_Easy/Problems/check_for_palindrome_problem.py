# Write a function that checks if a string is a palindrome using recursion

def practice(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False

    return practice(s[1:-1])

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

print(practice('tacocat'))