"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
def isSubsequence(s: str, t: str) -> bool:
    si = 0
    ti = 0
    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            si += 1
        ti += 1
    if si == len(s):
        return True
    return False