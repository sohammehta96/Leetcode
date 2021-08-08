"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""

def findLucky(arr):
    lucky = []
    for each in arr:
        if arr.count(each) == each:
            lucky.append(each)
    if len(lucky) >= 1:
        return max(lucky)
    return -1