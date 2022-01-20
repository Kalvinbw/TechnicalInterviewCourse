# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand. Find the maximum number in the sorted array. You may assume no duplicate exists in the array.
# This problem came from leetcode.com

input_array = [3, 4, 5, 1, 2]
input_array = [1, 2, 3, 4, 5]
# Output = 6

def find_max(array):
    l = 0
    r = len(array) - 1

    while l < r:
        mid = (l + r) // 2
        if array[mid] < array[l]:
            r = mid - 1
        else:
            l = mid
    return array[r]

print(find_max(input_array))
