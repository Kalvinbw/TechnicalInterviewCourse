"""
Given an array nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1]  == 9)

Input: nums = [3,2,4], target = 6
Output: [1, 2] 

Input: nums = [3,3], target = 6
Output: [0,1]

Source: https://leetcode.com/problems/two-sum/
"""

nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3, 2]
target3 = 6

def two_sum (arr, target) :
    dic = {}
    for i, j in enumerate(arr) :
        needed_num = target - j
        if needed_num in dic : 
            return [dic[needed_num], i]
        else : 
            dic[j] = i

print(two_sum(nums2, target2))
