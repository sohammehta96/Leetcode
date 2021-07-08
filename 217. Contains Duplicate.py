"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        return True if len(set(nums)) < len(nums) else False