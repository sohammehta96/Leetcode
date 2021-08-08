"""
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
"""
def thirdMax(nums):
    i = 1
    if len(set(nums)) < 3:
        return max(nums)
    while len(set(nums)) >= 1 and i <= 3:
        a = nums.pop(nums.index(max(nums)))
        while a in nums:
            nums.pop(nums.index(a))
        i += 1
    return a