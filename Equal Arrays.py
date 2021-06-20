"""
Given two given arrays of equal length, the task is to find if given arrays are equal or not. Two arrays
are said to be equal if both of them contain the same set of elements, arrangements (or
permutation) of elements may be different though.
Note: If there are repetitions, then counts of repeated elements must also be the same for two
arrays to be equal.
"""
def equalarray(arr1, arr2):
    mydict = {}
    equal = True
    for each in set(arr1):
        mydict[each] = arr1.count(each)
        
    for each in mydict.keys():
        if mydict[each] != arr2.count(each):
            equal = False
            break
            
    return equal


arr1 = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,5,6]
arr2 = [2,2,2,3,3,3,3,3,3,3,5,6,1,1,1,1,1,1,2,2,2]
print(equalarray(arr1,arr2))