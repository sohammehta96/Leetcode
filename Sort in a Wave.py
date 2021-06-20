"""
Sort an array in wave form
Difficulty Level: Medium
• Last Updated : 18 May, 2021
Given an unsorted array of integers, sort the array into a wave like array. An array'arr[0..n-1]' is
sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >=
"""
def quicksort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
    
    lower = []
    greater = []
    
    for each in seq:
        if each < pivot:
            lower.append(each)
        else:
            greater.append(each)
            
    return quicksort(lower) + [pivot] + quicksort(greater)

def bubblesort(seq):
    sort = False
    
    while not sort:
        sort = True
        for i in range(len(seq)-1):
            if seq[i] > seq[i+1]:
                sort = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq



a = quicksort([7,5,3,8,90,4,65,83,2,11,9,48,33])

new = a

for i in range(int(len(new)/2)):
    new[i*2],new[i*2+1] = new[i*2+1],new[i*2]