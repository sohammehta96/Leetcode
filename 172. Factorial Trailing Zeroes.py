"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 0
    
        i = 1
        while 5**i <= n:
            s += n//(5**i)
            i += 1
        return s