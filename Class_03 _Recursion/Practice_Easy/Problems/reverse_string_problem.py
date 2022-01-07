# Write a function that reverses a string using recursion

def reverse(s):
    if s == '':
        return ''
    return reverse(s[1:]) + s[0]

print(reverse('kalvin'))