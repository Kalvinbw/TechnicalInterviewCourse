# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division
# This problem came from leetcode.com

input_array = [1, 2, 3, 4]
# Output = [24, 12, 8, 6]

def sum_not_self(array):
    sum = 1
    output = []
    for item in array:
        sum *= item
    
    for item in array:
        v = sum // item
        output.append(v)

    return output

def sum_new(array):
    output = []
    for i in range(len(array)):
        s = 1
        for j in range(len(array)):
            if j != i:
                s *= array[j]
        output.append(s)
    return output


print(sum_new(input_array))
    
