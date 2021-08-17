"""
Given a string s, check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together.
"""
def repeatedSubstringPattern(s: str):
    if len(s) > 1 and s[0]*len(s) == s:
        return True
    for i in range(2,(len(s)//2)+1):
        if len(s) % i == 0:
            if (s[0:i]*(len(s)//i)) == s:
                return True