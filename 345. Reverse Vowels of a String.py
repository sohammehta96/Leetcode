"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        indices = []
        letters = []
        new = list(s)
        for i in range(len(s)):
            if s[i].lower() == "a" or \
            s[i].lower() == "e" or \
            s[i].lower() == "i" or \
            s[i].lower() == "o" or \
            s[i].lower() == "u":
                indices.append(i)
                letters.append(s[i])
        for i in range(len(letters)):
            new[indices[i]] = letters[len(indices)-1-i]
        listToStr = ''.join([str(elem) for elem in new])
        return listToStr