# Write a function that reverses a string using recursion

def reverse(s):
    if s == '':
        return ''
    return reverse(s[1:]) + s[0]

print(reverse('kalvin'))















def reversal(str):
    if len(str) == 1:
        return str
    
    return reversal(str[1:]) + str[0]

print(reversal('kalvin'))