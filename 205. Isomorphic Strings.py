"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
def isIsomorphic(s: str, t: str):
    mydict = {}
    for i in range(len(s)):
        if s[i] not in mydict:
            mydict[s[i]] = t[i]
    for i in range(len(t)):
        if mydict[s[i]] != t[i]:
            return False
    mydict = {}
    for i in range(len(t)):
        if t[i] not in mydict:
            mydict[t[i]] = s[i]
    for i in range(len(s)):
        if mydict[t[i]] != s[i]:
            return False
    return True