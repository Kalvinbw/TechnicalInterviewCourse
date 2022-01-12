# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5

# brute force approach
def brute(array):
    if len(array) == 0:
        return 0

    max = 0

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            dif = array[j] - array[i]
            if dif > max:
                max = dif
    return max

# optimized
def opt(array):
    if len(array) == 0:
        return 0
    min = array[0]
    max = 0
    for i in range(0, len(array)):
        if array[i] < min:
            min = array[i]
        dif = array[i] - min
        if dif > max:
            max = dif
    return max


print(brute(input_array))
print(opt(input_array))