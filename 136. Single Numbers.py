"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums):
        for each in nums:
            if each != 1 and nums.count(each) == 1:
                return each
        return 1