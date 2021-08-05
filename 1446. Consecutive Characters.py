"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
"""
def maxPower(self, s: str) -> int:
    if len(s) == 1:
        return 1
    start = 0
    end = 0
    max_length = 0
    while end <= len(s)-1:
        if s[start] == s[end]:
            end += 1
            if end-start > max_length:
                max_length = end-start
        else:
            start = end
    return max_length