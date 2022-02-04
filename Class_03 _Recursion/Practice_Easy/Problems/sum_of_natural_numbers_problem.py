# Write a function that sums all natural numbers that lead up to a given value using recursion

def sum_natural(n):
    if n <= 0:
        return 0
    return sum_natural(n - 1) + n

print(sum_natural(5))

def sum_num(n):
    if n == 0:
        return 0
    return sum_num(n-1) + (n-1)

print(sum_num(5))

def practice(num):
    if num == 0:
        return num

    return practice(num-1) + (num-1)

print(practice(5))