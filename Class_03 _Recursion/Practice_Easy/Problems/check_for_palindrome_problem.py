# Write a function that checks if a string is a palindrome using recursion

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True

    left = s[0] 
    right = s[len(s) - 1]

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

print(palindrome('tacocat'))