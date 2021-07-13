"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        op = []
        check = []
        for each in range(left,right+1):
            if "0" not in str(each):
                for every in str(each):
                    if each % int(every) == 0:
                        check.append(True)
                    else:
                        check.append(False)
                if False not in check:
                    op.append(each)
                check = []
        return op