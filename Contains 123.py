"""
Given an array arr[] of n numbers. The task is to print only those numbers whose digits are from set {1,2,3}.
"""
def contain123(arr):
    nums = []
    for i in range(len(arr)):
        if str(arr[i])[0] == '1' or str(arr[i])[0] == '2' or str(arr[i])[0] == '3':
            nums.append(arr[i])
    return nums

digits = [123,231,3,4,5,6,7,7,8,8,6,5,4,2333121,2,2]
print(contain123(digits))