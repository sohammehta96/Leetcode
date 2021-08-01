"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""
def countConsistentStrings(allowed, words):
    count = 0
    op = 0
    for each in words:
        for every in allowed:
            count += each.count(every)
        if count == len(each):
            op += 1
        count = 0
    return op