"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
"""
def findDisappearedNumbers(nums):
    mydict = {}
    for each in nums:
        if each not in mydict:
            mydict[each] = 1
    op = []
    for each in list(range(1,len(nums)+1)):
        if each not in mydict:
            op.append(each)
    return op