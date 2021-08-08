"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""
def checkIfExist(self, arr: List[int]) -> bool:
    for each in arr:
        if each != 0 and 2*each in arr:
            return True
        if each == 0 and arr.count(0)>1:
            return True
    return False