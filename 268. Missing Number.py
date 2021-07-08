"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
class Solution:
    def missingNumber(self, nums) -> int:
        i = 0
        while i in nums:
            i += 1
        return i