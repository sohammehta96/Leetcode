"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""
def decompressRLElist(nums):
    i = 0
    op = []
    while i < len(nums):
        for j in range(nums[i]):
            op.append(nums[i+1])
        i += 2
    return op