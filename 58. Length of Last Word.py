"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if s == len(s) * " ":
            return 0
        else:
            arr = s.split(" ")
            for i in range(len(arr)):
                if arr[len(arr)-1-i] != "":
                    return len(arr[len(arr)-1-i])