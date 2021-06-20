"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
    
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                max_current = max(nums[i], max_current+nums[i])
                max_global = max(max_global, max_current)    

        return max_global