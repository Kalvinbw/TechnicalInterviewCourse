# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand. You may assume no duplicate exists in the array.
# This problem came from leetcode.com

input_array = [6, 1, 2, 3, 4, 5]
# Output = 1

def find_min(array):
    l = 0
    r = len(array) - 1
    min_val = array[0]

    while l <= r:
        mid = (l + r) // 2

        if array[mid] > array[mid-1]:
            l = mid
        elif array[mid] < array[mid+1]:
            r = mid
        elif array[mid] < array[mid+1]:
            return array[mid]


def minimum_rotated_sorted_array_optimized(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        guess = (low + high) // 2
        if nums[guess] > nums[high]:
            low = guess + 1
        else:
            high = guess

    return nums[low]

# print(find_min(input_array))

print(minimum_rotated_sorted_array_optimized(input_array))