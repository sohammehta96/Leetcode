def quicksort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()
        
    items_greater = []
    items_lesser = []
    
    for item in seq:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lesser.append(item)
            
    return quicksort(items_lesser) + [pivot] + quicksort(items_greater)

    
sequence = [0,1,0,2,1,0,1,3,2,1,2,1]
print(quicksort(sequence))