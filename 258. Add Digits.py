"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

"""

class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        else:
            result = 0
            for each in str(num):
                result += int(each)
            return self.addDigits(result)