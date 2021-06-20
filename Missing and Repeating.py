"""
Given an unsorted array Arr of size N of positive integers. 
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. 
Find these two numbers.
"""
def missandrepeat(arr):
    
    A = 0
    B = 0
    
    #count all
    mydict = {}
    for each in arr:
        if each not in mydict:
            mydict[each] = 1
        else:
            mydict[each] += 1
    
    #missing
    num = max(arr)
    while num > 0:
        if num in arr:
            num -= 1
        else:
            A = num
            break
       
    #repeat
    for each in mydict:
        if mydict[each] == 2:
            B = each
    
    return A, B
        
arr = [1, 3, 3]
arr = [2,2]

print(missandrepeat(arr))