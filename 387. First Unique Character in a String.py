"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""
def firstUniqChar(self, s: str) -> int:
    arr = list(s)
    mydict = {}
    for i in range(len(arr)):
        if arr[i] not in mydict:
            mydict[arr[i]] = [i]
        else:
            mydict[arr[i]].append(i)
    
    for each in mydict:
        if len(mydict[each]) == 1:
            return mydict[each][0]
    return -1