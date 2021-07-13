"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        a = ''.join([str(elem) for elem in nums])
        b = a.split("0")
        long = 0
        for each in b:
            if len(each) > long:
                long = len(each)
        return long