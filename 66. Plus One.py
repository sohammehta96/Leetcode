"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def plusOne(self, digits):
        num = digits[0]
    
        for i in range(1,len(digits)):
            num = (num*10) + digits[i]

        num += 1
        return [int(list(str(num))[i]) for i in range(len(str(num)))]