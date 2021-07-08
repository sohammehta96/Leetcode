"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for each in s:
            if each.isalpha() or each.isnumeric():
                string += each.lower()
        if string == string[::-1]:
            return True
        return False