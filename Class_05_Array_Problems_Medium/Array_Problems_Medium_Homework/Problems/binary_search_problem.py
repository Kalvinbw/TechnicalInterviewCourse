# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# Output = 2

def binary_search(array, n):
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l + r) // 2

        if array[mid] == n:
            return mid
        
        if array[mid] < n:
            l = mid + 1
        elif array[mid] > n:
            r = mid - 1
        
    return -1

print(binary_search(input_array, input_target))