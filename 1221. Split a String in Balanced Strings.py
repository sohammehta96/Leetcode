"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""

def balancedStringSplit(self, s: str) -> int:
    count = 0
    i = 0
    j = 2
    while j <= len(s):
        if s[i:j].count("R") == s[i:j].count("L"):
            count += 1
            i = j
            j += 1
        else:
            j += 1
    return count