"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
def containsNearbyDuplicate(nums, k):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] not in mydict:
            mydict[nums[i]] = [i]
        else:
            mydict[nums[i]].append(i)
    for each in mydict:
        for i in range(len(mydict[each])-1):
            if abs(mydict[each][i] - mydict[each][i+1]) <= k:
                return True
    return False