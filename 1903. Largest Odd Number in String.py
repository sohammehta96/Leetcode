"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
"""
def largestOddNumber(self, num: str) -> str:
    i = len(num)
    while i > 0 and int(num[i-1]) % 2 == 0:
        i -= 1
    if i == 0:
        return ""
    return num[:i]