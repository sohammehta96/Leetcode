"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(50000):
            if (i*i) == num:
                return True
            if (i*i) > num:
                return False