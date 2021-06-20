def bubblesort(seq):
    sort = False
    
    while not sort:
        sort = True
        for i in range(0,len(seq)-1):
            if seq[i] > seq[i+1]:
                sort = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq

sequence = [0,1,0,2,1,0,1,3,2,1,2,1]
print(bubblesort(sequence))