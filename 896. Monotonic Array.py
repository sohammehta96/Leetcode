"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""
def isMonotonic(nums):
    cond = []
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            cond.append(True)
        elif nums[i-1] < nums[i]:
            cond.append(False)
    if len(set(cond)) <= 1:
        return True
    return False