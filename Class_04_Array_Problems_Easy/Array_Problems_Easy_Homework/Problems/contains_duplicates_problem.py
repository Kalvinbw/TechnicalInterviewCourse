# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 3, 4]
input_array = [1, 2, 3, 4]
# Output = True

# brute
def brute(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            # if the outer array = the inner array then we return true
            if array[i] == array[j]:
                return True
    return False

# optimized
def opt(array):
    # dict to hold values
    nums = {}

    for item in array:
        # if the value is in the dict then we return true
        if item in nums:
            return True
        nums[item] = 1
    
    return False



print(brute(input_array))
print(opt(input_array))

