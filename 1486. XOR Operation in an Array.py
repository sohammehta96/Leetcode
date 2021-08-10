"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""
def xorOperation(self, n: int, start: int) -> int:
    add = 0
    for i in range(n):
        add = add^(start+2*i)
    return add