"""
The next greater element of some element x in an array is the first greater element 
that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
and determine the next greater element of nums2[j] in nums2. If there is no next greater element, 
then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""
def nextGreaterElement(nums1, nums2):
    op = []
    for i in range(len(nums1)):
        j = nums2.index(nums1[i]) + 1
        if j >= len(nums2):
            op.append(-1)
        else:
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    op.append(nums2[j])
                    break
                else:
                    j += 1
            if j == len(nums2):
                op.append(-1)
    return op