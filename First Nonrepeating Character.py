"""
Given a string S consisting of lowercase Latin Letters. Find the first
non-repeating character in S.
"""
def firstnonrepeating(string):
    mydict = {}
    for each in string:
        if each not in mydict:
            mydict[each] = 1
        else:
            mydict[each] += 1

    for each in mydict:
        if mydict[each] == 1:
            char = each
            break
        else:
            char = -1
    return char

print(firstnonrepeating("rjbiunyguhbjuhgyitdytdhbz"))