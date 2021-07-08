"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cond = []
        mydict = {}
        for each in s:
            if each not in mydict:
                mydict[each] = 1
            else:
                mydict[each] += 1
        for each in mydict:
            if t.count(each) == mydict[each]:
                cond.append("True")
            else:
                cond.append("False")
        
        if "False" in cond:
            return False
        return True