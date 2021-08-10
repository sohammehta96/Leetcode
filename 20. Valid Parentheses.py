"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
def isValid(s: str) -> bool:
    arr = list(s)
    i = 0
    while len(arr) > 0 and i < len(arr)-1:
        if arr[i] == "(" and ord(arr[i]) == ord(arr[i+1])-1:
            arr.pop(i)
            arr.pop(i)
            i = 0
        elif ord(arr[i]) == ord(arr[i+1])-2:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    if len(arr) != 0:
        return False
    return True