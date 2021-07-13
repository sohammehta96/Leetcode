"""
A shift on s consists of taking string s and moving the leftmost character 
to the rightmost position. For example, 
if s = 'abcde', then it will be 'bcdea' after one shift on s. 
Return true if and only if s can become goal after some number of shifts on s.
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == len(goal) and len(s) == 0:
            return True
        for i in range(len(s)):
            if s[i:len(s)]+s[0:i] == goal:
                return True